secret_password = 'group55'
user_pass = ''

tries = 3

while tries > 0 and user_pass != secret_password:
    user_pass = input('Enter password (you have ' + str(tries) + 'tries left: ')

    tries -= 1

    if user_pass == secret_password:
        print('Access Granted.')
    elif tries == 0:
        print("you dont have any tries :(")
    else:
        print('Access Denied, try again 🙂 ')