$base = "G:\Lyra-Cofounder\yt-content"
$log = Join-Path $base "makelinks.log"
Start-Transcript -Path $log -Force | Out-Null
$names = @("grill-with-docs", "writing-for-agents")
foreach ($n in $names) {
    $link = Join-Path $base ".agents\skills\$n"
    $target = Join-Path $base ".opencode\skills\$n"
    if (Test-Path $link) { Remove-Item -Recurse -Force $link }
    New-Item -ItemType SymbolicLink -Path $link -Target $target | Out-Null
    Write-Host "symlink: $link -> $target"
}
Get-ChildItem -Force (Join-Path $base ".agents\skills") | Select-Object Mode, Name, Target, LinkType | Format-Table -AutoSize | Out-String -Width 200 | Write-Host
Stop-Transcript | Out-Null
