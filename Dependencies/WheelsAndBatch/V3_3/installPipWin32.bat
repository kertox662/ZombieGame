@echo off
echo Preparing To Install Pip
py -3 .\Dependencies\WheelsAndBatch\get-pip.py --user
pause
start Dependencies\WheelsAndBatch\V3_3\installPackagesWin32
cls
exit