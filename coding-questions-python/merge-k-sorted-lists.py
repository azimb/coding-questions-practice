def merge_sorted_lists(sorted_lists):
    if len(sorted_lists) == 1:
        return sorted_lists[0]
    result = merge_first_two(sorted_lists)
    return merge_sorted_lists(result)

def merge_first_two(sorted_lists):
    updated = []
    for i in range(0, len(sorted_lists) - 1, 2):
        result = merge(sorted_lists[i], sorted_lists[i+1])
        updated.append(result)
    return updated

def merge(list_one, list_two):
    result = []
    u = v = 0
    while u < len(list_one) and v < len(list_two):
        if list_one[u] <= list_two[v]:
            result.append(list_one[u])
            u += 1
        else:
            result.append(list_two[v])
            v += 1
    if v < len(list_two):
        copy_remaining(result, list_two, v)

    if u < len(list_one):
        copy_remaining(result, list_one, u)

    return result

def copy_remaining(list_one, list_two, index):
    for i in range(index, len(list_two)):
        list_one.append(list_two[i])

print(merge_sorted_lists( [[1,3,5,7],[2,4,6,8],[10,12,14,16],[9,11,13,15]] ))