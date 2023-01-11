day3 = ["vJrwpWtwJgWrhcsFMMfFFhFp", "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL", "PmmdzqPrVvPwwTWBwg", "wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn", "ttgJtRGJQctTZtZT", "CrZsJsPPZsGzwwsLwLmpwMDw"]
priorities = [j for j in range(0, 52)]

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

print(priorities)