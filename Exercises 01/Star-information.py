import numpy as np

infile = open("stars_data.txt", "r")
indata = infile.readlines()
infile.close()


n = len(indata)-1
for i in range(n):
    print(indata[i], "\n")
