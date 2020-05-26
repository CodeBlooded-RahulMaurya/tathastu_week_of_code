def remDuplicate(string):
    reqString = ""
    for x in reqString:
        if x not in reqString:
            reqString += x
    return reqString

string = input("Enter the string: ")
print("String after removing the duplicates is:", remDuplicate(string))