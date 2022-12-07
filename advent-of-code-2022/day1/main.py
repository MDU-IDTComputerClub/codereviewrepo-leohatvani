#%%
with open("input", "r") as f:
    rows = f.readlines()

#%%
rows.append("\n")
# %%
allSums = []
currentValue = 0
for row in rows:
    if row != '\n':
        currentValue += int(row)
    else:
        allSums.append(currentValue)
        currentValue = 0
allSums.sort()
print(allSums[-1])
print(sum(allSums[-3:]))
# %%
