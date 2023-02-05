class MarkdownTableUtil:

    @staticmethod
    def _generateHeader(header: list[str]):
        if len(header) == 0:
            raise Exception("header is empty")
        if len(header) == 1:
            return f"| {header[0]} |\n| --- |"

        columns = [f"| {header[0]} |"]
        for i in header[1:]:
            columns.append(f" {i} |")

        headerString = "".join(columns)

        splitString = "".join(["| --- |"] + [" --- |" for _ in range(len(header) - 1)])

        return f"{headerString}\n{splitString}"

    @staticmethod
    def _generateOneRow(columnLength: int, data: list[str]):
        if columnLength == 1:
            one = "" if data[0] is None else data[0]
            return f"| {one} |"

        columns = []
        for i in range(columnLength):
            one = ""
            try:
                one = data[i]
            except IndexError as e:
                pass

            if i == 0:
                columns.append(f"| {one} |")
            else:
                columns.append(f" {one} |")

        return "".join(columns)

    @staticmethod
    def _generateData(size: int, data: list[list[str]]):
        return "\n".join([MarkdownTableUtil._generateOneRow(size, oneRow) for oneRow in data])

    @staticmethod
    def generate(header: list[str], data: list[list[str]]):
        headerString = MarkdownTableUtil._generateHeader(header)
        dataString = MarkdownTableUtil._generateData(len(header), data)
        return f"{headerString}\n{dataString}"

    @staticmethod
    def fromCSVtoTable(csv_file_path: str) -> str:
        pass
        # with open(csv_file_path, 'r') as f:
        #     rows = f.read().split("\n")
        #     data = [row.split(',') for row in rows]
        #
        # MarkdownTableUtil.generate()


if __name__ == '__main__':
    print(MarkdownTableUtil.generate(["header1", "header2", "header3"], [["aa", "bb"], ["dd", "cc"], []]))
