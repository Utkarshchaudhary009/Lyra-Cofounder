$regPath = "HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\AppModelUnlock"
if (-not (Test-Path $regPath)) {
    New-Item -Path $regPath -Force | Out-Null
}
Set-ItemProperty -Path $regPath -Name "AllowDevelopmentWithoutDevLicense" -Value 1 -Type DWord
$val = (Get-ItemProperty -Path $regPath -Name "AllowDevelopmentWithoutDevLicense").AllowDevelopmentWithoutDevLicense
Write-Host "DeveloperMode set to $val"
