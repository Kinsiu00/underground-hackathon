class Scene:
    def __init__(self, desc, commands):
        self.desc = desc
        self.commands = commands

    def load_commands(self, commands):
        for i in self.commands:
            print(i)
A = Scene('you are in room A', ['i','s','e'])


#start trigger
if __name__ == '__main__':
    current_scene = A
    while current_scene == A:
        cmd = input(A.desc)
    #     cmd = test
    #     if cmd.lower() not in ['i']:
    #         print('sorry, I didn\'t get that')
    #     else:
    #         if cmd == 'i':
    #             for x in player.inv:
    #                 print(x)
    #         if cmd == 't':
    #             print(datetime.time())
    #         if cmd == 'g':