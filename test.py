day3 = ["vJrwpWtwJgWrhcsFMMfFFhFp", "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL", "PmmdzqPrVvPwwTWBwg", "wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn", "ttgJtRGJQctTZtZT", "CrZsJsPPZsGzwwsLwLmpwMDw"]
priorities = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

first_half = None
second_half = None
letters = []
number = 0

for text in day3:
    first_half = text[:int(len(text)/2)]
    second_half = text[int(len(text)/2):]
    for i in first_half:
        if i in second_half:
            if i in letters:
                continue
            else:
                letters.append(i)
        for j in range(len(priorities)):
            if priorities[j] == letters:
                number += len(priorities[:j]) + 1
                print(number, letters)
                break

print(number)