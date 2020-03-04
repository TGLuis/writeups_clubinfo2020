import  cv2

def get_indices():
    with open("decrypted.hint.mp3") as f:
        text = f.readlines()[0].strip()
        return [int(i) for i in text.split(" ")]

if __name__=="__main__":
    img = cv2.imread("zorro.png")
    ints = get_indices()
    col = 780
    height = 585
    values = []
    pixels = []
    valvert = []
    for x in ints:
        v = img[x//col][x%col][0]%2
        pixels.append(img[x//col][x%col][0])
        values.append(str(v))
    print(" ".join([str(i) for i in pixels]))
    print("".join(values))
    print(("".join(values))[::-1])
    
    bitstring = ("".join(values))[::-1]
    flag = ""
    for i in range(12):
        a = i*8
        flag += chr(int(bitstring[a:a+8], 2))
    print(flag)
    # todo interpret the last string as ascii
