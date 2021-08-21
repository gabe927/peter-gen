################
#              #
# Import Block #
#              #
################

import sys
import random
import getopt
from types import resolve_bases
from datetime import date
########
#      #
# Main #
#      #
########

class peter_gen:
    def __init__(self):
        self.import_nouns()
        self.import_verbs()
    
    def import_nouns(self, filePath="nouns.txt"):
        with open(filePath) as f:
            self.nouns = f.read().splitlines()

    def import_verbs(self, filePath="verbs.txt"):
        with open(filePath) as f:
            self.verbs = f.read().splitlines()

    def get_new_combo(self, reverse=False):
        if not reverse:
            verb = random.choice(self.verbs)
            noun = random.choice(self.nouns)
        else:
            verb = random.choice(self.nouns)
            noun = random.choice(self.verbs)
        
        return verb, noun

    def get_new_string(self, reverse=False):
        verb, noun = self.get_new_combo(reverse=reverse)
        return f"I'll {verb} your {noun} ;)"

if __name__ == "__main__":
    # initial variables
    reverse = False
    flip = False
    pg = peter_gen()

    # open/create save file to append
    file = open("bestof.txt", "a+")
    # arguments
    # -r: reverse verb and noun
    # -f: flip entire phrase
    # -c: clear save file
    try:
        opts, arg = getopt.getopt(sys.argv[1:], "rfc",[])
    except getopt.GetoptError:
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-r':
            reverse = True
        elif opt == '-f':
            flip = True
        elif opt == '-c':
            file = open("bestof.txt", "w+")

    # cli loop
    while True:
        phrase = pg.get_new_string(reverse=reverse)
        if flip:
            phrase = phrase[::-1]
        try:
            flag = str(input(f"{phrase} "))
            # check for flip -f
            if flag == '-f':
                print(phrase[::-1])
            # check for save -s
            elif flag == '-s':
                file.write(f"{date.today()}: {phrase}\n")
        except:
            break