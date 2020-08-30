# Using Map method to get list input based on spaces in input
n = int(input())
scoresheet = list(map(int, input().split()[:n]))
maxscore = max(scoresheet)
while maxscore == max(scoresheet):
    scoresheet.remove(maxscore)
runnerscore = max(scoresheet)
print(runnerscore)
