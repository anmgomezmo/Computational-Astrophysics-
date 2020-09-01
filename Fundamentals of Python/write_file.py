import numpy as np

# open the file for writting
outfile = open("out_file1.txt","w")

# writting a header
headerstring = "# This is the header for the file"
outfile.write(headerstring)

# write n lines of data
n = 100
for i in range(n):
    rand1 = np.random.random()
    rand2 = np.random.random()
    outstring = f"\n{rand1:.10f} , {rand2:.10f}"
    outfile.write(outstring)

# close the file
outfile.close()

print("\n\n")

import numpy as np

data = np.random.random([50,2])

np.savetxt("out_file2.txt", data, fmt = "%5.5f",
header = "This is the headerof the file")

np.savetxt("out_file3.txt", data, delimiter = ",", fmt = "%5.5f",
header = "This is the headerof the file")
