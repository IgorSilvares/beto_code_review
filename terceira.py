# Write a function to find the sum of all even numbers in an array

def sum_of_even(array):
    sum = 0
    for num in array:
        if num % 2 == 0:
            sum += num
    return sum

test = (1,2,3,4,5,6)
print(sum_of_even(test))