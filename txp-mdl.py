# create model...
# process sqlacodegen output to create model...

# %wpy% txp-mdl.py

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#output file..
wf = open("modelsgen-m.txt","w")
#input file..
with open("modelsgen.txt", "r") as f:
    for line in f:
        # add db.
        line = line.replace('= Column(', '= db.Column(db.') 
        wf.write(line)


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
