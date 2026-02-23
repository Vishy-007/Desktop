file1 = open("dupli.txt", "r")
file2 = open("update.txt", "r")
file3 = open("random.txt", "w")

file3.write(file1.read())
file3.write("\n")
file3.write(file2.read())

file1.close()
file2.close()
file3.close()