import inquirer
current_scene = {}

class Scene:
    def __init__(self, description, action, command_list):
        self.description = description
        self.action = action
        self.command_list = command_list
        self.scene = [
            inquirer.List('action',
                          message=self.action,
                          choices=self.command_list,
                          ),
        ]
        self.result = {}

# Different Scenes
penn_station = Scene('long ass description and stuff and things and more stuff and things and yes',
                     "You are standing in Penn Station",
                     ['Check MTA Schedule', 'eat a pizza', 'mike mike', 'go to time\'s square', 'jorge the great'])
times_square = Scene('there is a lot of billboards and people and a single naked cowboy',
                     "where to, adventurer?",
                     ['tip the cowboy', 'get lost in the crowd', 'check out the lego store', 'find true love', 'go to penn station'])

def start_scene(anything):
    print(anything.description)
    anything.result = inquirer.prompt(anything.scene)

def set_scene(anything):
    return anything.result

def set_description(anything, new_desc):
    anything.description = new_desc
    print(anything.description)
    anything.result = inquirer.prompt(anything.scene)

def switch_scenes(arg):
            switcher = {
                "go to time's square": start_scene(times_square),
                "go to penn station": start_scene(penn_station)
            }
            switcher.get(current_scene['action'])

if __name__ == '__main__':
    start_scene(penn_station)
    current_scene = set_scene(penn_station)

    while True:
        switch_scenes(current_scene['action'])