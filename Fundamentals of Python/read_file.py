infile = open("example_file1.txt","r")
data1 = infile.readlines()
infile.close()
print(data1, "\n")

import numpy as np

infile1 = open("example_file2.txt","r")
indata = infile1.readlines()
infile1.close()
print(indata)

n = len(indata) - 1
time = np.zeros(n)
data = np.zeros(n)

for i in range(n):
    splitline = indata[i+1][:-1].split(",")
    time[i] = float(splitline[0])
    data[i] = float(splitline[1])

print(time, "\n", data, "\n\n")

import numpy as np

data2 = np.loadtxt("example_file3.txt", comments = "#")
print(data2, "\n", data2[:,0], "\n", data2[:,1])
