with open("day2.txt", "r") as file:
    day2 = [line.strip() for line in file]
    print(day2)

    X = 1
    Y = 2
    Z = 3

    win = 6
    draw = 3
    lose = 0
    score = 0

    for i in day2:
        if i[0] == "A" and i[-1] == "X":
            score = score + X + draw
        elif i[0] == "A" and i[-1] == "Y":
            score = score + Y + win
        elif i[0] == "A" and i[-1] == "Z":
            score = score + Z + lose

        if i[0] == "B" and i[-1] == "X":
            score = score + X + lose
        elif i[0] == "B" and i[-1] == "Y":
            score = score + Y + draw
        elif i[0] == "B" and i[-1] == "Z":
            score = score + Z + win
        
        if i[0] == "C" and i[-1] == "X":
            score = score + X + win
        elif i[0] == "C" and i[-1] == "Y":
            score = score + Y + lose
        elif i[0] == "C" and i[-1] == "Z":
            score = score + Z + draw
    
    print(score)
