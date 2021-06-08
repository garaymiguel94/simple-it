@echo off

echo Finding new IP for Pinpad

FOR /L %%i IN (1,1,254) DO ping -n 1 192.168.1.%%i | FIND /i "Reply"

arp -a | FIND /i "mac-address" > test.txt

for /f "usebackq" %%a in ( "pinpadmatch.txt" ) do (
    set a=%%a
    goto done
)
:done
echo New ip: %a%
echo %a%

sqlcmd -S localhost\pcamerica -U user -P password -s, -W -Q "UPDATE [database].[dbo].[Payment_Processing_Config] SET [PrimaryUrl] = '%a%' WHERE PortNumber = 1" > ippinpad.txt 
echo new ip was placed in CRE check now
pause
