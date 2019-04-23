import sys
# objects = list(sys.stdin)
# objects = list(input().strip().split())
sys.stdin
res_lst = list()
for obj in objects:
    if obj not in res_lst:
        res_lst.append(obj)
print(len(res_lst))
