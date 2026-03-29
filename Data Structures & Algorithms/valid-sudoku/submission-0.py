class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def checkRows()-> bool:
            rows = len(board)
            for row in range(rows):
                seen = set()
                for digit in board[row]:
                    if digit == '.':
                        continue
                    if digit in seen:
                        # print(f"{row}, {digit}")
                        return False
                    seen.add(digit)

            return True

        def checkColumns() -> bool:
            rows = len(board)
            cols = len(board[0])

            for col in range(cols):
                seen = set()
                for row in range(rows):
                    digit = board[row][col]
                    if digit == '.':
                        continue
                    if digit in seen:
                        # print(f"{col}, {digit}")
                        return False

                    seen.add(digit)

            return True

        def checkSubboxes():
            col = 0
            for row in range(0, len(board), 3):
                curr_row = row
                for curr_col in range(0, len(board[0]), 3):
                    # print(f"{curr_row}, {curr_col}")
                    seen = set()
                    for r in range(curr_row, curr_row + 3):
                        for c in range(curr_col, curr_col + 3):
                            digit = board[r][c]
                            if digit == ".":
                                continue
                            if digit in seen:
                                # print(f"({r},{c}), {digit}")
                                return False
                            seen.add(digit)

            return True

        # print(checkRows())
        # print(checkColumns())
        # print(checkSubboxes())

        return checkRows() and checkColumns() and checkSubboxes()
