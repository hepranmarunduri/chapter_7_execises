# Work with a module that has multiple class.
# And prove the imported module works.

import module_admin

admin = module_admin.Admin('admin', None, None, None, None)

admin.admin_privileges.show_privileges()