import itertools

def calculate_probability_functional():
    # Generate all possible combinations of three dice rolls
    dice_rolls = itertools.product(range(1, 7), repeat=3)
    
    def condition(roll):
        d1, d2, d3 = roll
        product = d1 * d2 * d3
        sum_of_dice = d1 + d2 + d3
        return (product / 2) > sum_of_dice

    successful_rolls = filter(condition, dice_rolls)
    
    successful_rolls_list = list(successful_rolls)
    
    success_count = len(successful_rolls_list)
    total_count = 6 ** 3  

    probability = success_count / total_count
    return probability

probability = calculate_probability_functional()
print(f"The probability that half the product of three dice will exceed their sum: {probability:.4f}")
