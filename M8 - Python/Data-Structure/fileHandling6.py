file = open("random.txt", "r")

count = 1

for i in file:
    if (count % 2 != 0):
        print(i)
    count +=1

file.close()
