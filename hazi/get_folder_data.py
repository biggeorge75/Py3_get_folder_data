'''
Konzolos alkalmazás. Bekéri egy könyvtár útvonalát, majd kimenti a benne lévő fájlok adatait (name, size, date) *.txt + *.json + *.xlsx fájlokba.
'''

import os, openpyxl
import time
import json
from openpyxl.styles import Font, Alignment, NamedStyle
import datetime

# példányosítok egy workbookot
workbook = openpyxl.Workbook()

sheet = workbook.active

# beállítom az .xlsx oszlopainak szélességét
sheet.column_dimensions["A"].width = 40
sheet.column_dimensions["B"].width = 15
sheet.column_dimensions["C"].width = 30

# beállítom a fejlécet bold-ra
bold_font = Font(bold=True)
sheet[f'A1'].font = bold_font
sheet[f'B1'].font = bold_font
sheet[f'C1'].font = bold_font

# EXCEL első sorának kitöltése
sheet[f'A1'] = "File"
sheet[f'B1'] = "Size"
sheet[f'C1'] = "Date"

# létrehozok 2 üres szótárat
data = {}
vdata = {}

# bekérem a mappa útvonalát
try:
    folder = input('Kérem a mappa útvonalát: ')
    file_list = [ os.path.join(folder, f) for f in os.listdir(folder) if os.path.isfile(os.path.join(folder, f)) ]

    index = 1 # fájl utáni index szám a .json fájlban

    # .txt megnyitása írásra
    with open('folder_data.txt', 'w') as f:
        # fájl_list körbejárása + adatok változókba mentése
        for i in file_list:
            file_name = os.path.basename(i)
            file_size = os.path.getsize(i)
            file_date = datetime.datetime.fromtimestamp(os.path.getctime(i))

            # .txt fájl mentése, formázással
            f.write('{:<40}{:<10}{:<10}\n'.format(file_name,file_size,file_date.strftime("%y/%m/%d %H:%M")))

            # szótárakba mentem az adatokat
            data['file'+str(index)+'_'+i] = vdata
            vdata['size:'] = file_size
            vdata['date:'] = file_date.strftime("%y/%m/%d %H:%M")

            # betöltöm az adatokat az .xlsx-be
            sheet[f'A{index + 2}'] = file_name
            sheet[f'B{index + 2}'] = file_size
            sheet[f'C{index + 2}'] = file_date.strftime("%y/%m/%d %H:%M")

            index +=1 # fájl utáni index növelése
except:
    print('Nem adtad meg az útvonalat!')

# .json fájl mentése
with open("folder_data.json", "w") as f:
    json.dump(data, f)

# EXCEL fájl mentése
workbook.save(filename="folder_data.xlsx")

# fájl db szám kiíratása
print(len(data))