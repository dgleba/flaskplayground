'''
create field list and flask models for sqla from sqlacodegen...
David Gleba 2016-02-09

purpose:
process sqlacodegen output to create comma delimited fields list that
can be copied and pasted into flask-admin app...

This reads file: modelsgen.txt

output: modelsgen-fieldlist.txt  and...

python txp-fl.py
or
%wpy% txp-fl.py
'''

print "\nReading input file modelsgen.txt...\n"
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# make /tmp folder

import os, errno

def make_sure_path_exists(path):
    
    try:
        os.mkdir(path)
        print "\nMaking tmp folder our using existing one...\n"
    except OSError as exc:
        if exc.errno != errno.EEXIST:
            print "\n PROBLEM Oops.. There seems to be a problem making the tmp folder.\n"
            raise exc
        pass

    # check to see if path name exists as a file.
    if os.path.isfile(path):
        #let user know there is a naming problem with the /tmp folder...
        print "\n\n PROBLEM:  hmm.. /tmp does exist as a file at this time. Can't create it as a folder\n"
    else:
        print "INFO.. Temp folder. Using folder /tmp."

    try:
        os.makedirs(path)
    except OSError as exception:
        if exception.errno != errno.EEXIST:
            raise
        
make_sure_path_exists("/tmp")    

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# phase 1  remove white space and add ', to the = signs.

#output file..
wf = open("/tmp/tmpout1.txt","w")
#input file..
with open("modelsgen.txt", "r") as f:
    for line in f:
        # remove white space
        line = line.replace(' ', '') 
        # replace = with ",=  -- we will get rid of the = later..
        line = line.replace("=", "',=") 
        wf.write(line)
wf.close()
f.close()
        
import time
time.sleep(.3)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#phase 2 - add a ' to the begininng of every line..

#http://stackoverflow.com/questions/7633485/insert-string-at-the-beginning-of-each-line

infile = '/tmp/tmpout1.txt'
with open(infile) as finput:
    with open('/tmp/tmpout2.txt', 'w') as fout:
        for line2 in finput: 
            #print line2               #print for debugging
            #line3= ("'"+line2)        #print for debugging
            #print line3              #print for debugging
            fout.write("'"+line2)
fout.close()
finput.close()

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#phase 3 -  if tablename is not found in the line, remove everything after the = sign.

#ref..
#http://stackoverflow.com/questions/3437059/does-python-have-a-string-contains-substring-method

    
#in file... 
rf = open("/tmp/tmpout2.txt")
#output file..
wf = open("/tmp/tmpout3.txt","w")
for line in rf:
    if line.find("_tablename_") == -1:  # if that string is not found..
        # remove everything after the = sign. i guess it gets rid of the newline as well, this is what I want.
        sep = '='
        beg = line.split(sep, 1)[0]
        wf.write(beg)
    else:
        wf.write(line) #if it is found.. (in my case -- do nothing - just write the line that was found.)
wf.close()
rf.close()
    

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# views:

# views look like this.. 'Column('fullcommonname',String(33)),

# remove all after ,

#in file... 
rf = open("/tmp/tmpout3.txt")
#output file..
wf = open("/tmp/tmpout4.txt","w")
for line in rf:
    if line.find("'Column(") >= 0:  # if that string is not found..
        # debug.. print "column found"
        # remove everything after the ,  . i guess it gets rid of the newline as well.
        sep = ','
        beg = line.split(sep, 1)[0]
        beg2= beg+",_zxz_\n"
        wf.write(beg2)
    else:
        wf.write(line) #if it is found.. (in my case -- do nothing - just write the line that was found.)
wf.close()
rf.close()


time.sleep(.1)


# remove >>  'Column('

#in file... 
rf = open("/tmp/tmpout4.txt")
#output file..
wf = open("/tmp/tmpout5.txt","w")
for line in rf:
    # remove >>  'Column('
        line = line.replace("'Column(", '') 
        wf.write(line)
wf.close()
rf.close()


# remove everything after the , sign. i guess it gets rid of the newline as well, this is what I want.

#in file... 
rf = open("/tmp/tmpout5.txt")
#output file..
wf = open("modelsgen-fieldlist.txt","w")
for line in rf:
    if line.find("_zxz_") > -1:  # if that string is not found..
        # remove everything after the , sign. i guess it gets rid of the newline as well, this is what I want.
        sep = ','
        beg = line.split(sep, 1)[0]
        wf.write(beg+",")
    else:
        wf.write(line) #if it is found.. (in my case -- do nothing - just write the line that was found.)
wf.close()
rf.close()

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# add  " db. "  to models so the can be used in flask with sqlalchemy...
# there are several replacements needed..
# and..  from.. "Column('"  to..  "db.Column('" .   
# and  from ..  blah   to.. " = db.Table("

#output file..
wf = open("/tmp/tempout41.txt","w")
#input file..
with open("modelsgen.txt", "r") as f:
    for line in f:
        # replace x with  ..
        line = line.replace("= Column(", "= db.Column(db.") 
        line = line.replace("Column('", "db.Column('") 
        line = line.replace(" = Table(", " = db.Table(") 
        wf.write(line)
wf.close()
f.close()

#output file..
wf = open("/tmp/tempout42.txt","w")
#input file..
with open("/tmp/tempout41.txt", "r") as f:
    for line in f:
        # replace x with xx
        line = line.replace("(Base):", "(db.Model):") 
        wf.write(line)
wf.close()
f.close()

#output file..
wf = open("models.db.flask-sqla.txt","w")
#input file..
with open("/tmp/tempout42.txt", "r") as f:
    for line in f:
        # replace this with that
        line = line.replace(", ForeignKey", ", db.ForeignKey") 
        wf.write(line)
wf.close()
f.close()

print "\nFINISHED.. Look for output files: modelsgen-fieldlist.txt, models.db.flask-sqla.txt. \n"

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
