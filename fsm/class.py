import numpy as np

class FSM:
    def __init__(self, filename):
        self.filename = filename
        self.data= []
        self.tag_data= []
        self.morph_c = {}
        self.stems = []

        self.load()
        self.count()
        self.print()
        self.findStems()

    def load(self):
        with open(self.filename, 'r') as F:
            lines = F.read().split('\n')[:-1]
            self.data = [l.split() for l in lines]

    def count(self):
        for word in self.data:
            for morph in word:
                try:
                    self.morph_c[morph] += 1
                except KeyError:
                    self.morph_c[morph] = 1
    def findStems(self):
        for word in self.data:
            min_c = 10000
            val = ''
            for morph in word:
                comp = self.morph_c[morph]
                if min_c > comp:
                    min_c = self.morph_c[morph]
                    val = morph
            self.stems.append(val)
        self.stems = list(set(self.stems))
            

    
    def print(self):
        #print(self.data)
        #print('Data size:', len(self.data))
        print(self.morph_c)
        print("Stems: ", self.stems)


if __name__ == '__main__':
    fsm = FSM('trainseg.wix')

