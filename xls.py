import xlsxwriter as xw
from sys import argv
from file_ import ff, Modes

wb = xw.Workbook(
    './storage/downloads/Binarium/binariumDemo.xlsx'
)
ws = wb.add_worksheet()
cf = wb.add_format()

last = int(ff('last.txt').get(Modes.FIRST))
cur = str(last + 1)
if len(argv) == 3 and argv[2] == 'u':
    ws.write(                                                  'B'+cur,
        '=B'+cur,
        cf.set_font_color('green')
    )
    ws.write(
        'C'+cur,
        (),
        cf.set_font_color('green')
    )
    ws.write(
        'D'+cur
    )
    ff('last.txt').put(last+1)

if len(argv) == 3 and argv[2] == 'd':
    ws.write(
        'B'+cur,
        '=B'+cur,
        cf.set_font_color('red')
    )
    ff('last.txt').put(last+1)

if len(argv) == 2:
    ws.write(
        'A'+cur,
        '=A'+str(last)+'+D'+str(last)
    )
    ws.write('B'+cur, str(argv[1]))

wb.close() 
