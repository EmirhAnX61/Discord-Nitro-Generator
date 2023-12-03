import random
import string
import time
from colorama import Fore
import pyfiglet
import os

gift = "http://discord.gift/"

text = pyfiglet.figlet_format("Nitro Gen")

print(Fore.BLUE + text)




def generate_random_chars():
    all_chars = string.ascii_letters + string.digits
    random_chars = random.sample(all_chars, 22)
    result = ''.join(random_chars)
    return result

def save_to_txt(data, filename):
    with open(filename, 'a') as file:
        file.write(data + '\n')



while True:
    
    random_characters = generate_random_chars()

    
    print(gift+random_characters)

    
    save_to_txt(gift+random_characters, 'output.txt')

       
    time.sleep(0.3)





