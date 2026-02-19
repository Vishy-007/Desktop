file = open("random.txt", "r")

content = file.read()
lines = content.split('\n')

count = 0

for i in lines:
    if i:
        count += 1
        print(" No. of lines in the file: ", count)

