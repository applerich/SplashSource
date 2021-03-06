import random
import requests
import selenium
import time
import threading
from dropconfig import *

# main menu


def menu():
    print('''
Pick one. 

    1. Load proxies
    2. Get captcha balance
    3. Quit
    ''')

    userChoice = input('Enter the action that you want to take: ')
    choices = {
    1: load_proxies,
    2: captcha_balance,
    3: quit
    }

    try:
        choices[int(userChoice)]()
    except:
        print('Input not recognized. You probably did not enter a number. \n'
              'The program will restart. \n')
        menu()
    finally:
        Continue()


# displays 2captcha balance
def captcha_balance():
    if captcha_api == '':
        print('No captcha token present. Check your config file.')
    else:
        balance = requests.get("http://2captcha.com/res.php?key={}&action=getbalance".format(captcha_api)).text
        print('\nYour 2captcha balance is {}.\n'.format(balance))

# function to load user proxies.
def load_proxies():
    try:
        with open('proxies.txt') as proxiesFile:
            proxies = proxiesFile.read().splitlines()
        print('{} proxies succesfully loaded.'.format(len(proxies)))
    except IOError:
        print('Error importing proxy file.')
        exit()

# asks the user about continuing
def Continue():
    # asks the user if they want to keep calculating, converts to lower case
    keep_going = input('Do you want to keep going? Enter yes or no. \n'
                       '').lower()
    # evaluates user's response.
    if keep_going == 'yes':
        menu()
    elif keep_going == 'no':
        print('\nThanks for using the SplashForce!')
        quit()
    else:
        print('\nInput not recognized. Try again.')

# run the code
if __name__ == "__main__":
    print('Please read the readme on Github before using this bot.')
    menu()
