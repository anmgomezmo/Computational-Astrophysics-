import numpy as np

#infile = open("stars_data.txt", "r")
#indata = infile.readlines()
#infile.close()


#n = len(indata)-1
#for i in range(n):
    #print(indata[i], "\n")

#Starname = np.array(n)
#Stardistance = np.zeros(n)
#Starluminosity = np.zeros(n)

#for i in range(n):
#    splitline = indata[i+1][:-1].split(",")
#    Starname[i] = splitline[0]
#    Stardistance[i] = float(splitline[1])
#    Starluminosity[i] = float(splitline[3])


#print(Starname, "\n", Stardistance, "\n", Starluminosity, "\n\n")

data1 = np.loadtxt("stars_data.txt", comments = "#",
delimiter = ",", usecols = [1,2,3])
data2 = np.genfromtxt("stars_data.txt", comments = "#",
delimiter = ",", usecols = [0], dtype = "str")
print(data1, "\n", data2)
