def sort_merge(arr):
    if len(arr) <= 1:
        return arr
    m = int(len(arr) / 2)
    l, r = sort_merge(arr[m:]), sort_merge(arr[:m])
    return merge(l, r)

def merge(l, r):

    l_index = r_index = 0
    results = []
    while l_index < len(l) and r_index < len(r):
        if l[l_index] < r[r_index]:
            results.append(l[l_index])
            l_index += 1
        else:
            results.append(r[r_index])
            r_index += 1
    results.extend(l[l_index:])
    results.extend(r[r_index:])
    return results