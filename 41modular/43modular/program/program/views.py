from . import *

@app.route('/')  # Flask views
def index():
    return '<a href="/admin/">Click me to get to Admin!</a>'
    
class CarAdmin(sqla.ModelView):
    form_overrides = dict(cartype=SelectField)
    form_args = dict(cartype=dict(choices=[
                ('', 'Please Select'),
                ('Compact', 'Compact'),
                ('Mid-size', 'Mid-size'),
                ('Pickup Truck', 'Pickup Truck')
            ]))
