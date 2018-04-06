import hashlib # NOTE:  Imported Library like hashlib and Sys all native Python libs made in Python3!
import sys


print('Welcome to HashCompare!\n'
'Use the File path to compare your hashes!\n'
'If you dont want to Compare just leave it blank or type y ! \n\n')



# NOTE: this is md5 hash code section!

Filename = input("Enter PATH to File:")
compare=input('CompareFile:')
openfile = open(Filename)
readme = openfile.read(128)
trans=readme.encode('utf8')
md5 = hashlib.md5()
md5.update(trans)
print("MD5: {0}".format(md5.hexdigest()))
print('\n\n')

if compare == 'y': # NOTE:  this Section contains the code to compare 2 Files in MD5! if you want Sha1 just change all .md5() to .sha1()
    input=input('File PATH to compare:')
    open=open(input)
    reading=open.read(128)
    encoding=reading.encode('utf8')
    hash=hashlib.md5()
    hash.update(encoding)
    print('MD5:{0}'.format(md5.hexdigest()))
    print('\n')
    print('MD5:{0}'.format(hash.hexdigest()))
    print('\n')
    print('Done!')

# NOTE: End of Coding!
