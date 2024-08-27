def calculate_probability():
    success_count = 0
    total_count = 0

    for d1 in range(1, 7):
        for d2 in range(1, 7):
            for d3 in range(1, 7):
                product = d1 * d2 * d3
                sum_of_dice = d1 + d2 + d3
                
                if (product / 2) > sum_of_dice:
                    success_count += 1
                
                total_count += 1

    probability = success_count / total_count
    return probability

probability = calculate_probability()
print(f"The probability that half the product of three dice will exceed their sum: {probability:.4f}")
