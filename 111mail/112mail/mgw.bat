: mgw.bat - means - managewindows.bat

:Prepare date and temp folders - http://serverfault.com/questions/147515/need-leading-zero-for-batch-script-using-time-variable
set timea=%TIME: =0%
set ymd=%date:~12,2%%date:~4,2%%date:~7,2%&set dhms=%date:~12,2%%date:~4,2%%date:~7,2%_%timea:~0,2%%timea:~3,2%%timea:~6,2%
:c: & md c:\temp\log\"%dhms%"  & cd c:\temp\log\"%dhms%"

:main
rem ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ mgw


:cd C:\n\Dropbox\csd\VCS-git\flaskplay


set wpip=c:\p2\Python27\Scripts\pip

 %wpip% install -e git+https://github.com/flask-admin/flask-admin.git@master#egg=flask-admin
 
 %wpip% install -r requirements.txt


set wpy=c:\p2\python27\python

c:\p2\python27\scripts\sqlacodegen sqlite:///test.sqlite > modelsgen.txt

txp-fl.py

:  %wpy% txp-fl.py
:  %wpy% flplay2.py
:  %wpy% flplay.py



: %wpy% flpg6.py

: fltg.py



: timeout 987

rem ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ mgw







: offline items ---------------------------------------------------------
goto end
goto end
goto end


this is offline


: offline items ---------------------------------------------------------
:end
pause
