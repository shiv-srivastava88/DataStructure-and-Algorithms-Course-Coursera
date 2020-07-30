def minRefill(dist, m, n, Stops):
    Stops.insert(0,0)
    Stops.append(dist)
    num_refill,curr_refill = 0,0
    while curr_refill <= n:
        last_refill = curr_refill
        while (curr_refill <= n and Stops[curr_refill + 1] - Stops[last_refill] <= m):
            curr_refill += 1
        if curr_refill == num_refill :
            return -1
        if curr_refill <= n:
            num_refill +=1
    return num_refill

            
     
dist = int(input())
m = int(input())
n = int(input())
Stops = list(map(int, input().strip().split()))
print(minRefill(dist, m, n, Stops))
