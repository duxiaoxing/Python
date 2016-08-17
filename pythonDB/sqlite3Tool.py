# encoding:UTF-8

import sqlite3
from xlrd import open_workbook
from xlwt import Workbook, easyxf, Style, XFStyle
from tempfile import TemporaryFile
import types

db_file_name = 'exception.db'
db_table_name = 'Exceptions'
xls_file_name = 'exception.xls'
xls_file_allStaffs = 'simple.xls'

# 请求标题
request_title_index = 0
emergency_index = 1
staff_number_index = 2
staff_name_index = 3
staff_apartment_index = 4
request_date_index = 5
entourage_persons_index = 6
request_reason_index = 7
go_to_out_date_index = 8
# 外出开始时间
go_to_out_date_start_index = 9
# 外出结束时间
go_to_out_date_end_index = 10
# 备注
remarks_index = 11
# 外出目的地
destination_index = 12

# 每月天数 默认index = 0
days_in_month = 31


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
    rows = []
    conn = sqlite3.connect(db_file_name)
    conn.text_factory = str
    c = conn.cursor()
    # staff_apartment_unicode = unicode(staff_apartment)
    # print staff_apartment_unicode
    # staff_name_unicode = unicode(staff_name)
    # go_to_out_date_unicode = unicode(go_to_out_date)
    # c.execute(
    #     ''"select * from Exceptions where staff_apartment=:staff_apartment and staff_name=:staff_name AND go_to_out_date=:go_to_out_date",
    #     {"staff_apartment": staff_apartment, "staff_name": staff_name,
    #      "go_to_out_date": go_to_out_date})
    c.execute(
        ''"select * from Exceptions where  staff_name=:staff_name AND go_to_out_date=:go_to_out_date",
        {"staff_name": staff_name,
         "go_to_out_date": go_to_out_date})
    # c.execute(
    #     "select * from Exceptions where staff_name=:staff_name",
    #     {"staff_name":staff_name})
    for row in c:
        rows.append(row)
    conn.close()
    return rows


# 所有员工姓名

def all_staffs_name(file_name):
    wb = open_workbook(file_name)
    sheet_name_0 = wb.sheets()[0]
    all_staffs_name_array = []
    all_staffs_name_set = set()
    for row in range(sheet_name_0.nrows):
        values = []
        for col in range(sheet_name_0.ncols):
            value = sheet_name_0.cell(row, col).value
            staff_name = sheet_name_0.cell(row, 1).value
            if len(staff_name) > 0:
                all_staffs_name_set.add(staff_name)
                # print type(staff_name)
                if staff_name in all_staffs_name_array:
                    # print '已包含:' + staff_name
                    pass
                else:
                    all_staffs_name_array.append(staff_name)
            if isinstance(value, float):
                value = str(value)
            values.append(value)
            # print ','.join(values)
    # print all_staffs_name_set
    # print len(all_staffs_name_set)
    # print len(all_staffs_name_array)
    all_staffs_name_array.pop(0)
    return all_staffs_name_array
    # for name in all_staffs_name_array:
    #     print name


# 判断是否迟到 08:59
def be_late(time_string):
    hour_and_second_array = time_string.split(':')
    hou_string = hour_and_second_array[0]
    second_string = hour_and_second_array[-1]
    late = 0
    if int(hou_string) < 9:
        late = 1
    else:
        late = 0

    return late


# 判断是否早退
def leave_early(time_string):
    hour_and_second_array = time_string.split(':')
    hou_string = hour_and_second_array[0]
    second_string = hour_and_second_array[-1]
    early = 0
    if int(hou_string) >= 18:
        early = 1
    else:
        early = 0

    return early


def create_excel_file():
    all_staffs_excel = Workbook(encoding='utf-8')
    sheet_one = all_staffs_excel.add_sheet('7月份出勤明细')
    all_staffs_excel.save('all_staffs.xls')
    all_staffs_excel.save(TemporaryFile())


all_staffs__name_array = all_staffs_name(xls_file_allStaffs)

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

# sql_create_table(create_table_string)
# insert()

search('力芯科技', '季育武', '2016-07-13')

# create_excel_file()

all_staffs_name_index = 1
all_staffs_date_index = 2
all_staffs_sign_in_date = 4
all_staffs_sign_in_date_description = 5
all_staffs_sign_out_date = 6
all_staffs_sign_out_date_description = 7
all_staffs_entourage_persons_index = 8

all_staffs_excel = Workbook(encoding='utf-8')
sheet_one = all_staffs_excel.add_sheet('7月份出勤明细')
sheet_one.write(0, all_staffs_name_index, '姓名')
sheet_one.write(0, all_staffs_date_index, '日期')
sheet_one.write(0, all_staffs_sign_in_date, '签到时间')
sheet_one.write(0, all_staffs_sign_in_date_description, '上班描述')
sheet_one.write(0, all_staffs_sign_out_date, '签退时间')
sheet_one.write(0, all_staffs_sign_out_date_description, '下班描述')
sheet_one.write(0, all_staffs_entourage_persons_index, '随行人员')
excel_row = 0

for staff_name in all_staffs__name_array:
    for day_in_month_index in list(range(days_in_month)):
        go_to_out_date_string = '2016-07-%02d' % (day_in_month_index + 1)
        rows = search('力芯科技', staff_name, go_to_out_date_string)
        go_to_out_date_start_time_array = []
        go_to_out_date_end_time_array = []
        excel_row = excel_row + 1
        print 'excel_row: ' + str(excel_row)
        sheet_one.write(excel_row, all_staffs_name_index, staff_name)
        sheet_one.write(excel_row, all_staffs_date_index, go_to_out_date_string)
        if len(rows) > 0:
            for row in rows:
                go_to_out_date_start_time = row[go_to_out_date_start_index]
                go_to_out_date_end_time = row[go_to_out_date_end_index]
                go_to_out_date_start_time_array.append(go_to_out_date_start_time)
                go_to_out_date_end_time_array.append(go_to_out_date_end_time)
            go_to_out_date_start_time_array.sort()
            go_to_out_date_end_time_array.sort()
            go_to_out_date_start_time_start = go_to_out_date_start_time_array[0]
            go_to_out_date_end_time_end = go_to_out_date_end_time_array[-1]

            entourage_persons = row[entourage_persons_index]
            if len(entourage_persons) > 0 and entourage_persons != 'null':
                sheet_one.write(excel_row, all_staffs_entourage_persons_index, entourage_persons)
            # print staff_name + ' ' + go_to_out_date_string + ' ' + go_to_out_date_start_time_start
            # print staff_name + ' ' + go_to_out_date_string + ' ' + go_to_out_date_end_time_end
            if be_late(go_to_out_date_start_time_start):
                print '早晨未打卡直接出差'
                sheet_one.write(excel_row, all_staffs_sign_in_date, go_to_out_date_start_time_start)
                sheet_one.write(excel_row, all_staffs_sign_in_date_description, '外出')
            else:
                print '早晨打卡后直接出差'
            if leave_early(go_to_out_date_end_time_end):
                print '出差结束时间未归公司'
                sheet_one.write(excel_row, all_staffs_sign_out_date, go_to_out_date_end_time_end)
                sheet_one.write(excel_row, all_staffs_sign_out_date_description, '外出')
            else:
                print '出差结束后归公司'

                # if be_late(go_to_out_date_start_time):
                #     print '早晨未打卡直接出差'
                # else:
                #     print '早晨打卡后直接出差'
                # if leave_early(go_to_out_date_end_time):
                #     print '出差结束时间未归公司'
                # else:
                #     print '出差结束后归公司'
                # for row in rows:
                #     go_to_out_date_start_time = row[go_to_out_date_start_index]
                #     go_to_out_date_end_time = row[go_to_out_date_end_index]
                #     if be_late(go_to_out_date_start_time):
                #         print '早晨未打卡直接出差'
                #     else:
                #         print '早晨打卡后直接出差'
                #     if leave_early(go_to_out_date_end_time):
                #         print '出差结束时间未归公司'
                #     else:
                #         print '出差结束后归公司'

all_staffs_excel.save('all_staffs.xls')
all_staffs_excel.save(TemporaryFile())
