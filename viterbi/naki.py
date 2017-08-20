import argparse
import pickle
import os
import sys

from viterbi import viterbi

def decode(word, modelfile, verbose=False):
    if os.path.getsize(modelfile) > 0:
        with open(modelfile, "rb") as data:
            unpickler = pickle.Unpickler(data);
            d = unpickler.load()
    else:
        print("Error reading model file")
        return None
        #d = pickle.load(data)
    states = d[0]
    start_p= d[1]
    trans_p = d[2]
    emit_p = d[3]
    word = list(word)
    estimate = viterbi(word, states, start_p, trans_p, emit_p)

    final = ""
    for i in range(len(estimate)):
        if estimate[i] == 'w':
            final = final + word[i]
        elif estimate[i] == '|':
            final = final + word[i]
            final = final + ' ' 
        else:
            break

    if verbose:
        print(estimate)
    print(final)

if __name__ == '__main__':


    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('--word', dest='word', type=str)
    parser.add_argument('--input', dest='input', type=str)
    parser.add_argument('--model', dest='model',  type=str, required=True)

    args = parser.parse_args()

    if not args.word and not args.input:
        print("Error: --word or --input are required")
        parser.print_help()
        sys.exit()

    if args.word:
        decode(args.word, args.model)
    else:
        if os.path.getsize(args.input) > 0:
            with open(args.input, "r") as F:
                for line in F:
                    word = line.replace("\n", "")
                    decode(word, args.model)
