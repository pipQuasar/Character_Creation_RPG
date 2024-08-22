import time
from rich import print  # type: ignore
from rich.table import Table  # type: ignore
from rich.console import Console  # type: ignore

# Function to simulate a charging frame, with some delay in it.
def game_charging(text, velocity=0.1):
    console = Console()

    for word in text.split():
        for letter in word:
            console.print(letter, end='', highlight=False)  
            time.sleep(velocity)
        console.print("", end=' ', highlight=False)

# Function to show the game title.
def game_title():
    game_title = "\n\n¡Welcome to WORLD OF LORDS!"
    time.sleep(2.5), game_charging("Loading...", velocity=0.3)
    time.sleep(2), print("Ready!")
    time.sleep(1.25), print("Starting...")
    time.sleep(2), print("[bold red]" + game_title + "[/bold red]")

# Function to validate that the input option was valid
def select_validation(select):
    time.sleep(1.5)
    while (select != "1" and select != "2" and select != "3"):
        select = input("\nI don't understand that. Please select a valid option.\n\n[1: Log in]\t[2: Register]\t[3: Exit game]\n\n3\t\t[?]: ")
    return select









def Menu():
    print("\n\n[bold red]" + "MENU" + "[/bold red]")
    select = input("[1: Log in]\t[2: Register]\t[3: Exit game]\n\n\t\t[?]: ")
    if(select != "1" and select != "2" and select != "3"):
        select = select_validation(select)
    return select





# Function to Log in and start the game
from admin_account import admin     # Here's the admin account to log in.
def Login():
    logged = True
    attempts = 0
    print("[bold red]" + "LOG IN" + "[/bold red]")
    username, password = input("\n[Enter your username ->]: "), input("[Enter your password ->]: ")  
    while(username != admin._user or password != admin._password):
        attempts+=1
        if attempts >= 5:
            print("\nToo many attemps")
            logged = False 
            return logged
        username, password = input("\nERROR! username or password wrong.\n\n[Enter your username ->]: "), input("[Enter your password ->]: ")
    print("logging in...") 
    time.sleep(2) 
    return logged

def Login_Menu():
    select = input("What u want?, create new character, view characters, exit")

# Function to finish the loop and close the game.
def Exit_game():
    print("Shutting down...")
    time.sleep(1)
    return exit()    












def WORLD_OF_LORDS():
    game_title()
    while(True):
        # Player action
        player_select = Menu()
        
        # Log in
        if player_select == "1":
            if (Login() == True):
                print("logged!")
                while(True):
                    Login_Menu()
                    break
                    # Acá estaria el codigo del juego, porque seria otro bucle hasta que decida volver al menu
            else:
                print("Try again later")
                continue
            
        # Register
        
        
        # Exit game
        elif player_select == "3":
            Exit_game()
        
if __name__ == "__main__":
    WORLD_OF_LORDS()