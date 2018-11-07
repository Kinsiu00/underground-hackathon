import datetime

class Character:
    def __init__(self, name, inv):
        self.name = name
        self.inv = inv
    
    def attack(self, target):
        target.hp = target.hp - self.attack
    
    def check_inv(self):
        for i in self.inv:
            print(i)

if __name__ == '__main__':
    player_name = input('please enter your name, player ')
    player = Character(player_name, ["pocket lint", "expired metro card"])
    running = True
    while running:
        test = input('you awaken in on a bench, your head is pounding and there is the smell of vomit.\nYou are on a bench at the 28th Ave Subway station\n[i]nventory\n')
        cmd = test
        if cmd.lower() not in ['i']:
            print('sorry, I didn\'t get that')
        else:
            if cmd == 'i':
                for x in player.inv:
                    print(x)
            if cmd == 't':
                print(datetime.time())
                
