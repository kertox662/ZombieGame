@echo off
echo Preparing to Install Packages
echo
pause
py -3 -m pip install .\Dependencies\WheelsAndBatch\V3_4\Pillow\Pillow-5.0.0-cp34-cp34m-win32.whl --user
py -3 -m pip install .\Dependencies\WheelsAndBatch\V3_4\Pygame\pygame-1.9.3-cp34-cp34m-win32.whl --user
py -3 -m pip install pynput --user
echo All Packages Hopefully Installed
pause
cls
exit