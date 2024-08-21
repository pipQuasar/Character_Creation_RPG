import csv
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
    time.sleep(2.5), game_charging("Charging...", velocity=0.3)
    time.sleep(2), print("Ready!")
    time.sleep(1.25), print("Starting...")
    time.sleep(2), print("[on black][bold red]" + game_title + "[/bold red][/on black]")

# Function to validate that the input option was valid
def select_validation(select):
    while (select != "1" and select != "2" and select != "3"):
        select = input("\nI don't understand that. Please select a valid option.\n\n[1: Log in]\n[2: Register]\n[3: Exit game]\n:")
    return select

# Function to finish the loop and close the game.
def exit_game(select):
    if select == "3":
        print("Shutting down...")
        time.sleep(1)
        return exit()

def game_menu():
    select = input("[1: Log in]\n[2: Register]\n[3: Exit game]\n:")
    if(select != "1" and select != "2" and select != "3"):
        select = select_validation(select)

    if select == "3":
        exit_game(select)
    
    





def WORLD_OF_LORDS():
    game_title()
    while(True):
        game_menu()
        
if __name__ == "__main__":
    WORLD_OF_LORDS()