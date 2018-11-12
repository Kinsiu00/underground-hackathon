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
        print(self.action_dictionary[key])

        for per_scene in self.scene_trigger:
            print(per_scene, " -- is what I'm listening for")
            print(key, " --  key")
            if key == 'Choose the blue martini':
                inventory.add('Golden Metrocard')
                print("--------------------------")
                dead_rabbit.command_list.remove(key)
            if key == 'Choose the red martini':
                dead_rabbit.command_list.remove(key)
            if key == 'take a ride on the wild side':
                questions = [
                inquirer.Text('answer', message="where are you trying to go?")
                ]
                answer = inquirer.prompt(questions)
                if answer['answer'] != 'dead rabbit':
                    print('where is that?')
                else:
                    print('off we go then')
                    set_scene(dead_rabbit)
                    start_scene(dead_rabbit)

            # print(per_scene, " -- per scene")
            # print(key, " --  key")
                
# Different Scenes
penn_station = Scene('long ass description and stuff and things and more stuff and things and yes',
                     "You are standing in Penn Station",
                     ['Check MTA Schedule', 'eat a pizza', 'mike mike', 'go to times square', 'check pocket', 'take a ride on the wild side'])

times_square = Scene('there is a lot of billboards and people and a single naked cowboy',
                     "where to, adventurer?",
                     ['tip the cowboy', 'get lost in the crowd', 'check out the lego store', 'find true love', 'go to penn station', 'go to dead rabbit', 'go to white rabbit tattoo'])

dead_rabbit = Scene('Dingy Bar Scene, with crowd of young hipsters',
                    "Loud cosy bar called Dead Rabbit",
                    ['Bribe the bartender', 'Whisper sweet nothings to them', 'Choose the blue martini',
                     'Choose the red martini', 'go to times square'])

rabbit_tattoo = Scene('The tattoo parlor is clean and neat, the walls are adorn with tattoo samples.\n A heavy-set man is busy concentrating on tattoo a face-down customer.', 'you are standing in the White Rabbit Tattoo Shop', ['talk to the man', 'get a tattoo', 'ask about hackathon', 'go to times square'])


penn_station_actions = Action({'Check MTA Schedule': 'late as usual',
                               'eat a pizza': 'yum but pricy',
                               'mike mike': 'mike mike mike',
                               'go to times square': 'off we go!',
                               'take a ride on the wild side':'puff the magic dragon',
                               'check pocket': '..nothing else'}, {'go to times square', 'puff the magic dragon'})

times_square_actions = Action({'tip the cowboy': 'There you go cowboy',
                               'get lost in the crowd': 'Oh Oh Trouble',
                               'check out the lego store': 'what a nice toy',
                               'find true love': 'Good luck with that!',
                               'go to penn station': "Now we getting somewhere",
                               'go to dead rabbit': 'Woah, it\'s dark here',
                               'go to white rabbit tattoo': 'tattoo time'}, {'go to penn station', 'go to dead rabbit', 'go to white rabbit tattoo'})

dead_rabbit_action = Action({'Bribe the bartender': "Bartender wants you to pay their loan",
                             'Whisper sweet nothings to them': "*Swish Whish Swish Whish*",
                             'Choose the blue martini': "There is a golden metrocard!",
                             'Choose the red martini': "Dude! Your better than this!!!",
                             'go to times square': "leaving so early?!"}, {'Choose the blue martini'})

rabbit_tattoo_action = Action({'talk to the man':'I am busy, come back later', 'get a tattoo':'this isn\'t something you should rush', 'ask about hackathon':'I don\'t know anything about that, we just do tattoos here', 'go to times square': 'you leave'},{'go to times square'})

scene_loader = {penn_station : penn_station_actions, times_square : times_square_actions, dead_rabbit : dead_rabbit_action, rabbit_tattoo: rabbit_tattoo_action}

scene_list = {'go to times square': times_square,
              'go to penn station': penn_station, 'go to dead rabbit': dead_rabbit}


#GLOBAL
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
    print('Welcome, placeholder starting message and description for why you are here and stuff\n')
    start_scene(current_scene)
    if current_scene.action['action'] == 'check pocket':
        print('Inside your pocket, you find:')
        for item in inventory:
            print(item)
    for key in current_action_set.action_dictionary:
        if current_scene.action['action'] == 'go to times square':
            set_scene(times_square)
            start_scene(current_scene)
        if current_scene.action['action'] == 'go to dead rabbit':
            set_scene(dead_rabbit)
            start_scene(current_scene)
        if current_scene.action['action'] == 'go to penn station':
            set_scene(penn_station)
            start_scene(current_scene)
        if current_scene.action['action'] == 'go to white rabbit tattoo':
            set_scene(rabbit_tattoo)
            start_scene(current_scene)
        if current_scene.action['action'] == 'Check MTA Schedule':
            os.system("python3 penn_station_scraper.py")
            start_scene(current_scene)
        elif current_scene.action['action'] == key:
            current_action_set.interaction(current_scene.action['action'])