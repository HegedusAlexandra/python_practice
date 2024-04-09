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

# find all the possible combinations for the given node, 
# from numbers until maxNumber including the number at position what is in the object excluding the last number / numbers 

def find_valid_combinations(target_sum, fixed_position, excluded_nums):
    all_combinations = []

    # Generate all possible combinations of numbers from 1 to maxNumber
    for i in range(1, maxNumber + 1):
        if i in excluded_nums:
            continue
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

find_valid_combinations_array1 = find_valid_combinations(*nodes[0])
find_valid_combinations_array2 = find_valid_combinations(*nodes[1])
find_valid_combinations_array3 = find_valid_combinations(*nodes[2])
find_valid_combinations_array4 = find_valid_combinations(*nodes[3])
find_valid_combinations_array5 = find_valid_combinations(*nodes[4])
find_valid_combinations_array6 = find_valid_combinations(*nodes[5])

# compare two nodes with given common position

def remove_duplicates(arrays):
    tuples = set(tuple(array) for array in arrays)
    return [list(t) for t in tuples]

def find_common_with_matching_positions(arr1, arr2, positions1, positions2):
    filtered = [[], []]

    for el1 in arr1:
        for el2 in arr2:
            # Corrected the comparison to use elements el1 and el2
            if el1[positions1[0]] == el2[positions2[0]] and el1[positions1[1]] == el2[positions2[1]]:
                filtered[0].append(el1)
                filtered[1].append(el2)

    # Applying remove_duplicates here to ensure the output is unique
    filtered[0] = remove_duplicates(filtered[0])
    filtered[1] = remove_duplicates(filtered[1])

    return filtered


common_1 = find_common_with_matching_positions(find_valid_combinations_array1, find_valid_combinations_array2, [1,2],[0,3])
common_1_array1 = remove_duplicates(common_1[0])
common_1_array2 = remove_duplicates(common_1[1])

common_2 = find_common_with_matching_positions(common_1_array2, find_valid_combinations_array3, [1,2],[0,3])
common_2_array2 = remove_duplicates(common_2[0])
common_2_array3 = remove_duplicates(common_2[1])

common_3 = find_common_with_matching_positions(find_valid_combinations_array4, find_valid_combinations_array5, [1,2],[0,3])
common_3_array4 = remove_duplicates(common_3[0])
common_3_array5 = remove_duplicates(common_3[1])

common_4 = find_common_with_matching_positions(common_3_array5, find_valid_combinations_array6, [1,2],[0,3])
common_4_array5 = remove_duplicates(common_4[0])
common_4_array6 = remove_duplicates(common_4[1])

common_5 = find_common_with_matching_positions(common_1_array1, common_3_array4, [2,3],[1,0])
common_5_array1 = remove_duplicates(common_5[0])
common_5_array4 = remove_duplicates(common_5[1])

common_6 = find_common_with_matching_positions(common_2_array2, common_4_array5, [2,3],[1,0])
common_6_array2 = remove_duplicates(common_6[0])
common_6_array5 = remove_duplicates(common_6[1])

common_7 = find_common_with_matching_positions(common_2_array3, common_4_array6, [2,3],[1,0])
common_7_array3 =  remove_duplicates(common_7[0])
common_7_array6 =  remove_duplicates(common_7[1])


print('common_with',common_5_array1 )
print('common_with',common_6_array2 )
print('common_with',common_7_array3 )
print('common_with',common_5_array4 )
print('common_with',common_6_array5 )
print('common_with',common_7_array6 )