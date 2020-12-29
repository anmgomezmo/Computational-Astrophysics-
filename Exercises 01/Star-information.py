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
    headerstring = '# List of stars sorted by distance from the earth \n'
    outfile.write(headerstring)

    N = 11
    List = array2[:,0]
    Names = array1
    for m in range(0,N):
        for n in range(0,N-1):
            d = List[n]
            d_f = List[n+1]
            Na = Names[n]
            Na_f = Names[n+1]
            if d<=d_f:
                List[n] = d
                List[n+1] = d_f
                Names[n] = Na
                Names[n+1] = Na_f
            else:
                List[n] = d_f
                List[n+1] = d
                Names[n] = Na_f
                Names[n+1] = Na

    for n in range(0,N):
        outstring = f' , {List[n]:.2f} \n'
        outfile.write(Names[n])
        outfile.write(outstring)

    outfile.close()
    return List


def List_Order_Luminosity(array1,array2):
    outfile = open('List_Order_Luminosity.txt','w')
    headerstring = '# List of stars sorted by luminosity from the earth \n'
    outfile.write(headerstring)

    N = 11
    List = array2[:,2]
    Names = array1
    for m in range(0,N):
        for n in range(0,N-1):
            d = List[n]
            d_f = List[n+1]
            Na = Names[n]
            Na_f = Names[n+1]
            if d<=d_f:
                List[n] = d
                List[n+1] = d_f
                Names[n] = Na
                Names[n+1] = Na_f
            else:
                List[n] = d_f
                List[n+1] = d
                Names[n] = Na_f
                Names[n+1] = Na

    for n in range(0,N):
        outstring = f' , {List[n]:.2e} \n'
        outfile.write(Names[n])
        outfile.write(outstring)

    outfile.close()
    return List



data1 = np.genfromtxt("stars_data.txt", comments = "#", delimiter = ",", usecols = [0], dtype = "str")
data2 = np.loadtxt("stars_data.txt", comments = "#", delimiter = ",", usecols = [1,2,3])
print(data1, "\n", data2)
print(data1.shape,data2.shape)
print(List_Order_Distance(data1,data2))
print(List_Order_Luminosity(data1,data2))
