<#
.SYNOPSIS
    PowerShell Test Runner Wrapper for Ukrainian Poetry & Suno AI Skill System.
.DESCRIPTION
    Runs the automated E2E test suite across Tiers 1-4 using the available Python runtime.
.PARAMETER Tier
    Optional tier number (1, 2, 3, 4, or All). Default is 'All'.
.PARAMETER Test
    Optional specific test ID to execute.
.PARAMETER Verbose
    Enables detailed assertion outputs.
.EXAMPLE
    .\tests\run_tests.ps1 -Tier All
    .\tests\run_tests.ps1 -Tier 1
    .\tests\run_tests.ps1 -Test TC_T2_01_Taboo_6Words_Ban
#>

[CmdletBinding()]
param(
    [Parameter(Position = 0)]
    [ValidateSet("1", "2", "3", "4", "All", "all")]
    [string]$Tier = "All",

    [Parameter()]
    [string]$Test = "",

    [Parameter()]
    [switch]$VerboseOutput
)

$ErrorActionPreference = "Stop"

# Find Python executable
$PythonCmd = $null
if (Get-Command py -ErrorAction SilentlyContinue) {
    $PythonCmd = "py -3"
} elseif (Get-Command python -ErrorAction SilentlyContinue) {
    $PythonCmd = "python"
} else {
    Write-Error "Python 3 runtime not found in PATH. Please ensure Python 3 is installed."
    exit 1
}

$ScriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$RunnerScript = Join-Path $ScriptDir "run_tests.py"

$ArgsList = @()
if ($Test) {
    $ArgsList += "--test"
    $ArgsList += $Test
} elseif ($Tier -eq "All" -or $Tier -eq "all") {
    $ArgsList += "--all"
} else {
    $ArgsList += "--tier"
    $ArgsList += $Tier
}

if ($VerboseOutput) {
    $ArgsList += "--verbose"
}

Write-Host "Running: $PythonCmd `"$RunnerScript`" $($ArgsList -join ' ')" -ForegroundColor DarkCyan

if ($PythonCmd -eq "py -3") {
    & py -3 "$RunnerScript" @ArgsList
} else {
    & python "$RunnerScript" @ArgsList
}

exit $LASTEXITCODE
