
# Programmer:  Caitlin Burns
# Course:  CS151, Professor Zee
# Due Date: 10/9/2024
# PA: 1
# Problem Statement: this program designs an adventure video game
# Data In: character choice, world choice, rest or search, chest 1 or 2
# Data Out:  map pieces collected
# Credits: This code is based on the assignment given in the read me file

#this code creates an adventure game with choices for the user to make in order to complete the game

name = input("What is your name? ")
print("Hello " + name)

#this sets the number of map pieces the user will need to find
map_pieces = input('Enter a number between 5 and 10: ')
map_pieces = int(map_pieces)
if map_pieces >= 5 and map_pieces <= 10:
    print('You need to find', map_pieces ,'pieces of the map')
else:
    print('Invalid input')

#this sets the length of the journey
journey_length = input('Enter a number between 1.0 and 10.0: ')
journey_length = float(journey_length)
short = journey_length > 1.0 and journey_length < 5.0
long = journey_length > 5.0 and journey_length < 10.0
if journey_length > 1.0 and journey_length < 5.0:
    journey_length = short
    print('You will have 4 days to find all pieces of the map')
elif journey_length > 5.0 and journey_length < 10.0:
    journey_length = long
    print('You will have 8 days to find all the pieces of the map')

#this allows user to select a character and a pet
character_choice = input('Would you like to be a pirate or a fairy? ')

if character_choice == 'pirate':
    if journey_length == long:
        pet_choice = 'Parrot'
    elif journey_length == short:
        pet_choice = 'Cat'
    else:
        pet_choice = 'unknown animal'
elif character_choice == 'fairy':
    if journey_length == long:
        pet_choice = 'Dog'
    elif journey_length == short:
        pet_choice = 'Mouse'
    else:
        pet_choice = 'unknown animal'
print(name,'your character is a', character_choice , 'and your pet is a', pet_choice)

#this determines world choice
world_choice = input('Enter a number between 1 and 9: ')
world_choice = int(world_choice)
if world_choice >= 1 and world_choice <= 3:
    print('Your world is enchanted forest')
    map_pieces_collected = '0'
elif world_choice >= 4 and world_choice <= 6:
    print('Your world is pirate beach')
    map_pieces_collected = '0'
elif world_choice >= 7 and world_choice <= 9:
    print('Your world is fairy castle.')
    chest_choice = input('You found two chests. select one. Option 1 or option 2? ')
    if chest_choice == '1':
        print('Wrong choice! You get nothing')
        map_pieces_collected = '0'
    elif chest_choice == '2':
        print('Lucky you! You get two map pieces')
        map_pieces_collected = '2'
    else:
        print('Invalid choice. Select between 1 and 2')

#This will determine whether the user can rest or keep searching depending on journey length and map pieces
map_pieces_collected = int(map_pieces_collected)
if map_pieces_collected <2 or journey_length == 'short':
    choice = input('Would you like to continue searching? ')
    if choice == 'yes':
        print('You have found one map piece!')
        map_pieces_collected = map_pieces_collected + 1
        print('You have collected' , map_pieces_collected , 'total pieces!')
        print(name, ', You have searched enough for today. You should rest now')
    elif choice == 'no':
        print('You should rest')
else:
    print(name, ', you cannot continue searching. You should rest')

#this lets the user continue their search for map pieces
print(name, '! In your travels you have found two more pieces of the map!')
map_pieces_collected = map_pieces_collected + 2
map_storage = input('Do you want to store the map in your backpack, or in your pocket? ')
if map_storage == 'pocket':
    print('Oh no! One of your map pieces fell out of your pocket. Now you have', map_pieces_collected - 1 , 'pieces')
else:
    print('You now have', map_pieces_collected , 'pieces')

#this allows user to select between two treasure chests for map pieces
chest_choice_two = input('You have come across two treasure chests. Select one. Option 1 or option 2? ')
if chest_choice_two == '1':
    print('Lucky you! You get two map pieces!')
    map_pieces_collected = map_pieces_collected + 2
elif chest_choice_two == '2':
    print('Wrong choice! You get nothing')
else:
    print('Invalid choice. Select between 1 and 2')

#this asks the user if they want to rest or continue searching for map pieces
if map_pieces_collected <= 4 or journey_length == 'short':
    second_choice = input('Would you like to continue searching? ')
    if second_choice == 'yes':
        print('You have found two map pieces!')
        map_pieces_collected = map_pieces_collected + 2
        print('You have collected' , map_pieces_collected , 'total pieces!')
        print(name, ', You have searched enough for today. You should rest')
    elif second_choice == 'no':
        print('You have', map_pieces_collected, 'pieces.', 'You should rest')
else:
    print(name, 'You have',map_pieces_collected, 'pieces.' ,'You cannot continue searching. You should rest')

#This ends the game
if not map_pieces_collected < map_pieces:
    print('You have completed the game!')
else:
    print('Game over!')







