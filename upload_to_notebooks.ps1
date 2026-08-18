$dbPath = "db.json"

# Load the database
if (Test-Path $dbPath) {
    $db = Get-Content $dbPath | ConvertFrom-Json
} else {
    Write-Host "Error: db.json not found!" -ForegroundColor Red
    exit 1
}

$pendingCount = ($db | Where-Object { $_.status -eq "pending" }).Count
Write-Host "Found $pendingCount pending uploads in db.json." -ForegroundColor Cyan

foreach ($entry in $db) {
    if ($entry.status -eq "pending") {
        Write-Host "Uploading to [$($entry.notebook_name)]: $($entry.url)"

        # Execute nlm CLI and capture the JSON output
        $output = nlm source add $entry.notebook_id --url $entry.url --json | Out-String
        
        try {
            $response = $output | ConvertFrom-Json
            
            # The test showed a successful response contains "source_id"
            if ($null -ne $response.source_id) {
                Write-Host "  [SUCCESS] Added source ID: $($response.source_id)" -ForegroundColor Green
                $entry.status = "success"
                
                # Save progress immediately so if script stops, we don't lose the state
                $db | ConvertTo-Json -Depth 10 | Set-Content $dbPath
            } 
            # The test showed a failed response contains "error"
            elseif ($null -ne $response.error) {
                Write-Host "  [FAILED] $($response.error) - $($response.hint)" -ForegroundColor Red
            } 
            else {
                Write-Host "  [WARNING] Unexpected response: $output" -ForegroundColor Yellow
            }
        } catch {
            Write-Host "  [FAILED] Could not parse CLI output. Output was:" -ForegroundColor Red
            Write-Host "  $output"
        }
        
        # Respect NotebookLM rate limits (2 seconds between source operations)
        Start-Sleep -Seconds 2
    }
}

Write-Host "Script completed! You can re-run this script anytime to retry pending uploads." -ForegroundColor Cyan