import xlwt
import xlrd
from xlutils.copy import copy

def WriteExcel(Path, strSheetName, intRow, intCol, strValue):
    read_wb = xlrd.open_workbook(Path)
    wb = copy(read_wb)
    intRow = int(intRow)
    intCol = int(intCol)
    #SheetIndex = int(SheetIndex)
    strSheetName = str(strSheetName)
    w_sheet = wb.get_sheet(strSheetName)
    w_sheet.write(intRow,intCol,strValue)
    wb.save(Path)


if __name__ == "__main__":
    WriteExcel('C:/Users/eswakat/Desktop/testing.xls', 0, 1 , 1, 'Swati')