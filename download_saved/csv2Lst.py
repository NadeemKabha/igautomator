import csv
def CLConvert(csvFName:str):
    links=[]
    with open(csvFName, newline='') as csvfile:
        linksCSV = csv.reader(csvfile, delimiter=' ')
        for link in linksCSV:
            links.append(link[0])
    return links
def LCConvert(csvFName:str,links:list):
    with open(csvFName, "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        for link in links:
            writer.writerow([link])
def clean(csvFName:str):
    f = open(csvFName, "w")
    f.truncate()