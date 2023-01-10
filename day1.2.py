with open("day1.txt", "r") as file:
    day1 = [line.strip() for line in file]
    sums = 0
    highest = 0
    second_highest = 0
    third_highest = 0

    for calories in day1:
        if calories == "":
            if sums > highest:
                third_highest = second_highest
                second_highest = highest
                highest = sums
            elif sums > second_highest and sums < highest:
                third_highest = second_highest
                second_highest = sums
            elif sums > third_highest and sums < second_highest:
                third_highest = sums
            sums = 0
        else:
            sums += int(calories)
    
    print(third_highest + second_highest + highest)