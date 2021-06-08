echo off

REM ****** This batch file is only for the CRE POS systems. ******
REM ****** Pings to see if the ip of pinpad is reachable ******
REM ******                                                  ******

echo Pinging Sources

ping -n 1 8.8.8.8 | find "TTL=" >nul
if errorlevel 1 (
    echo Unable to reach internet
) else (
    echo Able to reach internet
)

echo -----------------------------------

echo Pinging Pinpad in CRE DB

REM ****** Finds the ip address in the CRE database. Note: If trying to use on merchant change the database name******
sqlcmd -S localhost\pcamerica -U user -P password -s, -W -Q "SELECT [PrimaryUrl] FROM [database].[dbo].[Payment_Processing_Config] where PortNumber = 1" > ippinpad.txt

for /f "skip=2" %%G IN (ippinpad.txt) DO if not defined line set "line=%%G"
echo %line%

REM ****** Pings the IP address in the database******
ping -n 1 %line% | find "TTL=" >nul
if errorlevel 1 (
    echo Unable to reach pinpad....check IP Adress on Pinpad or Internet Connection
) else (
    echo Able to reach pinpad
)

echo -----------------------------------
echo The Status of Firewalls

netsh advfirewall show allprofiles state


pause


