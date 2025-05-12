def find_odd_even(numbers):
    odd_numbers = [num for num in numbers if num % 2 != 0]
    even_numbers = [num for num in numbers if num % 2 == 0]

    print("Odd Numbers:", odd_numbers)
    print("Even Numbers:", even_numbers)

# Example usage
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
find_odd_even(numbers)