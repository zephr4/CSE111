import xlrd

loc = ("file destination")
 
wb = xlrd.open_workbook(loc)
sheet = wb.sheet_by_index(0)
 
# For row 0 and column 0 example
print(sheet.cell_value(0, 0))