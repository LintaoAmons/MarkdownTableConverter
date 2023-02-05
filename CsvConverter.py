import TableConvertContext


class CsvConverter(TableConvertContext.TableDataParser):
    def parseData(self, rawData: str) -> TableConvertContext.DataModel:
        rows = rawData.strip().split("\n")
        if len(rows) < 1:
            raise Exception("No data in your input")

        header = rows[0].split(",")

        if len(rows) == 1:
            return TableConvertContext.DataModel(
                header=header,
                data=[]
            )
        else:
            data = [row.split(",") for row in rows[1:]]
            return TableConvertContext.DataModel(
                header=header,
                data=data
            )

    def type(self) -> TableConvertContext.Type:
        return TableConvertContext.Type.CSV


def testParseData():
    csv = "header1,header2\n" \
          "row1, row2\n" \
          "row3, row4\n"
    converter = CsvConverter()
    result = converter.parseData(csv).__repr__()

    expect = """{"header1": "row1", "header2": " row2"}
{"header1": "row3", "header2": " row4"}"""

    if result != expect:
        raise Exception("Test failed")
    else:
        print("Test passed")


if __name__ == '__main__':
    testParseData()
