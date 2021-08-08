from database import *
import pyperclip
pwd='krishiv1324'

def create_account():
    username_ = input('Enter your username or email:')
    website = input('Enter your website name:')
    url = input('Enter your login page url:')
    password = get_random_string(8)
    add_account(username=username_, password=password, website=website, url=url)
    print(f'Your password is in your clipboard')
    pyperclip.copy(password)


def main():
    quitting=False
    if input('Enter the master password')!=pwd:
        quitting=True
    while not quitting:
        print('''1. Add a new account\n
        2. Get password from an existing website
        3. Quit''')
        answer=input('')
        if answer=='3':
            quitting=True
        elif answer=='1':
            create_account()
        elif answer=='2':
            website=input('enter the website name')
            print(get_password(website))
        else:
            print('Invalid input')

    con.commit()
    con.close()
if __name__ == '__main__':
    main()