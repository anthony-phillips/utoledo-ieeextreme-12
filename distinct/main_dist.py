val = input()
val = list(map(int, input().split()))

max_val = max(val)
lookup = [0 for _ in range(max_val+1)]

for num in val:
    lookup[num] += 1

steps = 0
while max(lookup) != 1:
    m = max(lookup)
    indexes = [i for i, j in enumerate(lookup) if j == m]
    index = indexes[0]

    if index - 1 <= -1:
        lookup.insert(0, 0)
        # because inserting messes up the indexes
        lookup[index] += 1
        lookup[index + 1] -= 1
        # check if smaller num is to left and check if moving left is the fastest way to get rid of it
    elif lookup[index - 1] < lookup[index] and (index + 1 < len(lookup)) and lookup[index + 1] >= lookup[index - 1]:
            lookup[index - 1] += 1
            lookup[index] -= 1

    elif index + 1 >= len(lookup):
        lookup.insert(len(lookup), 0)
        lookup[index + 1] += 1
        lookup[index] -= 1
    else:
        if lookup[index + 1] <= lookup[index]:
            lookup[index + 1] += 1
            lookup[index] -= 1
    steps += 1

print(steps)
