import os

# read directory and sub directories


def dir_walker(path):
    for root, dirs, files in os.walk(path):
        for file_ in files:
            print(os.path.join(root, file_))


def dir_printer(path):
    for root, dirs, files in os.walk(path):
        for filename in files:
            if filename.endswith(".py"):
                print (os.path.join(root, filename))
            else:
                continue


if __name__ == '__main__':
    dir_walker('/Users/lizeganjohnson/Documents/google-python-exercises')
    print "+" * 30
    dir_printer('/Users/lizeganjohnson/Documents/google-python-exercise')
    print "-" * 30

# write files to txt file
#     with open('listfiles.txt', 'w') as in_files:
#         in_files.write(files + '\n')
# read list copy matching files to new directory
