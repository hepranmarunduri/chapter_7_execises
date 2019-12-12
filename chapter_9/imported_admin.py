from privileges import *

admin = Admin(None, None, None, None, None)

admin.admin_privileges.show_privileges()

# Note:
# There will be a double outputs.
# It happens because in the module (privileges.py) there's some lines of code 
# that calls show_privileges() method.