:Prepare date and temp folders
set ymd=%date:~12,2%%date:~4,2%%date:~7,2%&set dhms=%date:~12,2%%date:~4,2%%date:~7,2%_%time:~0,2%%time:~3,2%%time:~6,2%
c: & md c:\temp\ & cd c:\temp & md c:\temp\log & md c:\temp\log\"%dhms%"  & cd c:\temp\log\"%dhms%"
:main
:goto skip1

rem ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ start here..
: below is not with prjfold
set srcdir=C:\n\Dropbox\csd\VCS-git
::next item is in the above folder.
set prjfold=cif207
set bkdir=c:\backup\cif207
set bkfname=cif207
set dbxcpy=C:\n\Dropbox\csd\copyof
rem ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ %bkfname%
:Title:
:7z-gpb = 7zip generic project folder backup routine...  David Gleba 2015-07-10

mkdir %bkdir%

del "%bkdir%\%bkfname%.%computername%.7z"
:timeout 2

:backup...
C:\n\Dropbox\csd\p2\7-Zip\7z.exe a -y -t7z  -xr!xdirx   "%bkdir%\%bkfname%.%computername%.%dhms%.7z"  %srcdir%\%prjfold%  

:copy
mkdir %dbxcpy%\%prjfold%
copy "%bkdir%\%bkfname%.%computername%.%dhms%.7z" %dbxcpy%\%prjfold%\%bkfname%.%computername%.latest.7z



rem ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ %bkfname%












:..........  offline items  ................................................
goto end
goto end
goto end
:#######




:#######
:end
pause