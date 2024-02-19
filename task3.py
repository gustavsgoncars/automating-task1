import selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
from openpyxl import Workbook, load_workbook 
import pandas as pd

service = Service()
option = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=option)

name=[]
# program read information from people.csv file and put all data in name list.
with open("people.csv", "r") as file:
    next(file)
    for line in file:
        row=line.rstrip().split(",") 
        name.append(row[2] + " " + row[3])

url = "https://emn178.github.io/online-tools/crc32.html"
driver.get(url)
time.sleep(2)

encr=[]

for x in name:
    find = driver.find_element(By.ID, "input")
    find.clear()
    find.send_keys(x)

    find = driver.find_element(By.ID, "output")
    temp = find.get_attribute("value")
    encr.append(temp)

input()

file2 = pd.read_excel("salary.xlsx", sheet_name="Sheet2")
info_list = file2.values.tolist()

employee = input()
i = 0
for n in name:
    if (employee == n):
        i=name.index(employee)
        break

nencr=encr[i]

salary=[]

for s in info_list:
    if nencr == s[0]:
        salary1 = s[1]
        salary.append(salary1)

print(sum(salary))
