# Az alábbi mintát jelenítsd meg for ciklus segítségével!
# Minta:
# 5 4 3 2 1
# 4 3 2 1
# 3 2 1
# 2 1
# 1
#
# l = [1, 2, 3, 4, 5]
# #
# # # list = [5, 4, 3, 2, 1]
# # # list = list(reversed(x))
# #
# list = l[::-1]

# SORONKÉNT ÍRJA KI

# for j in range(5):
#     for i in list[j:]:
#         print(i, end=' ')
#     print()
#
# x = [5, 4, 3, 2, 1]

# y = []
# for j in range(5):
#     y.append(x[j:])
# print(y)
# for idx, i in enumerate(y):
#     for k in range(len(i)):
#         print(y[idx][k], end=' ')
#     print()


# OSZLOPONKÉNT ÍRJA KI:
#
x = [5, 4, 3, 2, 1]
y = []
for j in range(5):
    y.append(x[j:])
for i in y:
    print(*i)
