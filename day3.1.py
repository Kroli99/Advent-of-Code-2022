with open("day3.txt", "r") as file:
    day3 = [line.strip()for line in file]

    priorities = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"  
    first_half = None
    second_half = None
    letter = None
    number = 0

    for text in day3:
        first_half = text[:int(len(text)/2)]
        second_half = text[int(len(text)/2):]
        for i in first_half:
            if i in second_half:
                letter = i
            for j in range(len(priorities)):
                if priorities[j] == letter:
                    number += len(priorities[:j]) + 1

    print(number)