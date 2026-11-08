# print all pair of numbers from all list

l = [1,2,3,4,5]

for i in range (len(l)):
    for j in range(i+1,len(l)):
        print(l[i], l[j])




sentence = "I study in UIU"

letter_count = {}

for letter in sentence:
    if letter != " ":
        letter = letter.lower()
        if letter in letter_count:
            letter_count[letter] += 1
        else:
            letter_count[letter] = 1

print(letter_count)