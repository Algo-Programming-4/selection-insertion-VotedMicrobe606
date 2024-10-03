def bubbleSort(x):
    y = len(x)
    z = x[:]
    for a in range(y):
        for b in range(y - 1):
            if z[b] > z[b + 1]:
                # Swap
                temp = z[b]
                z[b] = z[b + 1]
                z[b + 1] = temp
    return z

def selectionSort(m):
    n = len(m)
    p = m[:]
    for q in range(n):
        minIdx = q
        for r in range(q + 1, n):
            if p[r] < p[minIdx]:
                minIdx = r
        # Swap
        temp = p[q]
        p[q] = p[minIdx]
        p[minIdx] = temp
    return p

def insertionSort(s):
    t = len(s)
    u = s[:]
    for v in range(1, t):
        key = u[v]
        w = v - 1
        while w >= 0 and u[w] > key:
            u[w + 1] = u[w]
            w -= 1
        u[w + 1] = key
    return u

