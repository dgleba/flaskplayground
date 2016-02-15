# create field list...
#
# process sqlacodegen output to create comma delimited fields list that
# can be copied and pasted into flask-admin app...

# David Gleba 2016-02-09

# %wpy% txp-fl.py

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# phase 1  remove white space and add ', to the = signs.

#output file..
wf = open("tmpout1.txt","w")
#input file..
with open("modelsgen.txt", "r") as f:
    for line in f:
        # remove white space
        line = line.replace(' ', '') 
        # replace = with ",=  -- we will get rid of the = later..
        line = line.replace("=", "',=") 
        wf.write(line)


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#phase 2 - add a ' to the begininng of every line..

#http://stackoverflow.com/questions/7633485/insert-string-at-the-beginning-of-each-line

infile = 'tmpout1.txt'
with open(infile) as finput:
    with open('tmpout2.txt', 'w') as fout:
        for line in finput:
            fout.write("'"+line)


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#phase 3 -  if tablename is not found in the line, remove everything after the = sign.

#ref..
#http://stackoverflow.com/questions/3437059/does-python-have-a-string-contains-substring-method

    
#in file... 
rf = open("tmpout2.txt")
#output file..
wf = open("modelsgen-fieldlist.txt","w")
for line in rf:
    if line.find("_tablename_") == -1:  # if that string is not found..
        # remove everything after the = sign. i guess it gets rid of the newline as well, this is what I want.
        sep = '='
        beg = line.split(sep, 1)[0]
        wf.write(beg)
    else:
        wf.write(line) #if it is found.. (in my case -- do nothing - just write the line that was found.)
    

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
