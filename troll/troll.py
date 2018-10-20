n = int(input())


initial = [0] * n

nocorrect = 0
i = 0
while i < n:
    s = ''
    for a in initial:
        s += str(a) + ' '
    print('Q ' + s)
    initial[i] = 1
    #test
    guess = int(input())
    if guess > nocorrect:
        print('better guess')
        nocorrect = guess
    else:
        initial[i] = 0
    
    #print(input())
    i += 1
