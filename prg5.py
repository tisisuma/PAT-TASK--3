def distribute_mangoes(bags, students):
    bags.sort()  # Sort the bags in ascending order

    min_difference = float('inf')
    result = []

    for i in range(len(bags) - students + 1):
        current_difference = bags[i + students - 1] - bags[i]

        if current_difference < min_difference:
            min_difference = current_difference
            result = bags[i:i + students]

    return result

# Data given
bags = [3, 7, 1, 9, 5, 10, 7]
students = 3

result = distribute_mangoes(bags, students)
print("Selected bags:", result)
print("Minimum difference:", result[-1] - result[0])

