#%% 
def charToPriority(char):
    if 'a' <= char <= 'z':
        return ord(char) - ord('a') + 1
    elif 'A' <= char <= 'Z':
        return ord(char) - ord('A') + 27
    else:
        return 0
#%%
with open("input", "r") as f:
    rows = [x.strip() for x in f.readlines()]

#%% 
total = 0
for r in rows:
    total += charToPriority((set(r[:len(r)//2]) & set(r[len(r)//2:])).pop())
print(total)
# %%
from itertools import zip_longest
from functools import reduce
#%%
total = 0
N = 3
for rs in zip_longest(*( [iter(rows)]*N)):
    intersection = reduce(lambda x,y: set(x) & set(y), rs)
    total += charToPriority(intersection.pop())
print(total)
# %%
