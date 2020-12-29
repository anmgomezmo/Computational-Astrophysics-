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


def List_Order_Distance(array1,array2):
    outfile = open('List_Order_Distance.txt','w')
    headerstring = '# List of stars sorted by distance from the earth'
    outfile.write(headerstring)

    N = 11
    List = array2[:,0]
    for m in range(0,N):
        for n in range(0,N-1):
            d = List[n]
            d_f = List[n+1]
            if d<=d_f:
                List[n] = d
                List[n+1] = d_f
            else:
                List[n] = d_f
                List[n+1] = d

            aux = List[n]
            if m==N-1:
                outstring = f'\n {aux:.2f}'
                outfile.write(outstring)

    outfile.close()
    return List



data1 = np.genfromtxt("stars_data.txt", comments = "#", delimiter = ",", usecols = [0], dtype = "str")
data2 = np.loadtxt("stars_data.txt", comments = "#", delimiter = ",", usecols = [1,2,3])
print(data1, "\n", data2)
print(data1.shape,data2.shape)
print(List_Order_Distance(data1,data2))
