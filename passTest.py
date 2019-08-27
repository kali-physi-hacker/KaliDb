import sys, msvcrt

password = ''
while True:
    x = msvcrt.getch()
    if x == '\r':
        break
    sys.stdout.write("*")
    password += x
    if x == '\b':
        password += '\010'
print '\n'+password

