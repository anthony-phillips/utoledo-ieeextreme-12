def take_second(elem):
    return elem[1]


def get_input():
    inputs = []
    num_lines = input()

    for _ in range(int(num_lines)):
        inputs.append(list(map(int, input().split())))

    sorted_list = sorted(inputs, key=take_second)
    return sorted_list, int(num_lines)


def last_nonconf(arr, i):
    for val in range(i-1, -1, -1):
        if arr[val][1] <= arr[i-1][0]:
            return val
    return -1


def last_nonconf_memo(arr, i):
    for val in range(i-1, -1, -1):
        if arr[val][1] <= arr[i][0]:
            return val
    return -1

def max_score(jobs, n):
    if n == 1:
        return jobs[n-1][2]

    inclProf = jobs[n-1][2]

    i = last_nonconf(jobs, n)
    if i != -1:
        inclProf += max_score(jobs, i + 1)
    non_inc_score = max_score(jobs, n - 1)

    return max(inclProf, non_inc_score)


def find_max():
    jobs, n = get_input()

    memo = [0 for _ in range(n)]
    memo[0] = jobs[0][2]

    for i in range(1, n):
        inclProf = jobs[i][2]
        l = last_nonconf_memo(jobs, i)

        if l != -1:
            inclProf += memo[l]

        memo[i] = max(inclProf, memo[i-1])

    result = memo[n-1]

    return result


#jobs, n = get_input()

#print(max_score(jobs, n))
print(find_max())