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
        if key == self.scene_trigger:
            print('scene change!')



# Different Scenes
penn_station = Scene('long ass description and stuff and things and more stuff and things and yes',
"You are standing in Penn Station",
['Check MTA Schedule', 'eat a pizza', 'mike mike', 'go to time\'s square', 'jorge the great'])

times_square = Scene('there is a lot of billboards and people and a single naked cowboy',
"where to, adventurer?",
['tip the cowboy', 'get lost in the crowd', 'check out the lego store', 'find true love', 'go to penn station'])

penn_station_actions = Action({'Check MTA Schedule':'late as usual', 'eat a pizza':'yum but pricy', 'mike mike':'mike mike mike', 'go to time\'s square':'off we go!', 'jorge the great':'is gone'}, 'go to time\'s square')

def start_scene(element = penn_station):
    print(element.description)
    element.action = inquirer.prompt(element.scene)

def set_description(element, new_desc):
    element.description = new_desc

#GAME START
while __name__ == '__main__':
    current_scene = penn_station
    start_scene()

    for key in penn_station_actions.action_dictionary:
        if current_scene.action['action'] == key:
            penn_station_actions.interaction(key)
    if current_scene.action['action'] == 'go to penn station':
        start_scene(penn_station)