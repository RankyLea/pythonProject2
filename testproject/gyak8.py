# Betűjelek jelölik az egyes kő típusokat.
# Minden karakter egy kő fajtának felel meg. A karakterek kis és nagy betű érzékenyek,
# Tehát az "a" és az "A" különböző típusokat jelölnek.
# A feladat az, hogy megállapítsuk a kövek közül mennyi a drágakő?
#
# Example 1:
# Input: jewels = "aA", stones = "aAAbbbb"
# Output: 3
#
# Example 2:
# Input: jewels = "z", stones = "ZZ"
# Output: 0


def jewels_stones(jewels, stones):
    my_jewels = [str (x) for x in jewels]
    my_stones = [str (x) for x in stones]
    # print(my_jewels)
    # print(my_stones)
    m = 0
    for i in my_jewels:
        count_jewels = my_stones.count(my_jewels[0])
        m += count_jewels
    return m

print(jewels_stones("aAbbc", "aAAbccbbb"))
