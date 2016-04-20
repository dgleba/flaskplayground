'''
print column names for a table..
http://stackoverflow.com/questions/6039342/how-to-print-all-columns-in-sqlalchemy-orm
'''
import sys
from sqlalchemy import *

#db = create_engine('sqlite:///test.sqlite')
db = create_engine(r'sqlite:///c:\n\Dropbox\csd\VCS-git\flaskplay\251project\proj251b\project\fground.sqlite')

meta = MetaData()
meta.reflect(bind=db)

db.echo = False  # Try changing this to True and see what happens

'''
t1 = Table('cars', meta, autoload=True, autoload_with=db)
cnames = [ c.name for c in t1.columns ]
print cnames
'''

t1 = Table('users', meta, autoload=True, autoload_with=db)
cnames = [ c.name for c in t1.columns ]
print cnames


print [cname for cname in db.__dict__.keys()]


from sqlalchemy.orm import class_mapper
import sqlalchemy



def attribute_names(cls):
    return [prop.key for prop in class_mapper(cls).iterate_properties
        if isinstance(prop, sqlalchemy.orm.ColumnProperty)]
        
#attribute_names(t1)        