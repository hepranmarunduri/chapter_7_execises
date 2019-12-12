# Import a function in different ways.

# Format 1: import module_name
import album_function
print(album_function.make_album('a7x', 'avenged sevenfold'))

# from module_name import function_name
from album_function import make_album
print(make_album('a7x', 'avenged sevenfold'))

# from module_name import function_name as fn
from album_function import make_album as ma
print(ma('a7x', 'avenged sevenfold'))

# import module_name as mn
import album_function as af
print(af.make_album('a7x', 'avenged sevenfold'))

# from module_name import *
from album_function import *
print(make_album('a7x', 'avenged sevenfold'))