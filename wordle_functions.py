import csv 

def read_csv(path,printresults= False):
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