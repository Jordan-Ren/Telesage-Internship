import json
import xlrd
'''
TO USE REPLACE MODULE NAME AS WELL AS XLSX FILE PATHS.
REMOVE COMMENTS IN YML FILE BEFORE RUNNING, ADD BACK IN
AFTERWORDS.

This script adds descriptions to each item based on
if it has a description on the excell sheet or not.

Once finished running, copy and paste result into
the module file. You will then need to replace all
\\t and \\n with \t and \n.
'''

file_location = "C:\\Users\\jren\\Documents\\xcellDesc\\TOB.xlsx"

workbook = xlrd.open_workbook(file_location)

sheet = workbook.sheet_by_name('Sheet1')

descriptions = {}
#Creates a dictionary of item name -> value
for rownum in range(sheet.nrows):
    descriptions[sheet.cell_value(rownum, 0).lower()] = sheet.cell_value(rownum, 1)

with open('C:\git\ModuleFiles\DISC\Done\DISC_TOB_Youth_JSON_KE_4-18.yml', encoding='utf-8') as json_file:
    read_data = json_file.read()
    data = json.loads(read_data, strict=False)
#Finds the list of items
items = data["SubEntities"][0]["SubEntities"][0]["SubEntities"]

#less descriptions is usual, more descriptions is no issue.
print(len(descriptions), 'descriptions.')
print(len(items), 'items.')
#Adds descriptions for each item name if there is a description availible
for question in items:
    name = question["Name"]
    if name in descriptions:
        question["Properties"]["Description"] = descriptions[name]

final = json.dumps(data, indent=2, sort_keys=True)
print(final)
