# encoding:utf-8
from xlrd import open_workbook

# wb = open_workbook('simple.xls')
# for s in wb.sheets():
#     print 'Sheet:', s.name
#     for row in range(s.nrows):
#         values = []
#         for col in range(s.ncols):
#             value = s.cell(row, col).value
#             if (isinstance(value, float)):
#                 value = str(value)
#             values.append(value)
#         print ','.join(values)
# print
#


from xlrd import open_workbook, cellname, XL_CELL_TEXT, cellname, cellnameabs, colname, empty_cell
from tempfile import TemporaryFile
from xlwt import Workbook

file_name = 'simple1.xls'


# # Sheet_name
# wb = open_workbook('simple.xls')
# for sheet_name in wb.sheets():
#     print 'sheet_name:' + sheet_name.name


# # all_values
# wb = open_workbook('simple.xls')
# sheet_name_0 = wb.sheets()[0]
# for row in range(sheet_name_0.nrows):
#     values = []
#     for col in range(sheet_name_0.ncols):
#         value = sheet_name_0.cell(row, col).value
#         if isinstance(value, float):
#             value = str(value)
#         values.append(value)
#     print ','.join(values)
#
#
# # 写文件
# book = Workbook(encoding='utf-8')
# sheet1 = book.add_sheet('Sheet 1')
# book.add_sheet('Sheet 2')
# sheet1.write(0,0,'A1')
# sheet1.write(0,1,'B1')
# row1 = sheet1.row(1)
# row1.write(0,'A2')
# row1.write(1,'B2')
# sheet1.col(0).width = 10000
# sheet2 = book.get_sheet(1)
# sheet2.row(0).write(0,'Sheet 2 A1')
# sheet2.row(0).write(1,'Sheet 2 B1')
# sheet2.flush_row_data()
# sheet2.write(1,0,'Sheet 2 A3')
# sheet2.col(0).width = 5000
# sheet2.col(0).hidden = True
# book.save('demo.xls')
# book.save(TemporaryFile())


# for sheet_name in wb.sheets():
#     for row in range(sheet_name.nrows):
#         values = []
#         for col in range(sheet_name.ncols):
#             value = sheet_name.cell(row, col).value
#             if isinstance(value, float):
#                 value = str(value)
#             values.append(value)
#         print ','.join(values)

# # cell_name,value
# book = open_workbook(file_name)
# sheet = book.sheet_by_index(0)
# rows = sheet.nrows
# cols = sheet.ncols
# print 'sheet_name:' + sheet.name + '\n' + 'rows:' + str(rows) + '\n' + 'cols:' + str(cols)
# for row_index in range(sheet.nrows):
#     for col_index in range(sheet.ncols):
#         cell_name = cellname(row_index, col_index)
#         value = sheet.cell(row_index, col_index).value
#         if isinstance(value, float):
#             value = str(value)
#         print 'cell_name:' + cell_name + '  value:' + value


# 判断类型
# book = open_workbook(file_name)
# sheet = book.sheet_by_index(0)
# cell = sheet.cell(0, 0)
# print cell
# print cell.value
# print cell.ctype == XL_CELL_TEXT
# for i in range(sheet.ncols):
#     print sheet.cell_type(1, i), sheet.cell_value(1, i)

# 判断类型,暂时未用到
# book = open_workbook('simple.xls')
# sheet0 = book.sheet_by_index(0)
# # sheet1 = book.sheet_by_index(1)
# print sheet0.row(0)
# print sheet0.col(0)
# print
# print sheet0.row_slice(0, 1)
# print sheet0.row_slice(0, 1, 2)
# print sheet0.row_values(0, 1)
# print sheet0.row_values(0, 1, 2)
# print sheet0.row_types(0, 1)
# print sheet0.row_types(0, 1, 2)

# print 'empty_cell: ' + empty_cell.value

def cell_contents(sheet, row_x):
    result = []
    for col_x in range(2, sheet.ncols):
        cell = sheet.cell(row_x, col_x)
        result.append((cell.ctype, cell, cell.value))
    return result


# sheet = open_workbook(file_name).sheet_by_index(0)
# print 'XL_CELL_TEXT', cell_contents(sheet, 2)
# print 'XL_CELL_NUMBER', cell_contents(sheet, 2)
# print 'XL_CELL_DATE', cell_contents(sheet, 3)
# print 'XL_CELL_BOOLEAN', cell_contents(sheet, 4)
# print 'XL_CELL_ERROR', cell_contents(sheet, 5)
# print 'XL_CELL_BLANK', cell_contents(sheet, 6)
# print 'XL_CELL_EMPTY', cell_contents(sheet, 7)
# print
# sheet = open_workbook(
#     file_name, formatting_info=True
# ).sheet_by_index(0)
# print 'XL_CELL_TEXT', cell_contents(sheet, 1)
# print 'XL_CELL_NUMBER', cell_contents(sheet, 2)
# print 'XL_CELL_DATE', cell_contents(sheet, 3)
# print 'XL_CELL_BOOLEAN', cell_contents(sheet, 4)
# print 'XL_CELL_ERROR', cell_contents(sheet, 5)
# print 'XL_CELL_BLANK', cell_contents(sheet, 6)
# print 'XL_CELL_EMPTY', cell_contents(sheet, 7)

# 写文件
# book = Workbook(encoding='utf-8')
# sheet1 = book.add_sheet('Sheet 1')
# book.add_sheet('Sheet 2')
# sheet1.write(0,0,'A1')
# sheet1.write(0,1,'B1')
# row1 = sheet1.row(1)
# row1.write(0,'A2')
# row1.write(1,'B2')
# sheet1.col(0).width = 10000
# sheet2 = book.get_sheet(1)
# sheet2.row(0).write(0,'Sheet 2 A1')
# sheet2.row(0).write(1,'Sheet 2 B1')
# sheet2.flush_row_data()
# sheet2.write(1,0,'Sheet 2 A3')
# sheet2.col(0).width = 5000
# sheet2.col(0).hidden = True
# book.save('demo.xls')
# book.save(TemporaryFile())

from datetime import date, time, datetime
from decimal import Decimal
from xlwt import Workbook, Style

# wb = Workbook()
# ws = wb.add_sheet('Type examples')
# ws.row(0).write(0, u'\xa3')
# ws.row(0).write(1, 'Text')
# ws.row(1).write(0, 3.1415)
# ws.row(1).write(1, 15)
# ws.row(1).write(2, 265L)
# ws.row(1).write(3, Decimal('3.65'))
# ws.row(2).set_cell_number(0, 3.1415)
# ws.row(2).set_cell_number(1, 15)
# ws.row(2).set_cell_number(2, 265L)
# ws.row(2).set_cell_number(3, Decimal('3.65'))
# ws.row(3).write(0, date(2009, 3, 18))
# ws.row(3).write(1, datetime(2009, 3, 18, 17, 0, 1))
# ws.row(3).write(2, time(17, 1))
# ws.row(4).set_cell_date(0, date(2009, 3, 18))
# ws.row(4).set_cell_date(1, datetime(2009, 3, 18, 17, 0, 1))
# ws.row(4).set_cell_date(2, time(17, 1))
# ws.row(5).write(0, False)
# ws.row(5).write(1, True)
# ws.row(6).set_cell_boolean(0, False)
# ws.row(6).set_cell_boolean(1, True)
# ws.row(7).set_cell_error(0, 0x17)
# ws.row(7).set_cell_error(1, '#NULL!')
#
# format = wb.add_format()
#
# format.set_font_color('red')
#
# wb.write(0, 0, 'wheelbarrow', format)

# ws.row(8).write(
#     0, '', Style.easyxf('pattern: pattern solid, fore_colour
# green;
# '))
# ws.row(8).write(
#     1, None, Style.easyxf('pattern: pattern solid, fore_colour
# blue;
# '))
# ws.row(9).set_cell_blank(
#     0, Style.easyxf('pattern: pattern solid, fore_colour
# yellow;
# '))
# ws.row(10).set_cell_mulblanks(
#     5, 10, Style.easyxf('pattern: pattern solid, fore_colour
# red;
# ') )
# wb.save('types.xls')


# from datetime import date
# from xlwt import Workbook, XFStyle, Borders, Pattern, Font
# fnt = Font()
# fnt.name = 'Arial'
# borders = Borders()
# borders.left = Borders.THICK
# borders.right = Borders.THICK
# borders.top = Borders.THICK
# borders.bottom = Borders.THICK
# pattern = Pattern()
# pattern.pattern = Pattern.SOLID_PATTERN
# pattern.pattern_fore_colour = 0x0A
# style = XFStyle()
# style.num_format_str='YYYY-MM-DD'
# style.font = fnt
# style.borders = borders
# style.pattern = pattern
# book = Workbook()
# sheet = book.add_sheet('A Date')
# sheet.write(1,1,date(2009,3,18),style)
# book.save('date.xls')


# from xlwt import Workbook, easyxf
#
# style1 = easyxf('font: name Times New Roman')
# style2 = easyxf('font: name Times New Roman')
# style3 = easyxf('font: name Times New Roman')
#
#
# def write_cells(book):
#     sheet = book.add_sheet('Content')
#     sheet.write(0, 0, 'A1', style1)
#     sheet.write(0, 1, 'B1', style2)
#     sheet.write(0, 2, 'C1', style3)
#
#
# book = Workbook()
# write_cells(book)
# book.save('3xf3fonts.xls')
# book = Workbook(style_compression=1)
# write_cells(book)
# book.save('3xf1font.xls')
# book = Workbook(style_compression=2)
# write_cells(book)
# book.save('1xf1font.xls')


# from xlwt import Workbook, Formula
# book = Workbook()
# sheet1 = book.add_sheet('Sheet 1')
# sheet1.write(0,0,10)
# sheet1.write(0,1,20)
# sheet1.write(1,0,Formula('A1/B1'))
# sheet2 = book.add_sheet('Sheet 2')
# row = sheet2.row(0)
# row.write(0,Formula('sum(1,2,3)'))
# row.write(1,Formula('SuM(1;2;3)'))
# row.write(2,Formula("$A$1+$B$1*SUM('ShEEt 1'!$A$1:$b$2)"))
# book.save('formula.xls')


# from xlwt import Utils
#
# print 'AA ->', Utils.col_by_name('AA')
# print 'A ->', Utils.col_by_name('A')
# print 'A1 ->', Utils.cell_to_rowcol('A1')
# print '$A$1 ->', Utils.cell_to_rowcol('$A$1')
# print 'A1 ->', Utils.cell_to_rowcol2('A1')
# print (0, 0), '->', Utils.rowcol_to_cell(0, 0)
# print (0, 0, False, True), '->',
# print Utils.rowcol_to_cell(0, 0, False, True)
# print (0, 0, True, True), '->',
# print Utils.rowcol_to_cell(
#     row=0, col=0, row_abs=True, col_abs=True
# )
# print '1:3 ->', Utils.cellrange_to_rowcol_pair('1:3')
# print 'B:G ->', Utils.cellrange_to_rowcol_pair('B:G')
# print 'A2:B7 ->', Utils.cellrange_to_rowcol_pair('A2:B7')
# print 'A1 ->', Utils.cellrange_to_rowcol_pair('A1')
# print (0, 0, 100, 100), '->',
# print Utils.rowcol_pair_to_cellrange(0, 0, 100, 100)
# print (0, 0, 100, 100, True, False, False, False), '->',
# print Utils.rowcol_pair_to_cellrange(
#     row1=0, col1=0, row2=100, col2=100,
#     row1_abs=True, col1_abs=False,
#     row2_abs=False, col2_abs=True
# )
# for name in (
#         '', "'quoted'", "O'hare", "X" * 32, "[]:\\?/*\x00"
# ):
#     print 'Is %r a valid sheet name?' % name,
#     if Utils.valid_sheet_name(name):
#         print "Yes"
#     else:
#         print "No"
#
# from xlwt import Workbook
#
# w = Workbook()
# ws = w.add_sheet('Normal')
# ws.write(0, 0, 'Some text')
# ws.normal_magn = 75
# ws = w.add_sheet('Page Break Preview')
# ws.write(0, 0, 'Some text')
# ws.preview_magn = 150
# ws.page_preview = True
# w.save('zoom.xls')




import datetime
import time
import string

import xlwt

#
# style = xlwt.XFStyle()
# pattern = xlwt.Pattern()
# pattern.pattern = xlwt.Pattern.SOLID_PATTERN
# pattern.pattern_fore_colour = xlwt.Style.colour_map['dark_purple']
# style.pattern = pattern


# all_values
wb = open_workbook('simple.xls')
sheet_name_0 = wb.sheets()[0]

from xlwt import Workbook, easyxf, Style, XFStyle

copy_value = Workbook(encoding='utf-8')
sheet_one = copy_value.add_sheet('sheet1')
rows_description_index = 1

department_name = sheet_name_0.cell(rows_description_index, 0).value

staff_name = sheet_name_0.cell(rows_description_index, 1).value

month = sheet_name_0.cell(rows_description_index, 2).value

normal_work_time = sheet_name_0.cell(rows_description_index, 3).value

sign_in_time = sheet_name_0.cell(rows_description_index, 4).value

sign_in_time_description = sheet_name_0.cell(rows_description_index, 5).value

sign_out_time = sheet_name_0.cell(rows_description_index, 6).value

sign_out_description = sheet_name_0.cell(rows_description_index, 7).value


# print 'department_name:' + department_name
# print "sign_in_time:" + sign_in_time


# def hanle_value(value, row, col, sign_in, sheet_name):
#     if isinstance(value, float):
#         sheet_name.write(row, col, value, Style.easyxf(
#             'pattern: pattern solid, fore_colour yellow;'
#             'align: horiz center;'
#         ))
#     else:
#         staff_sign_value = value.encode('utf-8')
#         if -1 != str.find(staff_sign_value, '-'):
#             staff_sign_in_time_info = staff_sign_value.split(' ')
#             staff_sign_in_time_date = staff_sign_in_time_info[0]
#             staff_sign_in_time_hour_second = staff_sign_in_time_info[-1]
#             staff_sign_in_time_hour_second_info = staff_sign_in_time_hour_second.split(':')
#             staff_sign_in_time_hour = staff_sign_in_time_hour_second_info[0]
#             staff_sign_in_time_second = staff_sign_in_time_hour_second_info[-1]
#             staff_sign_in_time_hour_int = int(staff_sign_in_time_hour)
#             staff_sign_in_time_second_int = int(staff_sign_in_time_second)
#             if sign_in:
#                 if staff_sign_in_time_hour_int >= 9:
#                     sheet_one.write(row, col, value, Style.easyxf(
#                     'pattern: pattern solid, fore_colour yellow;'
#                     'align: horiz center;'
#                 ))
#                 sheet_one.write(row, col + 1, '迟到', Style.easyxf(
#                     'pattern: pattern solid, fore_colour yellow;'
#                 ))
#                 else:
#                 sheet_one.write(row, col, value)
#
#         else:
#             sheet_one.write(row, col, value)
#
#
#
#
#     if sign_in:
#         pass
#     else:
#         pass


for row in range(sheet_name_0.nrows):
    values = []
    for col in range(sheet_name_0.ncols):
        value = sheet_name_0.cell(row, col).value

        # 员工上班打卡时间
        if col == 4:
            staff_sign_in_time = sheet_name_0.cell(row, col).value
            if isinstance(staff_sign_in_time, float):
                staff_sign_in_time = str(staff_sign_in_time)
                sheet_one.write(row, col, value, Style.easyxf(
                    'pattern: pattern solid, fore_colour yellow;'
                    'align: horiz center;'
                ))
            else:
                staff_sign_in_time = staff_sign_in_time.encode('utf-8')
                if -1 != str.find(staff_sign_in_time, '-'):
                    staff_sign_in_time_info = staff_sign_in_time.split(' ')
                    staff_sign_in_time_date = staff_sign_in_time_info[0]
                    staff_sign_in_time_hour_second = staff_sign_in_time_info[-1]
                    staff_sign_in_time_hour_second_info = staff_sign_in_time_hour_second.split(':')
                    staff_sign_in_time_hour = staff_sign_in_time_hour_second_info[0]
                    staff_sign_in_time_second = staff_sign_in_time_hour_second_info[-1]
                    staff_sign_in_time_hour_int = int(staff_sign_in_time_hour)
                    staff_sign_in_time_second_int = int(staff_sign_in_time_second)
                    if staff_sign_in_time_hour_int >= 9:
                        sheet_one.write(row, col, value, Style.easyxf(
                            'pattern: pattern solid, fore_colour yellow;'
                            'align: horiz center;'
                        ))
                        sheet_one.write(row, col + 1, '迟到', Style.easyxf(
                            'pattern: pattern solid, fore_colour yellow;'
                        ))
                    else:
                        sheet_one.write(row, col, value)

                else:
                    sheet_one.write(row, col, value)
        # 下班时间
        elif col == 6:
            staff_sign_in_time = sheet_name_0.cell(row, col).value
            if isinstance(staff_sign_in_time, float):
                staff_sign_in_time = str(staff_sign_in_time)
                sheet_one.write(row, col, value, Style.easyxf(
                    'pattern: pattern solid, fore_colour yellow;'
                    'align: horiz center;'
                ))
            else:
                staff_sign_in_time = staff_sign_in_time.encode('utf-8')
                if -1 != str.find(staff_sign_in_time, '-'):
                    staff_sign_in_time_info = staff_sign_in_time.split(' ')
                    staff_sign_in_time_date = staff_sign_in_time_info[0]
                    staff_sign_in_time_hour_second = staff_sign_in_time_info[-1]
                    staff_sign_in_time_hour_second_info = staff_sign_in_time_hour_second.split(':')
                    staff_sign_in_time_hour = staff_sign_in_time_hour_second_info[0]
                    staff_sign_in_time_second = staff_sign_in_time_hour_second_info[-1]
                    staff_sign_in_time_hour_int = int(staff_sign_in_time_hour)
                    staff_sign_in_time_second_int = int(staff_sign_in_time_second)
                    if staff_sign_in_time_hour_int <= 18:
                        sheet_one.write(row, col, value, Style.easyxf(
                            'pattern: pattern solid, fore_colour yellow;'
                            'align: horiz center;'
                        ))
                        sheet_one.write(row, col + 1, '早退', Style.easyxf(
                            'pattern: pattern solid, fore_colour yellow;'
                        ))
                    else:
                        sheet_one.write(row, col, value)
                else:
                    sheet_one.write(row, col, value)
        elif col == 5:
            if row == rows_description_index:
                sheet_one.write(row, col, value)
            else:
                continue
        elif col == 7:
            if row == rows_description_index:
                sheet_one.write(row, col, value)
            else:
                continue
        else:
            sheet_one.write(row, col, value)

        if isinstance(value, float):
            value = str(value)
        values.append(value)
        # print ','.join(values)

copy_value.save('copyFile.xls')
copy_value.save(TemporaryFile())
