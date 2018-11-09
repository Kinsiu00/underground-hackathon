import inquirer

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
            print(per_scene, " -- per scene")
            print(key, " --  key")
        
        if key == per_scene:
            start_scene(scene_list[key])

# Different Scenes
penn_station = Scene('long ass description and stuff and things and more stuff and things and yes',
                     "You are standing in Penn Station",
                     ['Check MTA Schedule', 'eat a pizza', 'mike mike', 'go to time\'s square', 'jorge the great'])

times_square = Scene('there is a lot of billboards and people and a single naked cowboy',
                     "where to, adventurer?",
                     ['tip the cowboy', 'get lost in the crowd', 'check out the lego store', 'find true love', 'go to penn station', 'go to dead rabbit'])

dead_rabbit = Scene('Dingy Bar Scene, with crowd of young hipsters',
                    "Loud cosy bar called Dead Rabbit",
                    ['Bribe the bartender', 'Whisper sweet nothings to them', 'Choose the blue martini',
                     'Choose the red martini', 'got to time\'s square'])

penn_station_actions = Action({'Check MTA Schedule': 'late as usual',
                               'eat a pizza': 'yum but pricy',
                               'mike mike': 'mike mike mike',
                               'go to time\'s square': 'off we go!',
                               'jorge the great': 'is gone'}, {'go to time\'s square'})

times_square_actions = Action({'tip the cowboy': 'There you go cowboy',
                               'get lost in the crowd': 'Oh Oh Trouble',
                               'check out the lego store': 'what a nice toy',
                               'find true love': 'Good luck with that!',
                               'go to penn station': "Now we getting somewhere",
                               'go to dead rabbit': 'Woah, it\'s dark here'}, {'go to penn station', 'go to dead rabbit'})

dead_rabbit_action = Action({'Bribe the bartender': "Bartender wants you to pay their loan",
                             'Whisper sweet nothings to them': "*Swish Whish Swish Whish*",
                             'Choose the blue martini': "There is a golden metrocard!",
                             'Choose the red martini': "Dude! Your better than this!!!",
                             'got to time\'s square': "leaving so early?!"}, {'go to time\'s square'})


scene_list = {'go to time\'s square': times_square,
              'go to penn station': penn_station, 'go to dead rabbit': dead_rabbit}
current_scene = penn_station


def start_scene(element=penn_station):
    print(element.description)
    element.action = inquirer.prompt(element.scene)


def set_description(element, new_desc):
    element.description = new_desc


# GAME START
while __name__ == '__main__':
    start_scene()

    for key in penn_station_actions.action_dictionary:
        if current_scene.action['action'] == key:
            penn_station_actions.interaction(key)
