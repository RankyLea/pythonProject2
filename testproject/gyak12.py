# maganhangzok = ['a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U']
#
# my_word = input()
# mgh_szamlalo = 0
#
# for betu in my_word:
#
#     # ha a maganhangzok benne van a my_word-ben
#     # ha a betu benne van a maganhangzok-ban
#
#     if betu in maganhangzok:
#         mgh_szamlalo = mgh_szamlalo + 1
#
# print(mgh_szamlalo)

# szo= 'hello'
# #mag_hangz = ["a", "A", "e", "o", "u"]
# szamlalo = 0
# mag_hangz = 'aAeEiIoOuU'
# for betu in szo:
#     #ha a magan_hang benne van a szóban akkor...
#     # ha a betu benne van a magánhangzó
#     if betu in mag_hangz:
#         szamlalo = szamlalo+1
# print(szamlalo)

pelda = "hello"
maganhangzok = ['a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U']
pelda2 = "kamatoskamat"

def counter(word):
    res = 0
    for betu in word:
        if betu in maganhangzok:
            res += 1
    return res
print(counter(pelda))
print(counter(pelda2))
