################
#              #
# Import Block #
#              #
################

import sys
import random
import getopt
from types import resolve_bases

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

    # arguments
    try:
        opts, arg = getopt.getopt(sys.argv[1:], "rf",[])
    except getopt.GetoptError:
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-r':
            reverse = True
        elif opt == '-f':
            flip = True

    # cli loop
    while True:
        phrase = pg.get_new_string(reverse=reverse)
        if flip:
            phrase = phrase[::-1]
        input(phrase)