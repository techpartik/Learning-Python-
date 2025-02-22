import os

for i in range(0,100):
    os.rename(f"data/month{i+1}", f"data/day{i+1}")


import os
folder=os.listdir()
print(folder)