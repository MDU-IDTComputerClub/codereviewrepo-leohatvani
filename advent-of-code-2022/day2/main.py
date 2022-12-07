# Rock Paper Scissors is a game between two players.
# Each game contains many rounds; in each round,
# the players each simultaneously choose one of
# Rock, Paper, or Scissors using a hand shape.
# Then, a winner for that round is selected:
# - (X) Rock defeats (C) Scissors,
# - (Z) Scissors defeats (B) Paper, and
# - (Y) Paper defeats (A) Rock.
# If both players choose the same shape,
# the round instead ends in a draw.

# Your total score is the sum of your scores for each round.
# The score for a single round is the score for the shape you selected
# (1 for Rock, 2 for Paper, and 3 for Scissors)
# plus the score for the outcome of the round
# (0 if you lost, 3 if the round was a draw, and 6 if you won).
# %% [markdown] # Part 2
#%%
rowToScore = {
    "A X": 3 + 1,
    "A Y": 6 + 2,
    "A Z": 0 + 3,
    "B X": 0 + 1,
    "B Y": 3 + 2,
    "B Z": 6 + 3,
    "C X": 6 + 1,
    "C Y": 0 + 2,
    "C Z": 3 + 3,
}
#%%
with open("input", "r") as f:
    rows = [x.strip() for x in f.readlines()]

# %% [markdown] # Part 2
# X means you need to lose,
# Y means you need to end the round in a draw, and
# Z means you need to win
# %%
print(sum([rowToScore[row] for row in rows]))
# %%
rowToScore2 = {
    "A X": 0 + 3,
    "A Y": 3 + 1,
    "A Z": 6 + 2,
    "B X": 0 + 1,
    "B Y": 3 + 2,
    "B Z": 6 + 3,
    "C X": 0 + 2,
    "C Y": 3 + 3,
    "C Z": 6 + 1,
}
#%%
print(sum([rowToScore2[row] for row in rows]))

# %%
