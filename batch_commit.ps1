$files = Get-Content untracked_files.txt
$files += Get-Content modified_files.txt

$chunkSize = 10
$counter = 5 # skip first 5 as they were already committed

while ($counter -lt $files.Count) {
    $chunk = $files | Select-Object -Skip $counter -First $chunkSize
    if ($chunk.Count -eq 0) { break }
    
    foreach ($file in $chunk) {
        if ($file.Trim() -ne "") {
            git add "`"$file`""
        }
    }
    
    git commit -m "chore: batch commit part $([math]::floor($counter/$chunkSize) + 1)"
    $counter += $chunkSize
}
