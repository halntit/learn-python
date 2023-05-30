### move file

import os
import shutil # shell utilities

fileFrom = 'file-manipulation/test-move.txt'
fileTo = 'file-io/from-other-folder.txt'

print('movefile')
shutil.move(fileFrom, fileTo)
isfilecreated = os.path.exists(fileTo) # True
print('isfilecreated', isfilecreated)
isfileexisted = os.path.exists(fileFrom) # False
print('isfileexisted', isfileexisted)

print('==========')

print('movefile back')
shutil.move(fileTo, fileFrom)
isfilecreated = os.path.exists(fileFrom) # True
print('isfilecreated', isfilecreated)
isfileexisted = os.path.exists(fileTo) # False
print('isfileexisted', isfileexisted)

