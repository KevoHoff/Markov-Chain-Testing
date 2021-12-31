for name in ["trump", "clinton"]:
    fin = open("{}3.txt".format(name))

    lines = [l for l in [l.rstrip() for l in fin.readlines()] if len(l) > 0]

    L = 300

    idx = 0
    filenum = 0
    while idx < len(lines):
        s = ""
        while len(s) < L and idx < len(lines):
            s += lines[idx] + "\n\n"
            idx += 1
        fout = open("%s3-%.2i.txt"%(name, filenum), "w")
        fout.write(s)
        fout.close()
        filenum += 1
