# Adott egy egész számokból álló lista.
# Egy elem kivételével, minden elem kétszer fordul elő a listában.
# Keresd meg melyik az az elem, ami csak egyszer szerepel a listában.
# Example 1:
# Input: nums = [2,2,1]
# Output: 1
# Example 2:
# Input: nums = [4,1,2,1,2]
# Output: 4

my_list = [4, 1, 2, 4, 3, 5, 6, 1, 2, 7]

for i in my_list:
    if my_list.count(i) == 1:
        print(i)
