$ErrorActionPreference = "Stop"
$required = @("system","routers","frameworks","commands","chatgpt","codex","skills","templates","checklists","examples","docs","scripts",".github")
$missing = @()
foreach ($folder in $required) {
  $path = Join-Path $PSScriptRoot "../$folder/README.md"
  if (-not (Test-Path $path)) { $missing += $path }
}
if ($missing.Count -gt 0) {
  Write-Error ("Missing documentation:`n" + ($missing -join "`n"))
}
Write-Host "Documentation structure looks complete."
