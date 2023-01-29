@echo off
rem Alternative shortcut solution. Searches the current drive for the file 
rem specified in "filename". Can take a bit longer to execute, but does not rely
rem on absolute or even relative paths to the target file.

rem set filename to the exe to be launched
set filename="filename.exe"
echo Looking for %filename% in %~d0

rem more about the dir command: https://www.lifewire.com/dir-command-4050018
rem get the first match (comment out goto FOUND to get the last match)
for /f "delims=" %%a in ('dir "%~d0\%filename%" /s /b') do (
    set "name=%%a"
    if defined name (
        echo %name% inside for loop
        goto FOUND
    )
)
rem https://stackoverflow.com/questions/47450531/batch-write-output-of-dir-to-a-variable

echo File not found
timeout /t 2
EXIT 0

:FOUND
echo Launching %name%
start "" "%name%"
echo Done
EXIT 0






