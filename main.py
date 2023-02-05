import fire

from CsvConverter import CsvConverter
from TableConvertContext import TableConvertContext, Type


def main(filepath: str, converter: str) -> str:
    tableConvertContext = TableConvertContext([CsvConverter()])
    with open(filepath, "r") as f:
        content = f.read()
        return tableConvertContext.toMdTable(content, Type.fromString(converter))


if __name__ == '__main__':
    fire.Fire(main)
