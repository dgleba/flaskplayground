# clean sqlacodegen for comma delimited fields list...

# %wpy% txp-Rmw.py

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#output file..
wf = open("tmpout1.txt","w")
#input file..
with open("modelsgen.txt", "r") as f:
    for line in f:
        # remove white space
        line = line.replace(' ', '') 
        # replace = with ",=  -- we will get rid of the = later..
        line = line.replace('=', '",=') 
        wf.write(line)


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#http://stackoverflow.com/questions/7633485/insert-string-at-the-beginning-of-each-line

infile = 'tmpout1.txt'
with open(infile) as finput:
    with open('tmpout2.txt', 'w') as fout:
        for line in finput:
            fout.write('"'+line)


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#ref..
#http://stackoverflow.com/questions/3437059/does-python-have-a-string-contains-substring-method

    
#in file... 
rf = open("tmpout2.txt")
#output file..
wf = open("tmpout3.txt","w")
for line in rf:
    if line.find("_tablename_") == -1:  # if that string is not found..
        # remove everything after the = sign. i guess it gets rid of the newline as well, this is what I want.
        sep = '='
        beg = line.split(sep, 1)[0]
        wf.write(beg)
    else:
        wf.write(line) #if it is found.. (in my case -- do nothing - just write the line that was found.)
    

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
