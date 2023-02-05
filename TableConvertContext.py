import enum
import json
from abc import ABC

from MarkdownUtil import MarkdownTableUtil


class Type(enum.Enum):
    CSV = 1

    @staticmethod
    def fromString(str_: str):
        if str_ == 'csv':
            return Type.CSV
        else:
            raise Exception("Not support yet")


class DataModel:
    def __init__(self, header: list[str], data: list[list[str]]):
        self.header = header
        self.data = data

    def __repr__(self):
        rows = []
        for row in self.data:
            row_data = {}
            for i in range(len(self.header)):
                row_data[self.header[i]] = row[i] or ""
            rows.append(row_data)

        return "\n".join([json.dumps(row) for row in rows])


class TableDataParser(ABC):
    def parseData(self, rawData: str) -> DataModel:
        pass

    def type(self) -> Type:
        pass


class TableConvertContext:
    def __init__(self, converters: list[TableDataParser]):
        self.types = {}
        for converter in converters:
            self.types[converter.type()] = converter

    def toMdTable(self, rawData: str, type_: Type) -> str:
        dataModel = self.types[type_].parseData(rawData)
        return MarkdownTableUtil.generate(dataModel.header, dataModel.data)
