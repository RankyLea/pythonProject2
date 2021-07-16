# s1 = "lo"
# s2 = "hello"

# if s1 in s2: # s1 sting benne van-e s2-ben?

# if s1 not in s2 # s1nincs benne az s2-ben?

def neddle_haystack(needle, haystack):
    if needle not in haystack:
        return -1

    haystack_splits = (haystack.split(needle))

    return len(haystack_splits[0])


print(neddle_haystack("ll", "hellolololo"))


