# 트라이 풀이
import sys
input = lambda : sys.stdin.readline().strip()

def insert(trie, number):
    head = trie
    for token in number:
        head[token] = head.get(token, {})
        head = head[token]
    head["EOF"] = number

def go(trie, number):
    head = trie
    for token in number:
        head = head[token]
    return head

def solve(numbers):
    trie = {}
    for number in numbers:
        insert(trie, number)
    for number in numbers:
        if len(go(trie, number)) != 1:
            return "NO"
    return "YES"

if __name__ == "__main__":
    t = int(input())
    print(*[solve([input() for _ in range(int(input()))]) for _ in range(t)], sep="\n")

# 정렬 풀이
import sys
input = lambda : sys.stdin.readline().strip()
def solve(numbers):
    tmp = sorted(numbers)
    for i in range(1,len(tmp)):
        if tmp[i][:len(tmp[i-1])] == tmp[i-1]:
            return "NO"
    return "YES"

if __name__ == "__main__":
    t = int(input())
    print(*[solve([input() for _ in range(int(input()))]) for _ in range(t)], sep="\n")
