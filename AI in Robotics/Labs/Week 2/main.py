import random

list = [1,2,3,5,2,8,12,6,3,1,8,1,3,0,20,4,4,5,0,1,5,0,4,5,4,3,3,0]

# 1. find the max & min number in the list

print('this is the maximum,', max(list))

print('this is the minimum,', min(list))

# 2. count the occurrences

print('0 appears', list.count(0), 'times')

print('3 appears', list.count(3), 'times')

# 3. Basic Statistics

sum = 0

for i in list:
    sum += i

print('the sum of the numbers is', sum)

avg = sum / len(list)

print('the average of the numbers is', avg)


# 4. Guessing Game

# randomNum = random.randint(0,10)

# minrand = random.randint(0,(randomNum-1))
# maxrand = random.randint((randomNum+1),11)

# guessNum = int(input(f"\n\nGuess a number\n\nLess than {maxrand} & greater than {minrand}\nInsert number here: "))

# if guessNum == randomNum:
#     print("You guessed it!")
# else:
#     print(f"You didn't guess it!, the correct guess was {randomNum}")
    

# 5. Python Dictionary
print("\n\nPython Dictionaries")

d1 = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100, 11: 121, 12:
144, 13: 169, 14: 196, 15: 225}

print("\nHere is the first dictionary:\n", d1)

d2 = {}

for i in d1:
    if (d1[i] % 3) == 0:
        d2[i] = (d1[i])

print("\nHere is the second dictionary (Multiples of 3):\n", d2)


# 6. Sorting Dictionaries

print("\n\nSorting Dictionaries")

Dict1 = {'20':'2', 'embe':'21wq', '12':'banana', 'juice':'orange'}
# dict(sorted(Dict1.items()))

for i in Dict1:
    num = i
    

print(max(Dict1[]))