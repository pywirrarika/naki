import re

class morph():
    def __init__(self, filename):
        self.F = open(filename, "r")

        self.lines = []

        self.states = set()
        self.obs = set()

        self.start_p = {}
        self.start_p_c = {}
        self.start_p_n = 0 

        self.trans_p = {}
        self.trans_p_c = {}
        self.trans_p_n = {}

        self.emit_p = {}
        self.emit_p_c = {}
        self.emit_p_n = {}

    def read(self):
        for line in self.F:
            if not line or line == ' ':
                continue
            seg = line.replace("\n", "").lower()
            word = seg.replace(" ", "")
            seg = re.sub(r"[a-z+'] ","|", seg)
            seg = re.sub(r"[a-z+' ]", "w", seg)
            print(word) 
            print(seg)
            self.startP(seg)
            self.lines.append((word, seg))

            # Pepare sigma for output states and observed values 
            self.states = self.states | set(list(seg))
            self.obs= self.obs | set(list(word))

    
        
    def startP(self, seg):
        self.start_p_n += 1
        s = seg[:1]
        if s == '':
            print('+'*75)
            print(seg)
            print('+'*75)
        try:
            self.start_p_c[s] += 1
        except KeyError:
            self.start_p_c[s] = 1

    def p(self):
        for c in self.start_p_c.keys():
            self.start_p[c] = self.start_p_c[c] / self.start_p_n

        print(self.start_p_c)
        print(self.start_p)
        print(self.states)
        print(self.obs)




if __name__ == "__main__":
    M = morph("trainseg.wix")
    M.read()
    M.p()
