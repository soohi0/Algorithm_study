def solution(x, y, n):
    # dp
    tab = [float('inf')]*(y+1)
    tab[x] = 0
    for i in range(x, y+1):
        if i+n <= y:
            tab[i+n] = min(tab[i+n], tab[i]+1)
        if i*2 <= y:
            tab[i*2] = min(tab[i*2], tab[i]+1)
        if i*3 <= y:
            tab[i*3] = min(tab[i*3], tab[i]+1)
            
    return tab[y] if tab[y] != float('inf') else -1