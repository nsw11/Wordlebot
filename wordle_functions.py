import csv 

def read_csv(path,printresults= False): # reads a given csv file and formats it into an array, returns array
    output = []
    with open(path) as csvfile:    
        csvReader = csv.reader(csvfile)   
        for row in csvReader:
            output.append(row[0])
    if (printresults):
        print(output)
    print("read file of size "+ str(len(output)))
    print('FINISHED READING FILE '+ str(path))
    return output


def calc_avg(arr): #takes an array and calculates the average
    return sum(arr)/len(arr)

def calc_worst(arr):# the worst value should be the one with the least info gained
    return min(arr)
    