my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# Basic slicing examples
sliced_list = my_list[2:7]
print("Sliced List 1:", sliced_list)
#Slicing from the beginning
sliced_list = my_list[:4]
print("Sliced List 2:", sliced_list)
# Slicing from index 5
sliced_list = my_list[5:]
print("Sliced List 3:", sliced_list)
#Slicing with a step of 2
sliced_list = my_list[1:9:2]
print("Sliced List 4:", sliced_list)
# Negative indexing
#  Slicing the last 3 elements of the list
sliced_list = my_list[-3:]
print("Sliced List 5:", sliced_list)
#  Reversing the list
sliced_list = my_list[::-1]
print("Reversed List:", sliced_list)



even_numbers = [2, 4, 6, 8, 2, 4, 10]
odd_numbers = [1, 3, 5, 7, 3, 9]
combined_list = even_numbers + odd_numbers
number_occurrences = {}
for number in combined_list:
    if number in number_occurrences:
        number_occurrences[number] += 1
    else:
        number_occurrences[number] = 1

print("Combined List:", combined_list)
print("Number Occurrences:")
for number, count in number_occurrences.items():
    print(f"{number}: {count}")
