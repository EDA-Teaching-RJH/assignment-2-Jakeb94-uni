numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
numbers.sort()
numbers = [num for num in numbers if num != 1]
numbers.extend([7, 8])
print("Final List",",".join(map(str, numbers)))
# 1st is list of numebrs. 2nd sorts numebrs in acending order. 
# 3rd removes all the'1's from list. 4th puts 7,8 on the end of the list. 
# final adds final list, adds comma between numbers and removes square brackets from print.
