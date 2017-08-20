

def compare(hypfile, reffile):
    hyp = open(hypfile).read().split("\n")
    ref = open(reffile).read().split("\n")

    matched = 0
    i = 0
    for n in range(len(hyp)):
        i = i + 1
        if hyp[n] == ref[n]:
            matched = matched + 1
        else:
            pass
            #print(hyp[n], "!=",  ref[n])
    print("Result 1-best match = ", str(float(matched)/float(i)))

if __name__ == "__main__":
    ref  = "testseg.wix"
    wixb = "testseg.wix.hyp"

    compare(wixb, ref)

