from datetime import datetime
from time import sleep


user_database = {
    'Seyi': {
        'password': 'seyi123', 'balance': 100500, 'accountNumber': '0000000001'
        },
    'Mike': {
        'password': 'mike123', 'balance': 85200, 'accountNumber': '0000000002'
        }
}

current_user = None
last_account_number = 2


def displayDateTime():
    weekdayNames = [
        'Monday', 'Tuesday', 'Wednesday',
        'Thursday', 'Friday', 'Saturday',
        'Sunday'
    ]
    monthName = [
        'January', 'February', 'March', 'April',
        'May', 'June', 'July', 'August', 'September',
        'October', 'November', 'December'
    ]
    now = datetime.now()
    print(weekdayNames[now.weekday()], now.day, monthName[now.month], now.year)
    print('%d:%d:%d' %(now.hour, now.minute, now.second))


def operations():
    print('These are the available options')
    print('1. Withdrawal')
    print('2. Cash Deposit')
    print('3. Complaint')
    print('4. Account Details')
    print('5. Logout')

    selectedOption = int(input('Select an option\n'))

    if selectedOption == 1:
        withdrawal_amount = int(input('How much would you like to withdraw?\n'))
        current_balance = user_database[current_user]['balance']
        if withdrawal_amount > current_balance:
            print('Insufficient Fund')
        else:
            current_balance -= withdrawal_amount
            user_database[current_user]['balance'] = current_balance
            print('Take your cash')

    elif selectedOption == 2:
        deposit_amount = int(input('How much would you like to deposit?\n'))
        user_database[current_user]['balance'] += deposit_amount
        print('Your current balance is #%d' %user_database[current_user]['balance'])

    elif selectedOption == 3:
        complaint = input('What issue will you like to report?\n')
        print('Thank you for contacting us')
    
    elif selectedOption == 4:
        print('Account Details')
        print('Username: %s' %current_user)
        for key, value in user_database[current_user].items():
            if key == 'password':
                continue
            print('{}: {}'.format(key, value))

    elif selectedOption == 5:
        print('GoodBye %s' %current_user)
        exit()

    else:
        print('Invalid selection, please try again.')


def login():
    global current_user

    isLoginSuccessful = False
    while not isLoginSuccessful:
        username = input('Enter your username \n')
        password = input('Enter password for %s \n' %username)
        if(username in user_database and password == user_database[username]['password']):
            isLoginSuccessful = True
        else:
            print('Password or username incorrect. Please try again')
    current_user = username
    print('Welcome ' + username)
    displayDateTime()


def generateAccountNumber():
    global last_account_number

    zeroPadding = '0' * (10 - len(str(last_account_number)))
    accountNumber = zeroPadding + str(last_account_number + 1)
    last_account_number += 1
    return accountNumber


def register():
    isRegisterSuccessful = False
    while not isRegisterSuccessful:
        username = input('Enter your username \n')
        password = input('Enter your password \n')
        if(username not in user_database):
            user_database[username] = {
                'password': password,
                'balance': 10000,
                'accountNumber': generateAccountNumber()
            }
            print('Registration successfull. Please login with your credentials')
            isRegisterSuccessful = True
        else:
            print('%s not available. Pick a different username' %username)
    login()


def reset_password():
    username = input('Enter your username \n')
    try:
        user = user_database[username]
    except KeyError:
        print('No account found for user %s' %username)

    accountNumber = input('Enter account number for %s \n' %username)
    if(accountNumber == user['accountNumber']):
        resetSuccess = False
        while not resetSuccess:
            new_password = input('Enter new password \n')
            repeat_password = input('Enter new password again \n')

            if new_password == repeat_password:
                user_database[username]['password'] = new_password
                resetSuccess = True
            else:
                print('Passwords did not match. Please try again')
        print('Password reset successfully')
    else:
        print('Invalid account number for user %s' %username)


def atmMockApp():
    try:
        print('Welcome, what would you like to do?')
        print('1. Login')
        print('2. Register')
        print('3. Reset Password')
        print('4. Exit')

        selectedAction = int(input('Select an option \n'))

        if(selectedAction == 1):
            login()
            while True:
                print()
                operations()
                sleep(2)
        
        elif(selectedAction == 2):
            register()
            while True:
                print()
                operations()
                sleep(2)
        
        elif(selectedAction == 3):
            reset_password()
            sleep(1)
            print()
            atmMockApp()

        elif(selectedAction == 4):
            exit()

        else:
            print('Invalid selection. Please try again \n')
            atmMockApp()
    except Exception:
        print('Unexpected error occurred. Please try again \n')
        atmMockApp()


atmMockApp()