# Work with multiple modules.
# Prove the work works.
import privileges_module
import admin_module

admin = admin_module.Admin('admin', None, None, None, None)

print(f"To {admin.first_name.title()}")

privileges = privileges_module.Privileges()
privileges.show_privileges()