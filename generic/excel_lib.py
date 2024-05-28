import xlrd


def read_locators(sheetname):
	file_path = r"C:\Users\Vidyashree M C\demo_project\POM\locators.xlsx"
	xlrd.xlsx.ensure_elementtree_imported(False, None)
	xlrd.xlsx.Element_has_iter = True
	wb = xlrd.open_workbook(file_path)
	ws = wb.sheet_by_name(sheetname)
	# rows = ws.get_rows()       # returns generator object
	# data = {}
	# for row in rows:
	# 	data[row[0].value] = (row[1].value, row[2].value)

	# data = {row[0].value: (row[1].value, row[2].value) for row in rows}
	# print(data)

	rows = ws.nrows
	data = {}
	for i in range(rows):
		row_element = ws.row_values(i)
		data[row_element[0]] = (row_element[1], row_element[2])

	return data
