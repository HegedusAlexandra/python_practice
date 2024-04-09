maxNumber = 12

# Node format: [target_sum, {fixed_position: fixed_value}, [excluded_nums]]

nodes = [
    [23, {3: 1}, [5]],  
    [37, {}, [1, 5]],
    [30, {2: 5}, [1]],
    [27, {0: 1}, [5]],
    [40, {}, [1, 5]],
    [24, {1: 5}, [1]]
]

def find_valid_combinations(target_sum, fixed_position, excluded_nums):
    all_combinations = []

    # Generate all possible combinations of numbers from 1 to maxNumber
    for i in range(1, maxNumber + 1):
        if i in excluded_nums:
            continue  # Skip excluded numbers
        for j in range(1, maxNumber + 1):
            if j in excluded_nums or j == i:
                continue
            for k in range(1, maxNumber + 1):
                if k in excluded_nums or k == j or k == i:
                    continue
                for l in range(1, maxNumber + 1):
                    if l in excluded_nums or l == k or l == j or l == i:
                        continue
                    combination = [i, j, k, l]

                    # Apply fixed position constraint
                    if fixed_position:
                        position, fixed_value = list(fixed_position.items())[0]
                        if combination[position] != fixed_value:
                            continue
                    
                    # Check if the combination meets the target sum
                    if sum(combination) == target_sum:
                        all_combinations.append(combination)

    return all_combinations

valid_combinations = find_valid_combinations(*nodes[2])
print(f"Valid combinations for node 3.:")
for combo in valid_combinations:
    print(combo)
