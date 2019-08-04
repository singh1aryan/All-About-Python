import csv

with open('congress_train.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    columns = []
    for row in csv_reader:
        columns.append(row)
        
    print(columns[1][1])
    print(len(columns))
    
    
'''
we can calssify them into yea and naa
and also classfiy them into democrats and republic


'''