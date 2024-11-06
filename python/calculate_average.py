def calculate_average(numbers):
    total = 0
    for number in numbers:
        total += number
    average = total / len(numbers)
    return average


# テスト用のリスト
numbers = [1, 2, 3, 4, 5]
print("Average:", calculate_average(numbers))
