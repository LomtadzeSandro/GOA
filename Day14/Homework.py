# numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
# print(numbers)

# numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
# even_numbers = [num for num in numbers if num % 2 == 0]
# print(even_numbers)


# my_array = []

# for i in range(50, 101):
#     my_array.append(i)

# print(my_array[-len(my_array):])


# while True:
#     try:
#         num1 = int(input("Enter the first number: "))
#         num2 = int(input("Enter the second number: "))
#         break
#     except ValueError:
#         print("Please enter valid integers.")

# start = min(num1, num2)
# end = max(num1, num2)

# for i in range(start, end + 1):
#     if i % 5 == 0:
#         print(i)




array = list(range(51))

output = array[0:26]
print("Original Array:", output)

next_second = output[0:3] + output[6:]
print("Next Second Array:", next_second)


 
  

