from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
from colorama import Fore, Style, init
import os
import pickle
import argparse


init()

def login_and_track(username, email, password):
   
    folder_path = 'friend_list_data'
    os.makedirs(folder_path, exist_ok=True)

    # Initialize a web driver (e.g., Chrome)
    driver = webdriver.Chrome(executable_path='/path/to/chromedriver')

    try:
       
        session_file = os.path.join(folder_path, f'session_{username}.pkl')
        if os.path.exists(session_file):
          
            with open(session_file, 'rb') as f:
                session_data = pickle.load(f)
            driver.get('https://www.facebook.com')
            for cookie in session_data:
                driver.add_cookie(cookie)
            driver.refresh()

        else:
           
            driver.get('https://www.facebook.com')
            driver.find_element_by_name('email').send_keys(email)
            driver.find_element_by_name('pass').send_keys(password)
            driver.find_element_by_name('login').click()
            with open(session_file, 'wb') as f:
                pickle.dump(driver.get_cookies(), f)

        driver.get(f'https://www.facebook.com/{username}/friends')

        body = driver.find_element_by_tag_name('body')
        for _ in range(10):  # Adjust the number of scrolls as needed
            body.send_keys(Keys.END)

        friend_list_html = driver.page_source

        soup = BeautifulSoup(friend_list_html, 'html.parser')

        with open(os.path.join(folder_path, f'friend_list_{username}.html'), 'w', encoding='utf-8') as f:
            f.write(str(soup))

        print(Fore.GREEN + "Friend list updated successfully!")
        print(Style.RESET_ALL)

    finally:
        driver.quit()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Track changes in a Facebook friend list")
    parser.add_argument("-u", "--username", help="Facebook profile username", required=False)
    args = parser.parse_args()

    if args.username:
        username = args.username
    else:
        username = input("Enter your Facebook profile username: ")
        
        #Enter your own facebook account login credentials here
    email = 'your_email@example.com'
    password = 'your_password'

    login_and_track(username, email, password)
