import csv
from sys import exit
from openpyxl import Workbook
import argparse
from pprint import pprint

parser = argparse.ArgumentParser(description='')
parser.add_argument('-s', '--stav', type=str)
parser.add_argument('-w', '--win', action='store_true')
parser.add_argument(
    '-l', '--lose', action='store_true'
)
parser.add_argument(
    '-c', '--conv', action='store_true'
)

args = parser.parse_args()
xp = './storage/downloads/Binarium/binariumDemo.xlsx'

with open('output.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    data = list(reader)

proc_ = 82
#edit
last = len(data) - 1
if args.win:
    if len(data[last]) == 2:
        st = int(data[last][1][:-1])
        data[last].append(
            str(
                round(st + (st * proc_ / 100), 0)
            )[:-2] + '₽'
        )
        data[last].append(
            str(round(st * proc_ / 100, 0))[:-2] + '₽'
        )
        data.append([
            str(
                int(data[last][0][:-1]) + round(
                    (st * proc_ / 100), 0
                )
            )[:-2] + '₽'
        ])
        pprint(
            data
        )
elif args.lose:
    if len(data[last]) == 2:
        data[last].append('0₽')
        data.append([
            str(
                int(data[last][0][:-1]) - int(
                    data[last][1][:-1]
                )
            ) + '₽'
        ])
        pprint(data)
else:
    if len(data[last]) == 1:
        data[last].append(args.stav + '₽')
        pprint(
            data
        )

def save_(data):
    # Откройте файл CSV для записи
    with open('output.csv', 'w', newline='') as csv_:
        writer = csv.writer(csv_)
        writer.writerows(data)
        csvfile.close()

    wb = Workbook()
    ws = wb.active

    for row in data:
        ws.append(row)

    wb.save(xp)

save_(data)
