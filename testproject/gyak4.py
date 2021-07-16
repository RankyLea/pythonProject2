# Adott egy egész számokból álló lista.
# Ha legalább egy elem kétszer szerepel a listában, akkor a visszatérési értékünk igaz,
# ha minden elem különböző, azaz csak egyszer szerepel a listában, akkor visszatérési értékünk hamis lesz.
# Example 1:
# Input: nums = [1,2,3,1]
# Output: true
#
# Example 2:
# Input: nums = [1,2,3,4]
# Output: false
#
# Example 3:
# Input: nums = [1,1,1,3,3,4,3,2,4,2]
# Output: true
#
# Example 3:
# Input: nums = [1,1,1,3,3,4,3,2,4,2]
# Output: true

my_list = [1, 2, 3, 1]
other_list = list(map(str, my_list))
print(other_list)
# new_list = [str(x) for x in my_list]
# print(new_list)

for i in other_list:

    if other_list.count(i) >= 2:
        print(True)
    else:
        print(False)
