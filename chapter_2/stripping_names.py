# Assign a name with whitespaces to a variable.
# Then remove the whitespaces with 3 stripping functions.
name = "\tPythonboy\t\n"

print(f"-{name.rstrip()}-")
print(f"-{name.lstrip()}-")
print(f"-{name.strip()}-")