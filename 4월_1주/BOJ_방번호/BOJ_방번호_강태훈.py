import sys
input = lambda : sys.stdin.readline().strip()

def main(n):
    for i in range(1, min(87654, n//2+1)):
        a, b = str(i), str(n-i)
        if len(a)!=len(set(a)) or len(b)!=len(set(b)) or set(list(a))&set(list(b)):
            continue
        else:
            print(i, "+", n-i)
            return
    print(-1)
    return

if __name__ == "__main__":
    n = int(input())
    main(n)