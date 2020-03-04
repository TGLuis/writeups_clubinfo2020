import  cv2

img = cv2.imread("stegano4.png")
val = []
col = 1224
letters = []
for i in range(16):
    n = ""
    for j in range(8):
        v = img[i][j][1]
        bit = v%2
        if bit != 0:
            print(f"{i},{j} = {bit}")
            letters.append(chr(16*j+i))
        n = n + str(bit)
    val.append(n)
print("".join(val))

ints = [int(i, 2) for i in val]
print(ints)
print(''.join(letters))
