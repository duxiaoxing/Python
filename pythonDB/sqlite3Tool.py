# encoding:utf-8

import sqlite3
from xlrd import open_workbook
import types

db_file_name = 'exception.db'
db_table_name = 'Exceptions'
xls_file_name = 'exception.xls'

request_title_index = 0
emergency_index = 1
staff_number_index = 2
staff_name_index = 3
staff_apartment_index = 4
request_date_index = 5
entourage_persons_index = 6
request_reason_index = 7
go_to_out_date_index = 8
go_to_out_date_start_index = 9
go_to_out_date_end_index = 10
remarks_index = 11
destination_index = 12


# 创建table
def sql_create_table(table_string):
    conn = sqlite3.connect(db_file_name)
    cursor = conn.cursor()
    cursor.execute(table_string)
    conn.commit()
    cursor.close()


# 插入数据
def insert():
    wb = open_workbook(xls_file_name)
    conn = sqlite3.connect(db_file_name)
    c = conn.cursor()
    for s in wb.sheets():
        for row in range(s.nrows):
            values = []
            for col in range(s.ncols):
                value = s.cell(row, col).value
                if value:
                    value = unicode(value)
                    # if type(value) is types.UnicodeType:
                    #     value = value.encode('utf-8')
                else:
                    value = 'null'
                values.append(value)
            print values
            c.execute(
                "INSERT INTO Exceptions(request_title,emergency,staff_number,staff_name,staff_apartment,request_date,entourage_persons,request_reason,go_to_out_date,go_to_out_date_start,go_to_out_date_end,remarks,destination) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)",
                values)
            conn.commit()


            # insert_string =
            # print insert_string


            # request_title = s.cell(row, request_title_index).value
            # values.append(request_title)
            # emergency = s.cell(row, emergency_index).value
            # values.append(emergency)
            # staff_number = s.cell(row, staff_number_index).value
            # values.append(staff_number)
            # staff_name = s.cell(row, staff_name_index).value
            # values.append(staff_name)
            # staff_apartment = s.cell(row, staff_apartment_index).value
            # values.append(staff_apartment)
            # request_date = s.cell(row, request_date_index).value
            # values.append(request_date)
            # entourage_persons = s.cell(row, entourage_persons_index).value
            # values.append(entourage_persons)
            # go_to_out_date = s.cell(row, go_to_out_date_index).value
            # values.append(go_to_out_date)
            # go_to_out_date_start = s.cell(row, go_to_out_date_start_index).value
            # values.append(go_to_out_date_start)
            # go_to_out_date_end = s.cell(row, go_to_out_date_end_index).value
            # values.append(go_to_out_date_end)
            # remarks = s.cell(row, remarks_index).value
            # values.append(remarks)
            # destination = s.cell(row, destination_index).value
            # values.append(destination)
            # insert_string = "INSERT INTO Exceptions VALUES (?,?,?,?,?,?,?,?,?,?,?,?)", values
            # print insert_string
            # c.execute(insert_string)
            # conn.commit()


# 查询记录
def search(staff_apartment, staff_name, go_to_out_date):
    conn = sqlite3.connect(db_file_name)
    conn.text_factory = str
    c = conn.cursor()
    # staff_apartment_unicode = unicode(staff_apartment)
    # print staff_apartment_unicode
    # staff_name_unicode = unicode(staff_name)
    # go_to_out_date_unicode = unicode(go_to_out_date)
    c.execute(
        "select * from Exceptions where staff_apartment=:staff_apartment and staff_name=:staff_name AND go_to_out_date=:go_to_out_date",
        {"staff_apartment": staff_apartment, "staff_name": staff_name,
         "go_to_out_date": go_to_out_date})
    # c.execute(
    #     "select * from Exceptions where staff_name=:staff_name",
    #     {"staff_name":staff_name})
    for row in c:
        print row[go_to_out_date_index]
    conn.close()

create_table_string = '''
                         CREATE TABLE IF NOT EXISTS Exceptions
                      (
                         request_title TEXT,
                         emergency TEXT,
                         staff_number TEXT,
                         staff_name TEXT,
                         staff_apartment TEXT,
                         request_date TEXT,
                         entourage_persons TEXT,
                         request_reason TEXT,
                         go_to_out_date TEXT,
                         go_to_out_date_start TEXT,
                         go_to_out_date_end TEXT,
                         remarks TEXT,
                         destination TEXT
                        )'''

sql_create_table(create_table_string)
insert()

search('力芯科技', '季育武', '2016-07-13')
