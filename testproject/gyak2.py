# Írjunk egy függvényt, amiben bekérünk egy pozitív egész (min kétjegyű) számot, és kiírjuk a kimenetre a számot fordított lista formájában
# Example:
# input: 123456
# print out : [6, 5, 4, 3, 2, 1]

my_num = input("Adj meg egy min kétjegyű egész számot: ")


def inverz_lista():
    my_list = list(my_num)
    my_inverz_lista = (my_list[:: -1])
    print(my_inverz_lista)


inverz_lista()
