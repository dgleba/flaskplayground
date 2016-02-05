mkdir c:\temp\rblogs

robocopy C:\n\Dropbox\csd\VCS-git\cif207 \\v206b2\html\python\cif207   /e  /COPY:DT /xd .git templates_c testnobackup /fft /dst /xo /ndl /np /r:0 /w:9 /tee /log:"c:\temp\rblogs\cif207-%dhms%-%random%-%random%"

pause
