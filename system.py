from time import time

# system var and function object
class system:
    def __init__(self):
        # game's main loop is active while true
        self.running = True

        # time (in seconds) game last saved
        self.time = -1
        #   -1 = no time set (yet)

        # game's current language
        self.lang = 0
        #   0 = JPN
        #   1 = EN

        # current location in game
        self.loc = 0
        #   loc 0 = main menu
        #   loc 1 = start of game
        # menu selection
        self.menu_sel = 0
        #   menu sel 1 = start new game
        #   menu sel 2 = load game
        #   menu sel 3 = quit

        # current paragraph in block
        self.para = 0
        # max paragraph
        self.para_max = -1

    def update_time(self):
        self.time = time()

    # break's out of inner and outer loop
    def quit_game(self):
        self.running = False
        self.loc = -1

    # change current location and update system variables if required.
    def move(self, location):
        self.loc = location
        if location == 1: # start of game
            self.para = 0
            self.para_max = 1

    # switch to other language
    def lang_change(self):
        if self.lang == 0:
            self.lang = 1
        else:
            self.lang = 0

    def forward(self):
        if self.para < self.para_max:
            self.para += 1

    def back(self):
        if self.para > 0:
            self.para -= 1
