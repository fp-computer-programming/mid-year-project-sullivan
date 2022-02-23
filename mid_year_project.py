# Author: CRS 02/10/22
import random
def chutes_and_ladders():
    chutes1 = random.randint(1, 6)
    chutes2 = random.randint(1, 6)
    chutes3 = random.randint(1, 6)
    ladders1 = random.randint(1, 6)
    ladders2 = random.randint(1, 6)
    ladders3 = random.randint(1, 6)
    if ladders1 == chutes1 & chutes1 != 6:
        ladders1 += 1
    else: ladders1 -= 1
    if ladders1 == chutes2 & chutes2 != 6:
        ladders1 += 1
    else: ladders1 -= 1
    if ladders1 == chutes3 & chutes3 != 6:
        ladders1 += 1
    else: ladders1 -= 1
    
    dice_roll = int(input("Pick a number between 1 and 6."))

chutes_and_ladders()