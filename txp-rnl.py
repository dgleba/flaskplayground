# remove newlines..

# %wpy% txp-rnl.py

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# i don't get this one...
#http://stackoverflow.com/questions/18865210/how-to-strip-newlines-from-each-line-during-a-file-read
# good:
#http://stackoverflow.com/questions/4791080/delete-newline-return-carriage-in-file-output

# works...
rf = open("modelsgen.txt")
wf = open("tmpout9.txt","w")
for line in rf:
    newline = line.rstrip('\n')
    wf.write(newline)
    # wf.write('\n') # this adds newline to each line so there will only be one new line - i think. Comment this out for zero newlines.
    
    
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# # result: this removes empty lines.
    
# #!/usr/bin/env python
# import fileinput

# import shutil
# shutil.copy2('modelsgen.txt', 'tmpout2.txt')

# for line in fileinput.input("tmpout2.txt", inplace=True):
    # if line != '\n':
        # line.strip("\r\n")
        # print line,  
       
       
       