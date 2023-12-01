'''recursive divide and conquer algorithm'''

list1 = [7, 4, 12, 14, 2, 10, 16, 6]
list2 = [7, 4, 12, 14, 2, 10, 16, 5]
list3 =  [14, 8, 2, 6, 3, 10, 12]

def cPairDist(points):
    sorted_points = sorted(points)
    if len(sorted_points) == 1:
        return sorted_points[0]
    else:
        min_distance = float('inf')
        for i in range(len(sorted_points) - 1):
            distance = abs(sorted_points[i] - sorted_points[i + 1])
            min_distance = min(min_distance, distance)
    return min_distance

# print(cPairDist(list1))
# print(cPairDist(list2))
# print(cPairDist(list3))

def recCPairDist(points):
    # base case
    if len(points) <= 3:
        return cPairDist(points)

    mid = len(points) // 2
    left = points[:mid]
    right = points[mid:]

    min_left = recCPairDist(left)
    min_right = recCPairDist(right)

    # finds min distances across both halves, left[-1] is largest point from left half, right[0] smallest point from right half
    min_cross = min(abs(left[-1] - right[0]), min_left, min_right)

    return min(min_left, min_right, min_cross)

print(recCPairDist(sorted(list1)))
print(recCPairDist(sorted(list2)))
print(recCPairDist(sorted(list3)))