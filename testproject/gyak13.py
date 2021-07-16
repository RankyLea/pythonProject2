# Caesar Criptor: a fgv kér egy szót és egy egész számot,
# hogy a kraktereket az adott szóban mennyivel tolja el
# a => e
# b => f
# c => g

# def fn(szo, eltolas=0):
#     for betu in szo:
#         print(chr(ord(betu) + eltolas), end="")
#     print()
#
# pelda = "alma"
# crip = "bmnb"
#
# print(pelda)
# fn(pelda, 1)
# fn(crip,-1)

def fn(szo, eltolas=0):
    cripto_text = []
    for betu in szo:
        cripto_text.append(chr(ord(betu) + eltolas))
    return "".join(cripto_text)

pelda = "alma"
crip = "bmnb"

print(fn(pelda, 1))
print(fn(crip,-1))
