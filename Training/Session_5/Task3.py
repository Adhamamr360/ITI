import random

def roll_dice():
    return random.randint(1, 6)

def expected_sum_given_first_die_even():
    even_numbers = [2, 4, 6]
    total_sum = 0
    num_even_outcomes = len(even_numbers)
    
    for even in even_numbers:
        expected_sum = even + sum(range(1, 7)) / 6
        total_sum += expected_sum
    
    return total_sum / num_even_outcomes

expected_sum = expected_sum_given_first_die_even()
print(f"Expected sum given the first die is even: {expected_sum:.1f}")
