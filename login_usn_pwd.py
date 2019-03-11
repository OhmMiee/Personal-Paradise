def LOGIN(usn, pwd):
    u = input('Please enter your Username: ')
    p = input('Please enter your Password: ')
    if u == usn and p == pwd:
        return True
    else :
        print('Username or password is wrong')
        return False

def HOME(usn):
    print ('Hello', usn)
    print ('Welcome to the Personal Paradise')

username = 'uSer'
password = 'pAss'

if LOGIN(username, password) == True:
    HOME(username)
else:
    print('ลาก่อย..')