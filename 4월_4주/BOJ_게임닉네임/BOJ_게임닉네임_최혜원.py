import sys
from collections import defaultdict, deque
input = lambda : sys.stdin.readline()

def same_part(name1, name2):
    length = 0
    if len(name1) > len(name2):
        length = len(name2)
    else:
        length = len(name1)
    for l in range(length):
        if name1[l] != name2[l]:
            return l
    return length

n = int(input())

names = [input().strip() for _ in range(n)]
def solv1(names):
    name_dict = defaultdict(dict) #{pre: {name:cnt}}

    for name in names:
        flag = False
        q = deque([])
        for prefix_len in range(1, len(name)+1, 1):
            prefix = name[0:prefix_len]
            if prefix in name_dict:
                if name in name_dict[prefix]:
                    name_dict[prefix][name] += 1
                    print(name + str(name_dict[prefix][name]))
                    flag = False
                    break
                else:
                    flag = True
                    for key, value in name_dict[prefix].items():
                        idx = same_part(key, name)
                        q.append(name[:idx+1])
                        continue
            else:
                if not flag:
                    name_dict[prefix][name] = 1
                    print(prefix)
                    break
        if flag:
            val = ''
            while q:
                p = q.popleft()
                if len(val) < len(p):
                    val = p
            name_dict[val][name] = 1
            print(val)
def solv2(names):
    name_dict = {}
    class Node:
        def __init__(self, s) -> None:
            self.s = s
            self.children = []
            self.parents = []
        def print_children(self):
            for c in self.children:
                print(c.s)
            print('---')
    class Trie:
        def __init__(self) -> None:
            self.root = Node(None)
        def insert(self, string):
            # print(string)
            if string in name_dict:
                name_dict[string] += 1
                print(string + str(name_dict[string]))
                return
            head = self.root
            parent_str = string[0]

            for idx, s in enumerate(string):
                isin = False
                for node in head.children:
                    if node.s == s:
                        head = node
                        isin = True
                        parent_str = string[:idx+2]
                        break
                if not isin:
                    # print(222, s)
                    n_node = Node(s)
                    head.children.append(n_node)
                    head = n_node
                if idx == len(string) - 1:
                    if parent_str == name:
                        if head.children == []:
                            if parent_str not in name_dict:
                                name_dict[name] = 1
                                print(parent_str)
                        else:
                            if parent_str not in name_dict:
                                name_dict[name] = 1
                                print(parent_str)
                    else:
                        name_dict[name] = 1
                        print(parent_str)
                        
    trie = Trie()
    for name in names:
        trie.insert(name)

# 구현으로 그냥 풂
# solv1(names)
solv2(names)