import os


def banner():
    os.system("clear")
    banner = r"""
 ________  ________  _________  ________     
|\   __  \|\   ____\|\___   ___\\   __  \    
\ \  \|\  \ \  \___|\|___ \  \_\ \  \|\ /_   
 \ \  \\\  \ \_____  \   \ \  \ \ \   __  \  
  \ \  \\\  \|____|\  \   \ \  \ \ \  \|\  \ 
   \ \_______\____\_\  \   \ \__\ \ \_______\
    \|_______|\_________\   \|__|  \|_______|
             \|_________|                    
                                             
    """
    toolbox = """
    OSINT Spy Tool Box   ||  Ver. 1.0 Beta
    """
    social_media = """
    Follow Me:
    - Instagram: https://instagram.com/HotaSamit
    - YouTube: https://youtube.com/c/SamitHota
    - Github: https://github.com/SamitHota
    """
    banner_lines = banner.split('\n')
    toolbox_lines = toolbox.split('\n')
    social_media_lines = social_media.split('\n')

    # Define color codes
    colors = {
        "header": "\033[1;35m",  # Purple text
        "reset": "\033[0m",      # Reset to default color
        "toolbox": "\033[1;36m",  # Cyan text
        "social_media": "\033[1;32m",  # Green text
    }

    # Print the banner with colors
    for line in banner_lines:
        print(colors["header"] + line + colors["reset"])

    print()  # Add an empty line
    for line in toolbox_lines:
        print(colors["toolbox"] + line + colors["reset"])

    print()  # Add an empty line
    for line in social_media_lines:
        print(colors["social_media"] + line + colors["reset"])

# Call the colorful_banner function to display the banner
banner()


#banner end

programs = {
    "1": ("Camera Spy", "cd camnull && bash camnull.sh"),
    "2": ("Location Spy", "cd locnull && python3 locnull.py"),
    "3": ("Instagram Spy", "cd spy && python3 ig.py"),
    "4": ("Facebook Spy", "cd spy && python3 fb.py"),
    "5": ("Location Info", "cd spy && python3 geo.py"),
    "6": ("Exit", None)
}


def display_menu():
    print("===== Home Page =====")
    for key, (name, _) in programs.items():
        print(f"{key}: {name}")
    print("=====================")


def run_program(command):
    if command:
        os.system(command)
    else:
        print("Exiting the home page.")


while True:
    display_menu()
    choice = input("Select a program by entering its number: ")

    if choice in programs:
        program_name, program_command = programs[choice]
        print(f"Opening {program_name}...")
        run_program(program_command)
        if choice == "6": 
            break 
    else:
        print("Invalid choice. Please select a valid option.")
