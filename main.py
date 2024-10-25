# Joshua Phillips
# 10/23/24
# Fortune Teller Project.

# Setup
import random
import sys
import time

fortunes = ['You are a winner!', 'A secret admirer will soon send you a sign of effection!', 'The one you love is closer than you think!', 'Good things will happen to you by the end of the day today!', 'Fame and fortune will be yours if you take the time to learn Python!', 'I\'m just a computer program, and have to magical powers!', '...', 'Buy a lottery ticket!', 'Have you ever heard of Tezcatlipoca and Quetzalcoatl?', '']
magic_colors = ['blue', 'red', 'green', 'yellow']

# Greetings
name = input('Please enter your first name: ')
username = name.title()
print(f'Welcome to my Python Fortune Teller program, {username}!')
# I
question1 = input('Would you like your fortune told? ')
question1.lower()
time.sleep(2)
# P
if question1 in ['y', 'yes', 'yes please', 'sure']:
    time.sleep(1)
    print('Okay! to get fortune, please input a magic color(blue, green, red or yellow)')
    color = input('color: ')
    color.lower()
# O
    time.sleep(1)
    print('Getting your fortune...')
    time.sleep(2)
    print(f'Here is your fortune, {username}:')
    time.sleep(1)

    if color in magic_colors:
        index = random.randint(0, len(fortunes)-1)
        print(fortunes[index])
    else:
        print('Please enter a magic color of either: blue, red, green or yellow.')
        time.sleep(1)
        print('Once you have entered a magic color, I will reveal yor fortune!')

else:
    print(f'Thank you for playing my Fortune Telling game today, {username}!')
    print('Goodbye!')
    sys.exit()

print(f'Thank you for playing my Fortune Telling game today, {username}!')
print('Goodbye!')