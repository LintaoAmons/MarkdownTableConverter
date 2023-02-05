import enum
from abc import ABC, abstractmethod


class Type(enum.Enum):
    CSV = 1


class TableConverter(ABC):
    @abstractmethod
    def toMdTable(self) -> str:
        pass

    @abstractmethod
    def fromMdTable(self) -> str:
        pass

    def type(self) -> Type:
        pass


class TableConvertContext:
    def __init__(self, converters: list[TableConverter]):
        self.types = {}
        for converter in converters:
            self.types[converter.type()] = converter

    def toMdTable(self, type_: Type):
        return self.types[type_].toMdTable()

    def fromMdTable(self, type_: Type):
        return self.types[type_].fromMdTable()
