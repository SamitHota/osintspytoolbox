import instaloader
from colorama import Fore, Style
import os
import shutil
from datetime import datetime

# Provide the login credentials of your own account
primary_username = '' 
primary_password = ''


second_account_username = input("Enter the username of the Target account: ")
loader = instaloader.Instaloader()
loader.login(primary_username, primary_password)
loader.save_session_to_file(filename='instaloader.session')
profile = instaloader.Profile.from_username(loader.context, second_account_username)
followers = profile.get_followers()
following = profile.get_followees()

try:
    with open('previous_scan_data.txt', 'r') as file:
        previous_scan_data = file.read().splitlines()
except FileNotFoundError:
    previous_scan_data = []

new_followers = [follower.username for follower in followers if follower.username not in previous_scan_data]
print(Fore.GREEN + f"New followers of {second_account_username}:" + Style.RESET_ALL)
for follower in new_followers:
    print(follower)

new_following = [account.username for account in following if account.username not in previous_scan_data]
print(Fore.BLUE + f"New accounts followed by {second_account_username}:" + Style.RESET_ALL)
for account in new_following:
    print(account)

current_scan_data = [follower.username for follower in followers]
current_scan_data.extend([account.username for account in following])
with open('previous_scan_data.txt', 'w') as file:
    file.write('\n'.join(current_scan_data))

backup_dir = os.path.join('history', second_account_username)
os.makedirs(backup_dir, exist_ok=True)

backup_filename = datetime.now().strftime("%Y%m%d_%H%M%S") + '_scan_data.txt'
backup_filepath = os.path.join(backup_dir, backup_filename)
with open(backup_filepath, 'w') as file:
    file.write('\n'.join(current_scan_data))

print(f"Backup of scan data saved: {backup_filepath}")
