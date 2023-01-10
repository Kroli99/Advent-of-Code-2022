with open("day1.txt", "r") as file:
    day1 = [line.strip() for line in file]
    sums = 0
    highest = 0

    for calories in day1:
        if calories == "":
            if sums > highest:
                highest = sums
            sums = 0
        else:
            sums += int(calories)
    
    print(highest)

