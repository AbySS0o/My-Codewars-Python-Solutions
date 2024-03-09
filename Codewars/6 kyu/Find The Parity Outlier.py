def find_outlier(arr):
    even_numbers = [num for num in arr if num % 2 == 0]
    odd_numbers = [num for num in arr if num % 2 != 0]
    
    if len(even_numbers) == 1:
        return even_numbers[0]
    else:
        return odd_numbers[0]