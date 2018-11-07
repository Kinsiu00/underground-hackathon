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

penn_station = Scene('long ass descriptoin and stuff and things and more stuff and things and yes',
"You are standing in Penn Station", ['Check MTA Schedule','eat a pizza','mike mike','charlie brown','turd nugget','jorge the great'])
def start_scene(anything):
    print(anything.description)
    anything.result = inquirer.prompt(anything.scene)

def set_scene(anything):
    return anything.result
#start trigger

# start(penn_station.scene)
if __name__ == '__main__':
    print(current_scene)
    start_scene(penn_station)
    current_scene = set_scene(penn_station)
    print(current_scene)