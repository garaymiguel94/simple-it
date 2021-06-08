echo off

echo Pinging Sources

ping -n 1 8.8.8.8 | find "TTL=" >nul
if errorlevel 1 (
    echo Unable to reach internet
) else (
    echo Able to reach internet
)

echo -----------------------------------
echo The Status of Firewalls

netsh advfirewall show allprofiles state


pause


