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


# Different Scenes
penn_station = Scene('long ass description and stuff and things and more stuff and things and yes',
"You are standing in Penn Station",
['Check MTA Schedule', 'eat a pizza', 'mike mike', 'go to time\'s square', 'jorge the great'])

times_square = Scene('there is a lot of billboards and people and a single naked cowboy',
"where to, adventurer?",
['tip the cowboy', 'get lost in the crowd', 'check out the lego store', 'find true love', 'go to penn station'])


def start_scene(element):
    print(element.description)
    element.action = inquirer.prompt(element.scene)

def set_description(element, new_desc):
    element.description = new_desc
    # print(anything.description)
    # anything.result = inquirer.prompt(anything.scene)


def switch_scenes(arg):
    switcher = {
        "go to time's square": start_scene(times_square),
        "go to penn station": start_scene(penn_station)
    }
    switcher.get(arg)

#GAME START
if __name__ == '__main__':
    print(current_scene.action)
    start_scene(current_scene)
    while True:
        switch_scenes(current_scene['action'])