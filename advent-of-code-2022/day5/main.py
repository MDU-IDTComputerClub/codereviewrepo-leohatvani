# %%
def loadStacks(start_configuration, number_of_stacks):
    stacks = [[] for _ in range(number_of_stacks)]
    for row in start_configuration.splitlines():
        for i in range(1, len(row), 4):
            if row[i] != " ":
                stacks[i // 4].insert(0, row[i])
    return stacks


#%%
def moveOne(stacks, stack_from, stack_to):
    stacks[stack_to].append(stacks[stack_from].pop())


def moveN(stacks, n, stack_from, stack_to):
    for _ in range(n):
        moveOne(stacks, stack_from, stack_to)


def moveN9001(stacks, n, stack_from, stack_to):
    stacks[stack_to].extend(stacks[stack_from][-n:])
    del stacks[stack_from][-n:]


def printStacks(stacks):
    for (i, stack) in enumerate(stacks):
        print(i, stack)


# %%
from parse import parse

# %%
def executeMoves(moves, stacks):
    printStacks(stacks)
    for move in moves.splitlines():
        parsed = parse("move {} from {} to {}", move)
        print("moving {} from {} to {}".format(parsed[0], parsed[1], parsed[2]))
        moveN(stacks, int(parsed[0]), int(parsed[1]) - 1, int(parsed[2]) - 1)
        printStacks(stacks)
    return "".join([x[-1] for x in stacks])


# %%
def executeMoves9001(moves, stacks):
    printStacks(stacks)
    for move in moves.splitlines():
        parsed = parse("move {} from {} to {}", move)
        print("moving {} from {} to {}".format(parsed[0], parsed[1], parsed[2]))
        moveN9001(stacks, int(parsed[0]), int(parsed[1]) - 1, int(parsed[2]) - 1)
        printStacks(stacks)
    return "".join([x[-1] for x in stacks])
