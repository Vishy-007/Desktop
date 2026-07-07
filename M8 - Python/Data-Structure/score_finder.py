q_score = [12, 30, 57, 80, 100, 101, 110, 156, 178]

target = 101
steps = 0

# for i in q_score:
#     if i == target:
#         steps += 1 
#         print("Found")
# print(steps)

low = 0
high = len(q_score)-1

# while low <= high:
#     steps += 1
#     mid = (low+high) // 2
#     if q_score[mid] == target:
#         print("Found")
#         break
#     elif q_score[mid] < target:
#         low = mid + 1
#     else:
#         high = mid - 1

# print(steps)

# def average(low, high, target):
#     if low <= high:
        