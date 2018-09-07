import csv

hypo = ['%','%','%','%','%','%']
with open("prog1_data") as csv_file:
    read_csv = csv.reader(csv_file, delimiter=",")
    data = []
    print("\nThe given examples are:")
    for row in read_csv:
        print(row)
        if(row[-1].upper() == "YES"):
            data.append(row)
    
    print("\nThe positive examples are")
    for x in data:
        print(x)
    
    print("\nApplying Find-S Algorithm\n")
    total = len(data)
    attr = len(data[0]) - 1
    temp_list = []
    # print("Total: " + str(total))
    # print("Attr: " + str(attr))
    for j in range(attr):
        temp_list.append(data[0][j])
    hypo = temp_list

    # print(hypo)

    for i in range(total):
        for k in range(attr):
            if(hypo[k] != data[i][k]):
                hypo[k] = '?'
        print(hypo)
    
    print("\nThe maximally specific Find-S hypothesis for the training given training examples is:")
    print(hypo)
