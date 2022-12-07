#%%
with open("input", "r") as f:
    rows = [x.strip().split(',') for x in f.readlines()]

#%%
result = 0
for row in rows:
    rangA = [int(x) for x in row[0].split('-')]
    rangB = [int(x) for x in row[1].split('-')]
    if rangA[0] <= rangB[0] and rangA[1]>= rangB[1]:
        result+=1
    elif rangA[0] >= rangB[0] and rangA[1]<= rangB[1]:
        result+=1
print(result)


# %%
result = 0
for row in rows:
    rangA = [int(x) for x in row[0].split('-')]
    rangB = [int(x) for x in row[1].split('-')]
    if not (rangA[1] < rangB[0] or rangA[0] > rangB[1]):
        result+=1
print(result)
# %%
