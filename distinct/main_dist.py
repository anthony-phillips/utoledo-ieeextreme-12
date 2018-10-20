val = input()
val = list(map(int, input().split()))

max_val = max(val)
lookup = [0 for _ in range(max_val+1)]

for num in val:
    lookup[num] += 1

m = max(lookup)
steps = 0

while m != 1:
    #indexes = [i for i, j in enumerate(lookup) if j == m]
    index = next(i for i, j in enumerate(lookup) if j == m)

    if index - 1 <= -1:
        lookup.insert(0, 0)
        # because inserting messes up the indexes
        lookup[index] += 1
        lookup[index + 1] -= 1
        # check if smaller num is to left and check if moving left is the fastest way to get rid of it
    elif lookup[index - 1] < lookup[index] and (index + 1 < len(lookup)) and lookup[index + 1] >= lookup[index - 1]:
        if (lookup[0:index].count(1)/len(lookup[0:index]) < lookup[index+1:].count(1)/len(lookup[index+1:])) or ((len(lookup) - index - 1) >= index) or (lookup[index + 1] > lookup[index - 1]):
            lookup[index - 1] += 1
            lookup[index] -= 1
        else:
            lookup[index + 1] += 1
            lookup[index] -= 1

    elif index + 1 >= len(lookup):
        lookup.insert(len(lookup), 0)
        lookup[index + 1] += 1
        lookup[index] -= 1
    else:
        if lookup[index + 1] <= lookup[index]:
            lookup[index + 1] += 1
            lookup[index] -= 1

    m = max(lookup)

    steps += 1

print(steps)
