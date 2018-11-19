import inquirer
import os
# import requests

# SCENE = SELF, DESCRIPTION, MESSAGE, COMMAND_LIST, SCENE (INQ OBJ), ACTION {'action': whatever}


class Scene:
    def __init__(self, description, message, command_list):
        self.description = description
        self.message = message
        self.command_list = command_list
        self.scene = [
            inquirer.List('action',
                          message=self.message,
                          choices=self.command_list,
                          ),
        ]
        self.action = {}


class Action:
    def __init__(self, action_dictionary, scene_trigger):
        self.action_dictionary = action_dictionary
        self.scene_trigger = scene_trigger

    def interaction(self, key):
        print("\n\n")
        print(self.action_dictionary[key])
        print("----------------------------------------------------")
        for per_scene in self.scene_trigger:
            # print(per_scene, " -- is what I'm listening for")
            # print(key, " --  key")
            if key == 'Look for the White Rabbit':
                times_square.command_list.add('Enter White Rabbit Intimates')
                times_square.command_list.add(
                    'Go to the White Rabbit Tattoo Parlor')

            if key == 'Order the Blue cocktail':
                
                inventory.add('Golden Metrocard')
                dead_rabbit.command_list.remove(key)
            if key == 'Order the Red cocktail':
                dead_rabbit.command_list.remove(key)
            if key == 'Hail a cab':
                dead_taxi = [
                    inquirer.Text(
                        'answer', message="Enter the address of the location")
                ]
                answer = inquirer.prompt(dead_taxi)
                if answer['answer'] != '30 waters st':
                    print('where is that?')
                else:
                    print('off we go then')
                    set_scene(dead_rabbit)
                    start_scene(dead_rabbit)
                    times_square.command_list.add('Go to Dead Rabbit Bar')

            # print(per_scene, " -- per scene")
            # print(key, " --  key")

# Different Scenes
penn_station = Scene(
    'You are in the heart of New York City\'s transit system - Penn Station.\nAround you is a sea of people too busy going about their daily routines to notice you.\nThe monitors change rapidly to reflect the hundreds of trains coming into and out of the city.',
    "You are standing in Penn Station",
    ['Glance at the MTA Schedule',
     'Grab a bite to eat',
     'Wander the station',
     'Head to Times Square',
     'Hail a cab',
     'Check your pocket'])

times_square = Scene(
    'Before you is the heart of New York City - massive, bright displays and billboards surround you,\nselling you the answer to all of life\'s problems. The din of the city is overwelming here.\nYou notice a (mostly) naked cowboy strumming a guitar, as well as an odd, solitary poster on a wall.',
    "You are standing at the center of the world",
    {'Check out the Naked Cowboy.',
     'Look for the White Rabbit',
     'Read Poster',
     'Go to Penn Station',
     'Check your pocket'})

dead_rabbit = Scene(
    'The Dead Rabbit is a slick and modern bar, with the proper ambiance for a good first impression,\nromantic or otherwise. It is currently not busy, the bartender is idily wiping down a glass,\nyou can almost make out a faint humming slip through her lips.',
    "Music is playing faintly",
    ['Chat with the Bartender',
     'Ask about White Rabbit',
     'Order the Blue cocktail',
     'Order the Red cocktail',
     'Head to Times Square',
     'Check your pocket'])

rabbit_tattoo = Scene(
    'The tattoo parlor is clean and neat, the walls are adorn with tattoo samples.\nA heavy-set man is busy concentrating on tattooing a face-down customer.',
    'A tattoo gun buzzes softly in the background',
    ['Ask about White Rabbit',
     'Get a Tattoo',
     'Ask about Underground Hackathon',
     'Head to Times Square',
     'Check your pocket'])


penn_station_actions = Action({
    'Glance at the MTA Schedule': 'you see:',
    'Grab a bite to eat': 'you are not sure if it is the prices, but you do not feel particularly hungry.',
    'Wander the station': 'You wander about, getting lost in the faces of the crowd.\nYou experience a profound sense of sonder.',
    'Head to Times Square': 'You head towards Times Square..',
    'Hail a cab': 'puff the magic dragon',
    'Check your pocket': '..nothing else'
},
    {'Head to Times Square',
     'puff the magic dragon'})

times_square_actions = Action({
    'Check out the Naked Cowboy.': 'He continues to strum his guitar and gives you a wink.',
    'Look for the White Rabbit': 'You search high and low, but the only things you find are a lingerie store and a tattoo parlor.',
    'Enter White Rabbit Intimates': 'Sorry, not available in this version.',
    'Read Poster': 'It is an advert for a bar called "Dead Rabbit", unfortunately, the address is worn and not legible.\nMaybe you can look it up somehow?',
    'Go to Penn Station': "You head into Penn Station",
    'Go to Dead Rabbit Bar': 'You head to Dead Rabbit',
    'Go to the White Rabbit Tattoo Parlor': 'You head for the Tattoo Parlor',
    'Check your pocket': '..nothing else'
},
    {'Look for the White Rabbit',
     'Go to Penn Station',
     'Go to Dead Rabbit Bar',
     'Go to the White Rabbit Tattoo Parlor'})

dead_rabbit_action = Action({
    'Chat with the Bartender': "'There's a rumor of a secret metro station at 9 and 3/16th st, whatever that means.', she confides.",
    'Ask about White Rabbit': "'Have a drink', she winks",
    'Order the Blue cocktail': "You drink it down, it tastes of blueberries and sunshine. It isn\'t until you finish that you notice something under the coaster.\nYou've obtained a Golden Metrocard!",
    'Order the Red cocktail': "You drink it down, it is tastes of strawberries and summer days.",
    'Head to Times Square': "You head back to Times Square",
    'Check your pocket': '..nothing else'},
    {'Order the Blue cocktail'})

rabbit_tattoo_action = Action({
    'Ask about White Rabbit': '"I don\'t know anything about that", the man states flately, never taking his eyes away from his work.\n"Try asking at that something Rabbit Bar, a cab should be able to take you."',
    'Get a Tattoo': '"Sorry, all booked up, come back tomorrow.", the man says.',
    'Ask about Underground Hackathon': '"What is that? Look buddy, we just do tattoos here"',
    'Head to Times Square': 'you leave',
    'Check your pocket': '..nothing else'},
    {'Head to Times Square'})

scene_loader = {
    penn_station: penn_station_actions,
    times_square: times_square_actions,
    dead_rabbit: dead_rabbit_action,
    rabbit_tattoo: rabbit_tattoo_action
}

scene_list = {
    'Head to Times Square': times_square,
    'Go to Penn Station': penn_station,
    'Go to Dead Rabbit Bar': dead_rabbit
}


# GLOBAL
current_scene = penn_station
current_action_set = penn_station_actions
inventory = {'pocket lint'}


def set_scene(loadee):
    global current_scene
    current_scene = loadee
    global current_action_set
    current_action_set = scene_loader[loadee]


def start_scene(element):
    print(current_scene.description)
    current_scene.action = inquirer.prompt(current_scene.scene)


# GAME START
# set_scene(penn_station)
while __name__ == '__main__':
    print("----------------------------------------------------")
    # print('\n')
    start_scene(current_scene)
    if current_scene.action['action'] == 'Check your pocket':
        print('Inside your pocket, you find:')
        for item in inventory:
            print(item)
    for key in current_action_set.action_dictionary:
        if current_scene.action['action'] == key:
            current_action_set.interaction(current_scene.action['action'])
    if current_scene.action['action'] == 'Head to Times Square':
        set_scene(times_square)
        start_scene(current_scene)
    if current_scene.action['action'] == 'Go to Dead Rabbit Bar':
        set_scene(dead_rabbit)
        start_scene(current_scene)
    if current_scene.action['action'] == 'Go to Penn Station':
        set_scene(penn_station)
        start_scene(current_scene)
    if current_scene.action['action'] == 'Go to the White Rabbit Tattoo Parlor':
        set_scene(rabbit_tattoo)
        start_scene(current_scene)
    if current_scene.action['action'] == 'Glance at the MTA Schedule':
        os.system("python3 penn_station_scraper.py")
        start_scene(current_scene)