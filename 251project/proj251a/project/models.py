from . import *

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Define models directly without reflection...
class Customer(db.Model):
    CustomerId = db.Column(db.Integer(), primary_key=True)
    FirstName = db.Column(db.Unicode(40), nullable=False)
    LastName = db.Column(db.String(20), nullable=False)
    City = db.Column(db.Unicode(40))
    Email = db.Column(db.Unicode(60), unique = True)
 
    def __str__(self):
        return self.CustomerID
        
class City(db.Model):
    Id = db.Column(db.Integer(), primary_key=True)
    City = db.Column(db.Unicode(40), unique = True)
 
    def __str__(self):
        return self.ID
        
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
