with open("day3.txt", "r") as file:
    day3 = [line.strip()for line in file]

    priorities = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

    first_half = None
    second_half = None
    letters = []
    score = 0

    for text in day3:
        first_half = text[:int(len(text)/2)]
        second_half = text[int(len(text)/2):]
        for i in first_half:
            if i in second_half:
                if i in letters:
                    continue
                else:
                    letters.append(i)

    for letter in letters:
        number = 0
        for prioritie in priorities:
            if prioritie == letter:
                score = score + number + 1
            else:
                number = number + 1

    print(score)