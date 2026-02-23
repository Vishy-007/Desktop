ifile = open("dupli.txt", "r")
ofile = open("update.txt", "w")

s = set()

for line in ifile:
    if line not in s:
        ofile.write(line)
        s.add(line)


ifile.close()
ofile.close()