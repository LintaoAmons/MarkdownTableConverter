import TableConvertContext


class CsvConverter(TableConvertContext.TableConverter):

    def toMdTable(self) -> str:
        return "csvConverter"

    def fromMdTable(self) -> str:
        return "csvConverter"

    def type(self) -> TableConvertContext.Type:
        return TableConvertContext.Type.CSV
