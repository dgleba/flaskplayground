from . import *

from .viewsRbac import *

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#App specific views...
 
class customer_view(regularRbacView):

    column_searchable_list = ['CustomerId', 'City',  'Email', 'FirstName', 'LastName',]
    # make sure the type of your filter matches your hybrid_property
    column_filters = ['FirstName', 'LastName',  'City',  'Email'   ]
    # column_default_sort = ('part_timestamp', True)
    #column_export_list = ['CustomerId', 'City',  'Email', 'FirstName', 'LastName',]
   

    