# o(n)

# def fun1(n):
#     return n * (n+1) // 2

# print(fun1(3)) 

# o(1)

# def fun2(n):
#     count = 0
#     for i in range(1, n+1):
#         count = count + 1
#     return count

# print(fun2(3))

#o(n^2)

def fun3(n):
    count = 0
    for i in range (1, n+1):
        for j in range(1, n+1):
            count = count + 1
    return count

print(fun3(3))