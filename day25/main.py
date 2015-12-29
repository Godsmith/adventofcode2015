__author__ = 'Filip'

code = 20151125

def next_code():
    global code
    code = (code * 252533) % 33554393
    return code

def get_number_from_coordinate(target_row, target_column):
    columns = [[20151125]]
    while True:
        columns.append([])
        for column in columns:
            column.append(next_code())
        if len(columns) >= target_column:
            if len(columns[target_column - 1]) >= target_row:
                return columns[target_column - 1][target_row - 1]

print get_number_from_coordinate(3010,3019)

