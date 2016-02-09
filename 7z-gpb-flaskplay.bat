:Prepare date and temp folders - http://serverfault.com/questions/147515/need-leading-zero-for-batch-script-using-time-variable
set timea=%TIME: =0%
set ymd=%date:~12,2%%date:~4,2%%date:~7,2%&set dhms=%date:~12,2%%date:~4,2%%date:~7,2%_%timea:~0,2%%timea:~3,2%%timea:~6,2%
c: & md c:\temp\log\"%dhms%"  & cd c:\temp\log\"%dhms%"

:main
rem ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ start here..

: below is not with prjfold
set srcdir=C:\n\Dropbox\csd\VCS-git
::next item is in the above folder.
set prjfold=flaskplay
set bkdir=c:\backup\flaskplay
set bkfname=flaskplay
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