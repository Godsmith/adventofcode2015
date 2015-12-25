__author__ = 'Filip'

from operator import mul

def step_through_set(current_set, remainder, target_sum, possible_sets):
    for value in remainder:
        new_set = current_set | {value}
        new_remainder = remainder - {value}
        sum_ = sum(new_set)
        if sum_ < target_sum:
            step_through_set(new_set, new_remainder, target_sum, possible_sets)
        elif sum_ == target_sum:
            print new_set
            possible_sets.add(frozenset(new_set))

def step_indices(indices, max_):
    """steps [1,3,5,6] to [1,3,5,7] if max > 6
    and [1,3,5,6] to [1,4,5,6] if max == 6
    and [1,2,3,6] to [1,2,4,5] if max == 6"""
    for i in range(len(indices))[::-1]:
        max_for_current_index = max_ - (len(indices) - i) + 1
        if indices[i] == max_for_current_index:
            # if the index cannot move
            pass
        else:
            indices[i] += 1
            # set the following indices to immediately following the current
            addition = 1
            for j in range(i+1, len(indices)):
                indices[j] = indices[i] + addition
                addition += 1
            return indices

def go_to_next_step_that_increases_sum(indices):
    """steps [1,4,5,6] to [2,3,4,5]
       returns None for [1,2,3,4]
       step [1,2,3,7] to [1,2,4,5]"""
    for i in range(len(indices))[-2::-1]:
        if indices[i+1] > indices[i] + 1:
            indices[i] += 1
            # set the following indices to immediately following the current
            addition = 1
            for j in range(i+1, len(indices)):
                indices[j] = indices[i] + addition
                addition += 1
            return indices



with open('input.txt') as f:
    weights = [int(line) for line in f.readlines()][::-1]

total_weight = sum(weights)
one_third_weight = total_weight / 4

possible_package_indices = []

for num_packages in range(1, 7):
    # allocate the first n packages
    package_indices = range(num_packages)

    while package_indices is not None:
        sum_ = sum(weights[i] for i in package_indices)
        #print 'indices: {}. sum: {}.'.format(package_indices, sum_)
        if sum_ == one_third_weight:
            possible_package_indices.append(list(package_indices))
        if sum_ > one_third_weight:
            package_indices = step_indices(package_indices, len(weights)-1)
        elif sum_ <= one_third_weight:
            package_indices = go_to_next_step_that_increases_sum(package_indices)

products = []
for package_indices in possible_package_indices:
    selected_weights = [weights[i] for i in package_indices]
    products.append(reduce(mul, selected_weights, 1))

print min(products)




#print step_indices([1,3,5,6], 7)
#print step_indices([1,3,5,6], 6)
#print step_indices([1,2,3,6], 6)

# print go_to_next_step_that_increases_sum([1,4,5,6])
# print go_to_next_step_that_increases_sum([1,2,3,7])
#print go_to_next_step_that_increases_sum([1,2,3,4])
#
# possible_sets = set()
#
# #step_through_set(set(), weights, one_third_weight, possible_sets)
#
# print possible_sets
