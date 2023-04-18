# https://www.acmicpc.net/problem/16934
import sys
input = sys.stdin.readline

class Node:
    def __init__(self, key, value=0, children=None):
        self.key = key
        self.value = value
        self.children = {} if not children else children

class Trie:
    def __init__(self):
        self.root = Node(None)
    
    def insert(self, string):
        head = self.root
        flag = True
        for idx, token in enumerate(string):
            if token not in head.children:
                head.children[token] = Node(token)
                if flag:
                    print(string[:idx+1])
                    flag = False
            head = head.children[token]
        head.value += 1
        if flag:
            if head.value==1:
                print(string)
            else:
                print(f"{string}{head.value}")


def solve(users):
    trie = Trie()
    for user in users:
        trie.insert(user)

if __name__ == "__main__":
    n = int(input())
    users = [input().rstrip() for _ in range(n)]
    solve(users)