import os

# List all files in a directory using os.listdir
basepath = 'santvani\\'

i = 0

for dirpath, dirnames, files in os.walk(basepath):
    filecount = 0
    print(f'Found directory: {dirpath}')
    for file_name in files:
        if (os.path.splitext(file_name)[1] == '.mp3'):
            i = i + 1
            filecount += 1
            oldPath = (os.path.join(dirpath, file_name))
            newPath = f"{i:04d}" + ".mp3"
            print('Old Path - ' + oldPath + ' New Path ' + newPath)
            os.rename(oldPath, newPath)

    print(f'Total Files in Dir   ' + str(filecount))
