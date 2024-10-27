import random
numbers = [random.randint(1, 100) for _ in range(10)]
print("10 Random Numbers From Number Generator:", numbers)
x = 0
while x < len(numbers):
    if numbers[x] % 2 == 0:
        numbers.pop(x)
    else:
        x += 1
numbers.sort()
print("Final List without even numbers:", ",".join(map(str, numbers)))
# 1st import random. 2nd, list assinged, from random ints 1-100 uses for loop to get range of 10 from rand list.
# while loop to run through length of numbers, checks if they are evena and. pop function to remove even numbers from list.
# final list printed without square brackets, a comma in between each number and in acending order.
