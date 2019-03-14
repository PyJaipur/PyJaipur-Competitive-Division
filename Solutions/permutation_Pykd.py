T = int(input())
for i in range(0,T):
    N = int(input())
    p = list(map(int,input().split()))
    copy = p.copy()
    check = sorted(p)
    true = 0
    while(True):
        true +=1
        for i in range(0,N):
            p[i] = copy[copy[i]-1]
        
            if (i == N-1):
                copy = p.copy()
        if(p == check):
            print(true)
            break
        if(true >N+5):
            print(-1)
            break
