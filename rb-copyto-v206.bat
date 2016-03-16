mkdir c:\temp\rblogs

robocopy C:\n\Dropbox\csd\VCS-git\flaskplay \\10.4.11.27\home\albe\www\flaskplay   /e  /COPY:DT /xd  testnobackup /fft /dst /xo /ndl /np /r:0 /w:9 /tee /log:"c:\temp\rblogs\fplf1-%dhms%-%random%"

robocopy C:\n\Dropbox\csd\VCS-git\flaskplay \\v206bflask1\home\albe\www\flaskplay   /e  /COPY:DT /xd  testnobackup /fft /dst /xo /ndl /np /r:0 /w:9 /tee /log:"c:\temp\rblogs\fplf1b-%dhms%-%random%"

:robocopy C:\n\Dropbox\csd\VCS-git\cif207 \\v206b2\html\python\cif207   /e  /COPY:DT /xd .git templates_c testnobackup /fft /dst /xo /ndl /np /r:0 /w:9 /tee /log:"c:\temp\rblogs\cif207-%dhms%-%random%-%random%"

pause
