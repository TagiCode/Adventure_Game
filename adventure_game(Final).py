import time
import random
import string


def print_pause(message, delay=1):
    typewriter_simulator(message)
    time.sleep(delay)


def typewriter_simulator(message):
    for char in message:
        print(char, end='')
        if char in string.punctuation:
            time.sleep(.5)
        time.sleep(.03)
    print('')


def valid_input(prompt, options):
    while True:
        option = input(prompt).lower()
        if option in options:
            return option
        print_pause(f'Sorry, the option "{option}" is invalid. Try again!')


def intro(Beast, weapon):
    messages = ['You find yourself standing in an open field \n',
                'filled with grass and yellow wildflowers.\n'
                'Rumor has it that a ', Beast, '\n'
                'fairie is somewhere around here,\n'
                'and has been terrifying the nearby village.\n'
                'In front of you is a house\n'
                'To your right is a dark cave\n'
                'In your hand you hold your trusty,\n'
                '(but not very efective) dagger']
    print_pause(messages, delay=1)


def field(Beast, weapon):
    while True:
        print_pause(['Enter 1 to knock on the door of house'])
        print_pause(['Enter 2 to peer into cave'])
        house_or_cave = valid_input("please enter 1 or 2 ", ['1', '2'])
        if house_or_cave == '1':
            house(Beast, weapon)
        elif house_or_cave == '2':
            cave(Beast, weapon)


def house(Beast, weapon):  # fight or run to field
    messages = ['You approach the door of the house\n'
                'You are about to knock when the door opens,\n'
                'and out steps a ', Beast, '\n'
                'Eep! This the ', Beast, 's house!']
    print_pause(messages, delay=1)
    fight(Beast, weapon)


def cave(Beast, weapon):  # dagger
    weapon = []
    print_pause(['You peer cautiosly into the cave'])
    if weapon == []:
        messages = ['It turns out to be only very small cave.\n'
                    'Your eye catches a glint of metal behind a rock.\n'
                    'You have found a magical Sword of Ogoroth!\n'
                    'You discad your silly old dagger and\n'
                    'take the sword with you\n'
                    'You walk back out to the field\n']
        print_pause(messages, delay=1)
        weapon.append('Ogoroth')
        field(Beast, weapon)
    else:
        messages = ['You have been here before,\n'
                    'and gotten all the good stuff.\n'
                    'It is just an empty cave now.\n'
                    'you walk back out to the field.']
        print_pause(messages, delay=1)
        field(Beast, weapon)  # main


def fight(Beast, weapon):  # fight
    print_pause(['The ', Beast, 'attacks you'])
    if weapon != []:
        fight_run = valid_input("Would you like to fight(1) or\n"
                                "run away(2)?", ['1', '2'])
        if fight_run == '1':  # fight with new sword
            messages = ['As the ', Beast, 'moves to attack,\n'
                        'you unsheath your new sword.'
                        'The Sword of Oporoth shine brightly in your had,\n'
                        'as you brace yourself for attack.\n'
                        'But the ', Beast, ' takes the look,\n'
                        'at your shiny new toy and runs away!\n'
                        'you have rid the town of the ', Beast, '.\n'
                        'You are victorious!']
            print_pause(messages, delay=1)
            play_again(Beast, weapon)  # paly again or not
        else:
            print_pause(['You run back into the field. Luckily,\n'
                         'you do not seem to have been followed'])
            field(Beast, weapon)   # main
    else:
        print_pause(['You feel a bit unde-prepared for this,\n'
                    'with only having a tiny dagger'])
        fight_run = valid_input("Would you like to fight(1) or\n"
                                "run away(2)?", ['1', '2'])
        if fight_run == '1':  # fight
            messages = ['You do your best ...\n'
                        'but your dagger is no match for ', Beast, '\n'
                        'You have been defeated!']
            print_pause(messages, delay=1)
            play_again(Beast, weapon)  # play again or not
        elif fight_run == '2':  # run
            print_pause(['You run back into the field. Luckily,\n'
                         'you do not seem to have been followed'])
            field(Beast, weapon)  # main


def play_again(Beast, weapon):
    while True:
        choice = valid_input("Would you like to play again? (y/n)", ['y', 'n'])
        if choice == "y":
            print_pause("\nExcellent! Restarting the game ...\n")
            play_game(Beast, weapon)
        elif choice == "n":
            print_pause("\nThanks for playing! See you next time.\n")
            exit(0)


def play_game(Beast, weapon):
    while True:
        Beast = random.choice(["wicked fairie", "pirate",
                               "dragon", "troll", "gorgon"])
        intro(Beast, weapon)
        field(Beast, weapon)


play_game('Beast', 'weapon')
