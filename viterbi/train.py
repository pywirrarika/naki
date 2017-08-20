#!/usr/bin/env python3

# Author: Manuel Mager
# GPL 3.0+
# 2017

import re
from viterbi import viterbi

class morph():
    def __init__(self, filename, verbose=False):
        self.F = open(filename, "r")
        self.Fo = open(filename.split(".")[0] + ".model", "w")

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

        self.verbose=verbose

    def read(self):
        for line in self.F:
            if not line or line == ' ':
                continue
            seg = line.replace("\n", "").lower()
            word = seg.replace(" ", "")
            seg = re.sub(r"[a-z+'] ","|", seg)
            seg = re.sub(r"[a-z+' ]", "w", seg)
            #print(word) 
            #print(seg)
            self.startP(seg)
            self.lines.append((list(word), list(seg)))

            # Pepare sigma for output states and observed values 
            self.states = self.states | set(list(seg))
            self.obs= self.obs | set(list(word))

        self.states = self.states | set('#')
        self.obs= self.obs | set('#')



        #Prepare dics
        for k in self.states:
            self.trans_p[k] = {o:0 for o in self.states}
            self.trans_p_c[k] = {o:0 for o in self.states}
            self.trans_p_n[k] = 0


        for k in self.states:
            self.emit_p[k] = {o:0 for o in self.obs}
            self.emit_p_c[k] = {o:0 for o in self.obs}
            self.emit_p_n[k] = 0

        self.start_p['#'] = 0



        for line in self.lines:
            hidden = line[1]
            obs = line[0]

            # Count the transitions
            for i in range(len(hidden)):
                try:
                    next = hidden[i+1]
                except:
                    next = '#'

                self.trans_p_c[hidden[i]][next] += 1
                self.trans_p_n[hidden[i]] += 1

            # Count the emitions
            for i in range(len(hidden)):
                self.emit_p_c[hidden[i]][obs[i]] += 1
                self.emit_p_n[hidden[i]] += 1



    def startP(self, seg):
        self.start_p_n += 1
        s = seg[:1]
        try:
            self.start_p_c[s] += 1
        except KeyError:
            self.start_p_c[s] = 1

    def p(self):

        #Start Probability
        for c in self.start_p_c.keys():
            self.start_p[c] = self.start_p_c[c] / self.start_p_n

        #Transition Probability
        for s in self.trans_p_c.keys():
            for k in self.trans_p_c[s].keys():
                try:
                    self.trans_p[s][k] = self.trans_p_c[s][k] / self.trans_p_n[s]
                except ZeroDivisionError:
                    self.trans_p[s][k] = 0

        #Emit probability
        for s in self.emit_p_c.keys():
            for k in self.emit_p_c[s].keys():
                try:
                    self.emit_p[s][k] = self.emit_p_c[s][k] / self.emit_p_n[s]
                except ZeroDivisionError:
                    self.emit_p[s][k] = 0


        if self.verbose:
            print('Hidden states:', self.states)
            print('Observed states', self.obs)
            print('Start P:', self.start_p)
            print('Transition P', self.trans_p)
            print('Emit P', self.emit_p)


if __name__ == "__main__":

    trainfile = "trainseg.wix"

    M = morph(trainfile)

    M.read()
    M.p()
    M.save()
    
    seq = list('nekiri')

    estimate = viterbi(seq, M.states, M.start_p, M.trans_p, M.emit_p)
    final = ""
    for i in range(len(estimate)):
        if estimate[i] == 'w':
            final = final + seq[i]
        elif estimate[i] == '|':
            final = final + seq[i]
            final = final + ' ' 
        else:
            break

    print(estimate)
    print(final)


