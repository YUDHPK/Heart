# Alternative (improved?) implementation of Measure-Command
# Works similarly to the Linux/Unix `time` command
#
# Function which times how long a command takes to completion
# Note that this function outputs to Write-Host so as to
# protect the proper return value. Note that a time will be
# returned even if the command fails.
#
# Unless `-quiet` is specified, command output is sent directly
# to `Write-Host` to allow for the simultaneous return of the
# elapsed time object.
#
# Returns: DateTime object representing how much time elapsed
#          for the duration of the command.
#
# Arguments:
#   -quiet : Suppress output from command (the difference
#            is still displayed and returned).
#   -command : The command (as a string) you wish to time.
#
# Usage:
#   time "echo hello world"
#   time -q "echo The command runs but suppresses the output"
#   $dateTimeObject = $(time "vagrant converge")


function time {
    Param(
        [Parameter(Mandatory=$true)]
        [string]$command,
        [switch]$quiet = $false
    )
    $start = Get-Date
    try {
        if ( -not $quiet ) {
            iex $command | Write-Host
        } else {
            iex $command > $null
        }
    } finally {
        $(Get-Date) - $start
    }
}