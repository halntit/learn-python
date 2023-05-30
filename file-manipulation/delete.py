### delete file:

import os
import shutil # shell utilities

filePath = 'file-manipulation/test-delete.txt';

def createFile(filePath):
    file = open(filePath, 'w+')
    file.write('This is a test file')
    file.close()

def deleteFile(filePath):
    try:
        os.remove(filePath)
    except OSError as e:
        print('file not found')
    except PermissionError as e:
        print('permission denied')
    except Exception as e:
        print('error occured')
    else:
        print('file deleted successfully')

def createFolder(folderPath):
    try:
        os.mkdir(folderPath)
    except OSError as e:
        print('folder already existed')
    except PermissionError as e:
        print('permission denied')
    except Exception as e:
        print('error occured')
    else:
        print('folder created successfully')

def deleteFolder(folderPath, force=False):
    try:
        if force:
            shutil.rmtree(folderPath) # remove folder and all its content
        else:
            os.rmdir(folderPath)
    except OSError as e:
        print(e)
    except PermissionError as e:
        print('permission denied')
    except Exception as e:
        print('error occured')
    else:
        print('folder deleted successfully')

# createFile(filePath)
# deleteFile(filePath)

folderPath = 'file-manipulation/test-delete-folder'
createFolder(folderPath)
createFile('file-manipulation/test-delete-folder/test-delete-file.txt') # create file inside folder
deleteFolder(folderPath) # delete folder with file inside it (will throw error)
# deleteFolder(folderPath, True) # delete folder with file inside it