from fdef import cpa
from curses import *

class pix:
    def __init__(self):
        self.img0 = [
            "7??????IIII7IIIIIIIIIII?+II=?+=?~7?IIIII=~77==+77I=I=IIII?II=III7777777777777777",
            "77?????IIII7I7IIIII+III=?I?:?I7I=77IIIIIII:+77:...=7=??II?III:II77777IIIIIII7777",
            "7777???IIIIII7IIIIIIIII=?=I~7777==777~IIIII?7~7=~~=.I=7=IIIII?=I=777IIIIIIIII777",
            "7777777I77IIIIIIIIIIIII+??I=77?=7==7777IIIII=I7?:::?.77I=IIII+7=I77IIIIIIIIIII77",
            "7777777?II?I7IIIIIII?II???7=I77?77=7777777III=,,,:: ?~7I=+I~I?7~=77IIIIIIIIIII77",
            "77777777IIIIII7IIIIIIII??77:...+?I7=77777777II:~,:,  77I==?=I=77=I7IIIIIIIIIII77",
            "77777???III+IIIIIIIII?I?77..~~~~ 777=7777777777.,,,7777I~~==I?77I+77IIIIIIIII777",
            "7777????=IIIII77I?III?I77.? I7::,7777777777777777777II77=:==II??7=77777III777777",
            "7777?????III+II7II=III:77.?.::::=.7777777777777777I7777?====I?=??+77777777777III",
            "77777????+IIIIII7II=III=7.?7.,=?=.7777777777I77777777777====I=I???777777777IIIII",
            "7777777777III=IIIIII=II=~+.   7,777777777777777777777777===+I=I???I777777IIIIIII",
            "7777777777+II==I?III+==I==77777777I777777777777777777777~==I===+???777777IIIIIII",
            "77777777777II==I+IIII===?==777IIIII777777777+=~,7777777====I=~=????77777IIIIIIII",
            "+++77777777?I===?=IIII===~==III777777777?=======7777777++==I7 I=I~======~==IIIII",
            "++++I777777=+===I=?III?===??==777777777:====+??==77777?=?==?777I=777777777+=IIII",
            "+++++7777777======~IIII+===???+77777777?==??????I7777????=I+77777=7777777777IIII",
            "+++++7777777=7======IIII+===??7?77777777~??????7777???7=?=I~======~=====~??7+III",
            "+++++7777777=7=======?III+====+,?7777777777?I77777+?+7777=~=777777777777~~===III",
            "+++?77777777=7========~III====++=??=7777777777777???777777I:==7777777777777 7III"
            ]

    def disp_image(self, win, image_no=0):
        if image_no == 0:
            line = 0
            while (line < 18):
                cpa(win, line, 0, self.img0[line])
                line += 1

    def clear_image(self, win):
        line = 0
        while (line < 18):
            cpa(win, line, 0, " "*80)
            line += 1
