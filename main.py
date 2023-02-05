from CsvConverter import CsvConverter
from TableConvertContext import TableConvertContext, Type

if __name__ == '__main__':
    TableConvertContext = TableConvertContext([CsvConverter()])
    print(TableConvertContext.toMdTable(Type.CSV))
