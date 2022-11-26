import random
def cawbull():
    box = []
    for _ in range(4):
        box.append(random.randint(0, 9))

    a, b, c, d = 11, 11, 11, 11
    print(box)
    while box[0] != a or box[1] != b or box[2] != c or box[3] != d:
        bulls = []
        cows = []
        number = input("Podaj numer:\n")
        a = int(number[0])
        b = int(number[1])
        c = int(number[2])
        d = int(number[3])

        if a == box[0]:
            cows.append(a)
        elif a == box[1] or a == box[2] or a == box[3]:
            bulls.append(a)

        if b == box[1]:
            cows.append(a)
        elif b == box[0] or b == box[2] or b == box[3]:
            bulls.append(a)

        if c == box[2]:
            cows.append(a)
        elif c == box[0] or c == box[1] or c == box[3]:
            bulls.append(a)

        if d == box[3]:
            cows.append(a)
        elif d == box[0] or d == box[1] or d == box[2]:
            bulls.append(a)

        print(f"Cows: {len(cows)} Buls: {len(bulls)}")
        cows.clear()
        bulls.clear()


cawbull()