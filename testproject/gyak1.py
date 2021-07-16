# 1. feladat:
# Adj meg egy egész számot, majd nyomtassa ki annyiszor hogy i sheep, ahányas számot megadtam!
# Használjunk függvényt!
# outputon: 1 sheep... 2 sheep... 3 sheep... stb.

# b = int(input("Adj meg egy pozitív egész számot: "))
# for i in range(b):
#     print(i, "sheep", end=('...'))

def sheep_counter(n):
    for i in range(n):
        print(f"{i + 1} sheep", end="...")
    print()


m = int(input("hanyat? "))
sheep_counter(m)
