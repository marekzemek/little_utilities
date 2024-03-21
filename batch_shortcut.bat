@echo off

if "%~n0"=="batch_shortcut" (
    echo Alternative shortcut solution. 
    echo Searches the current drive for an executable and launches it.
    echo Can take a bit longer to execute, but does not rely on absolute or even relative paths to the target file.
    echo ___
    echo HOW TO USE: just name this batch file exactly the same as the EXE you would like it to launch.
    echo EXAMPLE: to launch App.exe on drive F:, rename this file to App.bat and place it somewhere on F: 
    pause
    EXIT 0
    )

rem get filename and drive letter
rem https://stackoverflow.com/questions/8797983/can-a-windows-batch-file-determine-its-own-file-name
set filename="%~n0.exe"
set drive=%~d0
echo Looking for %filename% in %drive%

rem more about the dir command: https://www.lifewire.com/dir-command-4050018
rem get the first match (comment out goto FOUND to get the last match)
for /f "delims=" %%a in ('dir "%drive%\%filename%" /s /b') do (
    set "executable=%%a"
    if defined executable (
        goto FOUND
    )
)
rem https://stackoverflow.com/questions/47450531/batch-write-output-of-dir-to-a-variable

echo File not found
timeout /t 2
EXIT 0

:FOUND
echo Launching %executable%
start "" "%executable%"
echo Done
EXIT 0

