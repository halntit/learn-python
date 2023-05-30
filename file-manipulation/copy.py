### copy file
# copyfile: copy file content only
# copy: copy file content and permission (but not last modified time)
# copy2: copy file content and metadata (permission, last modified time, etc.)

import os
import shutil # shell utilities

print('copyfilecontent')
shutil.copyfile('file-manipulation/test.txt', 'file-manipulation/test-copy.txt')
isfilecreated = os.path.exists('file-manipulation/test-copy.txt') # True
print('isfilecreated', isfilecreated)
filepermission = os.stat('file-manipulation/test.txt').st_mode
filepermissioncopy = os.stat('file-manipulation/test-copy.txt').st_mode
print('filepermission', filepermission)
print('filepermissioncopy', filepermissioncopy)
lastmofiletime = os.path.getmtime('file-manipulation/test.txt')
lastmofiletimecopy = os.path.getmtime('file-manipulation/test-copy.txt')
print('lastmofiletime', lastmofiletime)
print('lastmofiletimecopy', lastmofiletimecopy)

print('==========')

print('copyfilecontent and permission')
shutil.copy('file-manipulation/test.txt', 'file-manipulation/test-copy2.txt')
isfilecreated = os.path.exists('file-manipulation/test-copy2.txt') # True
print('isfilecreated', isfilecreated)
filepermission = os.stat('file-manipulation/test.txt').st_mode
filepermissioncopy = os.stat('file-manipulation/test-copy2.txt').st_mode
print('filepermission', filepermission)
print('filepermissioncopy', filepermissioncopy)
lastmofiletime = os.path.getmtime('file-manipulation/test.txt')
lastmofiletimecopy = os.path.getmtime('file-manipulation/test-copy2.txt')
print('lastmofiletime', lastmofiletime)
print('lastmofiletimecopy', lastmofiletimecopy)

print('==========')
print('copyfilecontent, permission and metadata')
shutil.copy2('file-manipulation/test.txt', 'file-manipulation/test-copy3.txt')
isfilecreated = os.path.exists('file-manipulation/test-copy3.txt') # True
print('isfilecreated', isfilecreated)
filepermission = os.stat('file-manipulation/test.txt').st_mode
filepermissioncopy = os.stat('file-manipulation/test-copy3.txt').st_mode
print('filepermission', filepermission)
print('filepermissioncopy', filepermissioncopy)
lastmofiletime = os.path.getmtime('file-manipulation/test.txt')
lastmofiletimecopy = os.path.getmtime('file-manipulation/test-copy3.txt')
print('lastmofiletime', lastmofiletime)
print('lastmofiletimecopy', lastmofiletimecopy)