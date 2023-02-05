import enum
from abc import ABC

from MarkdownUtil import MarkdownTableUtil


class Type(enum.Enum):
    CSV = 1


class DataModel:
    def __init__(self, header: list[str], data: list[list[str]]):
        self.header = header
        self.data = data


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
