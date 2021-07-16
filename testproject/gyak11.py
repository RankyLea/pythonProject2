# Adott szavak listája:
# words = ["cat", "mouse", "fair", "fire", "fuel", "movie", "pirate", "nature"]

# Számoljuk meg hány jó szó van a listában?
# Azt a szót tartjuk jó szónak, ami páros számú karakterből áll.
# (dog: not good, apple: not good, baby: good, acid: good)

words = ["cat", "mouse", "fair", "fire", "fuel", "movie", "pirate", "nature"]
good_words = []

for actual_word in words:
    if len(actual_word) % 2 == 0:
        good_words.append(actual_word)
print(len(good_words))

# n = 0
# for i in words:
#     mennyi = len(i)
#     if mennyi % 2 == 0:
#         n = n+1
# print(n)