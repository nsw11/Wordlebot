import csv 

def read_csv(path,printresults= False): # reads a given csv file and formats it into an array, returns array
# guidence for this function provided by https://www.folkstalk.com/2022/10/python-read-csv-into-array-with-code-examples.html
    output = []
    with open(path) as csvfile:    
        csvReader = csv.reader(csvfile,delimiter=',')   
        for row in csvReader:
            output.append(row[0])
    if (printresults):
        print(output)
    print("read file of size "+ str(len(output)))
    print(' FINISHED READING FILE '+ str(path))
    return output

def write_csv(path,list):
    with open(path,"w",newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        for i in range(len(list)):
            csvwriter.writerow(list[i])
    print("Finished writing file "+path +" with "+  str(len(list)) + " elements")
            

def calc_avg(arr): #takes an array and calculates the average
    return sum(arr)/len(arr)

def calc_worst(arr):# the worst value should be the one with the least info gained
    return min(arr)
    