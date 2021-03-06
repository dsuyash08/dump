# Uses python3
import sys
import random

def partition3(a, l, r):
    #write your code here
    pass

def partition3(a, l, r):
    x = a[l]
    j, k = l, l
    for i in range(l + 1, r + 1):
        if a[i] <= x:
            j += 1
            a[i], a[j] = a[j], a[i]            
            if(k != l):
                a[k] , a[j] = a[j] , a[k]
                k += 1 
            if a[j] == x and k == l:
                k = j
    if(k != l):
        a[l], a[k-1] = a[k-1], a[l]
    else:
        a[l],a[j] =a[j],a[l]    
        k = j
    return k, j


def randomized_quick_sort(a, l, r):
    if l >= r:
        return
    k = random.randint(l, r)
    a[l], a[k] = a[k], a[l]
    #use partition3
    m,n = partition3(a, l, r)
    randomized_quick_sort(a, l, m - 1);
    randomized_quick_sort(a, n + 1, r);


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    randomized_quick_sort(a, 0, n - 1)
    for x in a:
        print(x, end=' ')
