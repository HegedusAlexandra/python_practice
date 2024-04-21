maxNumber = 12

# Node format: [target_sum, {fixed_position: fixed_value}, [excluded_nums]]

#original

nodes = [
    [23, {3: 1}, [5]],  
    [37, {}, [1, 5]],
    [30, {2: 5}, [1]],
    [27, {0: 1}, [5]],
    [40, {}, [1, 5]],
    [24, {1: 5}, [1]]
] 

#test 1 - hold position, change number, numbers - 2, no common node

""" nodes = [
    [23, {3: 1}, [6]],  
    [37, {}, [1, 6]],
    [30, {2: 6}, [1]],
    [27, {0: 1}, [6]],
    [40, {}, [1, 6]],
    [25, {1: 6}, [1]]
] """

#test2 - change position, change number, numbers - 2, no common node

""" nodes = [
    [23, {3: 1}, [12]],  
    [33, {}, [1 , 12]],
    [30, {}, [1 , 12]],
    [23, {0: 1}, [12]],
    [36, {2: 12}, [1]],
    [25, {3: 12}, [1]]
] """

# find all the possible combinations for the given node, 
# from numbers until maxNumber including the number at position what is in the object excluding the last number / numbers 

def find_valid_combinations (target_sum, fixed_position, excluded_nums):
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

array1 = find_valid_combinations(*nodes[0])
array2 = find_valid_combinations(*nodes[1])
array3 = find_valid_combinations(*nodes[2])
array4 = find_valid_combinations(*nodes[3])
array5 = find_valid_combinations(*nodes[4])
array6 = find_valid_combinations(*nodes[5])

# compare two nodes with given common position

def remove_duplicates(arrays):
    tuples = set(tuple(array) for array in arrays)
    return [list(t) for t in tuples]

def find_common_with_matching_positions(arr1, arr2, positions1, positions2):
    filtered = [[], []]

    # Function to check matching positions
    def positions_match(el1, el2):
        return all(el1[pos1] == el2[pos2] for pos1, pos2 in zip(positions1, positions2))

    # Function to check uniqueness except at matching positions
    def is_unique_except_positions(el1, el2):
        combined = [el for i, el in enumerate(el1 + el2) if i not in positions1 + [x + len(el1) for x in positions2]]
        return len(combined) == len(set(combined))

    for el1 in arr1:
        for el2 in arr2:
            if positions_match(el1, el2) and is_unique_except_positions(el1, el2):
                filtered[0].append(el1)
                filtered[1].append(el2)

    # Remove duplicates
    filtered[0] = remove_duplicates(filtered[0])
    filtered[1] = remove_duplicates(filtered[1])

    return filtered

constellation_type_1=[[1,2],[0,3]]
constellation_type_2=[[2,3],[1,0]]
constellation_type_middle_1=[[2],[0]]
constellation_type_middle_2=[[3],[1]]

array1 = find_common_with_matching_positions(array1, array2, *constellation_type_1)[0]
array2 = find_common_with_matching_positions(array1, array2, *constellation_type_1)[1]

array2 = find_common_with_matching_positions(array2, array3, *constellation_type_1)[0]
array3 = find_common_with_matching_positions(array2, array3, *constellation_type_1)[1]

array4 = find_common_with_matching_positions(array4, array5, *constellation_type_1)[0]
array5 = find_common_with_matching_positions(array4, array5, *constellation_type_1)[1]

array5 = find_common_with_matching_positions(array5, array6, *constellation_type_1)[0]
array6 = find_common_with_matching_positions(array5, array6, *constellation_type_1)[1]

array1 = find_common_with_matching_positions(array1, array4, *constellation_type_2)[0]
array4 = find_common_with_matching_positions(array1, array4, *constellation_type_2)[1]

array2 = find_common_with_matching_positions(array2, array5, *constellation_type_2)[0]
array5 = find_common_with_matching_positions(array2, array5, *constellation_type_2)[1]

array3 =  find_common_with_matching_positions(array3, array6, *constellation_type_2)[0]
array6 =  find_common_with_matching_positions(array3, array6, *constellation_type_2)[1]

array1 =  find_common_with_matching_positions(array1, array5, *constellation_type_middle_1)[0]
array5 =  find_common_with_matching_positions(array1, array5, *constellation_type_middle_1)[1]

array2 =  find_common_with_matching_positions(array2, array6, *constellation_type_middle_1)[0]
array6 =  find_common_with_matching_positions(array2, array6, *constellation_type_middle_1)[1]

array2 =  find_common_with_matching_positions(array2, array4, *constellation_type_middle_2)[0]
array4 =  find_common_with_matching_positions(array2, array4, *constellation_type_middle_2)[1]

array3 =  find_common_with_matching_positions(array3, array5, *constellation_type_middle_2)[0]
array5 =  find_common_with_matching_positions(array3, array5, *constellation_type_middle_2)[1]




array1 = find_common_with_matching_positions(array1, array2, *constellation_type_1)[0]
array2 = find_common_with_matching_positions(array1, array2, *constellation_type_1)[1]

array2 = find_common_with_matching_positions(array2, array3, *constellation_type_1)[0]
array3 = find_common_with_matching_positions(array2, array3, *constellation_type_1)[1]

array4 = find_common_with_matching_positions(array4, array5, *constellation_type_1)[0]
array5 = find_common_with_matching_positions(array4, array5, *constellation_type_1)[1]

array5 = find_common_with_matching_positions(array5, array6, *constellation_type_1)[0]
array6 = find_common_with_matching_positions(array5, array6, *constellation_type_1)[1]

array1 = find_common_with_matching_positions(array1, array4, *constellation_type_2)[0]
array4 = find_common_with_matching_positions(array1, array4, *constellation_type_2)[1]

array2 = find_common_with_matching_positions(array2, array5, *constellation_type_2)[0]
array5 = find_common_with_matching_positions(array2, array5, *constellation_type_2)[1]

array3 =  find_common_with_matching_positions(array3, array6, *constellation_type_2)[0]
array6 =  find_common_with_matching_positions(array3, array6, *constellation_type_2)[1]

array1 =  find_common_with_matching_positions(array1, array5, *constellation_type_middle_1)[0]
array5 =  find_common_with_matching_positions(array1, array5, *constellation_type_middle_1)[1]

array2 =  find_common_with_matching_positions(array2, array6, *constellation_type_middle_1)[0]
array6 =  find_common_with_matching_positions(array2, array6, *constellation_type_middle_1)[1]

array2 =  find_common_with_matching_positions(array2, array4, *constellation_type_middle_2)[0]
array4 =  find_common_with_matching_positions(array2, array4, *constellation_type_middle_2)[1]

array3 =  find_common_with_matching_positions(array3, array5, *constellation_type_middle_2)[0]
array5 =  find_common_with_matching_positions(array3, array5, *constellation_type_middle_2)[1]

""" print('common_with',*array1 )
print('common_with',*array2 )
print('common_with',*array3 )
print('common_with',*array4 )
print('common_with',*array5 )
print('common_with',*array6 ) """

# Structured assembly of result based on specified indices from the arrays
result = [
    [array1[0][0], array1[0][1], array2[0][1], array3[0][1]],
    [array1[0][3], array4[0][1], array6[0][0], array6[0][1]],
    [array4[0][3], array4[0][2], array6[0][3], array6[0][2]]
]

for row in result:
    print(row)