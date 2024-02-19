import pandas as pd

get_info=input()

fails = pd.read_excel("description.xlsx", sheet_name="LookupAREA")
info_list = fails.values.tolist()

region=[]

for x in range (len(info_list)):
    i=info_list[x][1]
    if i==get_info:
        reg_name=info_list[x][0]
        break
else:
    print(0)
    exit(0)

with open("data.csv","r") as f:
    next(f)
    for line in f:
        row=line.rstrip().split(",")
        if row[1]==reg_name:
            region.append(int(row[3]))

print(sum(region))