# %%
def uniqueCharacters(mystr):
    return len(set(mystr)) == len(mystr)

def computePart1(buffer, n=4):
    for start in range(n, len(buffer)):
        if uniqueCharacters(buffer[start-n:start]):
            return start


