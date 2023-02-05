import TableConvertContext


class CsvConverter(TableConvertContext.TableDataParser):
    def parseData(self, rawData: str) -> TableConvertContext.DataModel:
        return TableConvertContext.DataModel(
            header=["header1", "header2"],
            data=[["row1", "row2"], ["row3", "row4"]]
        )

    def type(self) -> TableConvertContext.Type:
        return TableConvertContext.Type.CSV
