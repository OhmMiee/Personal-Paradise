def LOGIN(usn, pwd):
    u = input('USERNAME: ')
    p = input('PASSWORD: ')
    if u == usn and p == pwd:
        return True
    else:
        print('Wrong username or password')
        return False
    
def HOME(usn):
    print('HELLO!', usn)
    print('Welcome to PERSONAL PARADISE')
    
username = 'user'
password = 'pass'

if LOGIN(username, password):
    HOME(username)
else:
    print('BYE!')
    
    
            