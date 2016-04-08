from . import *

  
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#Typical RBAC views...
    
# Create customized model view class
class dgBaseView(sqla.ModelView):

    column_display_pk = True
    page_size = 20
    can_view_details = True
    #can_export = False
    can_export = True

    def _handle_view(self, name, **kwargs):
        """
        Override builtin _handle_view in order to redirect users when a view is not accessible.
        """
        if not self.is_accessible():
            if current_user.is_authenticated:
                # permission denied
                abort(403)
            else:
                # login
                return redirect(url_for('security.login', next=request.url))

              
class regularRbacView(dgBaseView):

    def is_accessible(self):

        # set accessibility...
        if not current_user.is_active or not current_user.is_authenticated:
            return False

        # roles not tied to ascending permissions...
        if  not current_user.has_role('export'):
            self.can_export = False
            
        # roles with ascending permissions...
        if current_user.has_role('adminrole'):
            self.can_create = True
            self.can_edit = True
            self.can_delete = True
            self.can_export = True
            return True
        if current_user.has_role('supervisor'):
            self.can_create = True
            self.can_edit = True
            self.can_delete = False
            return True
        if current_user.has_role('user'):
            self.can_create = True
            self.can_edit = True
            self.can_delete = False
            return True
        if current_user.has_role('create'):
            self.can_create = True
            self.can_edit = False
            self.can_delete = False
            return True
        if current_user.has_role('read'):
            self.can_create = False
            self.can_edit = False
            self.can_delete = False
            return True
        return False
 
class lookupRbacView(dgBaseView):

    def is_accessible(self):
        # set accessibility...
        if not current_user.is_active or not current_user.is_authenticated:
            return False

        # roles not tied to ascending permissions...
        if  not current_user.has_role('export'):
            self.can_export = False
            
        # roles with ascending permissions...
        if current_user.has_role('adminrole'):
            self.can_create = True
            self.can_edit = True
            self.can_delete = True
            self.can_export = True
            return True
        if current_user.has_role('supervisor'):
            self.can_create = True
            self.can_edit = True
            self.can_delete = False
            return True
        if current_user.has_role('user'):
            self.can_create = False
            self.can_edit = False
            self.can_delete = False
            return True
        if current_user.has_role('create'):
            self.can_create = False
            self.can_edit = False
            self.can_delete = False
            return True
        if current_user.has_role('read'):
            self.can_create = False
            self.can_edit = False
            self.can_delete = False
            return True
        return False
 
class SuperView(dgBaseView):

    can_export = True

    def is_accessible(self):
        if not current_user.is_active or not current_user.is_authenticated:
            return False
        if current_user.has_role('adminrole'):
            self.can_create = True
            self.can_edit = True
            self.can_delete = True
            #self.can_export = True
            return True
        return False
 
    

    