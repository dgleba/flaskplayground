# create model...
# process sqlacodegen output to create model...

# David Gleba 2016-02-09


# %wpy% txp-mdl.py

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# output file..
wf = open("modelsgen-mdl.txt","w")
# input file..
with open("modelsgen.txt", "r") as f:
    for line in f:
        # add db.
        line = line.replace('= Column(', '= db.Column(db.') 
        wf.write(line)


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
