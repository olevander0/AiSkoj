def add_block(s):
    return [s, s, s]

def extend_block(block, len1 = 0, len2 = 0, len3 = 0):
    return [block[0] + len1, block[1] + len2, block[2] + len3]

b1 = add_block(10)
print(b1)

print(extend_block(b1, 0, 0, 3))
