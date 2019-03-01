import pandas as pd
import sys

print("Welcome to the Best Set Generator!\n")
filename = input("Please provide an inventory list: ")

file = open(filename, 'r')
title = file.readline()
titles = title.split(" ");
header_list = []
for t in titles:
	header_list.append(t)
len = len(header_list)
if len > 4 or len <= 0:
	sys.exit("Error: Expected 4 Categories.")

type = titles[0]
name = titles[1]
price = titles[2]
value = titles[3]
gold = 300

store = pd.read_table(file, names = header_list, sep =" ")

head = pd.DataFrame(columns = header_list)
top = pd.DataFrame(columns = header_list)
bottom = pd.DataFrame(columns = header_list)
feet = pd.DataFrame(columns = header_list)

head_list = []
top_list = []
bottom_list = []
feet_list = []

for index, row in store.iterrows():
	if row[type] == "Helmet":
		head_list.append(row)
	elif row[type] == "Chest":
		top_list.append(row)
	elif row[type] == "Leggings":
		bottom_list.append(row)
	elif row[type] == "Boots":
		feet_list.append(row)
	else:
		sys.exit("Error: Unexpected Armor Labels")

head = pd.DataFrame(head_list, columns = header_list)
top = pd.DataFrame(top_list, columns = header_list)
bottom = pd.DataFrame(bottom_list, columns = header_list)
feet = pd.DataFrame(feet_list, columns = header_list)

print(store)
print(head)
print(top)
print(bottom)
print(feet)


