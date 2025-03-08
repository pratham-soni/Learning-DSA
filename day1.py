def nuke(n):
    a = []
    for i in range(10):
        if (n>1):
            print('appending nuke(i-1) (',(i-1),')...')
            a.append(nuke(n-1))
        else:
            print('appending i (',i,')')
            a.append(i)
    return a

print(nuke(2))