# Work with multiple modules.
# Prove the work works.

import admin_privileges

admin = admin_privileges.Admin('admin', None, None, None, None)

admin.admin_privileges.show_privileges()