class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        hm = defaultdict(list)
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    continue
                if len(hm[board[i][j]]):
                    for elem in hm[board[i][j]]:
                        row, col = elem[0], elem[1]
                        if row == i:
                            return False
                        if col == j:
                            return False
                        if row // 3 == i // 3 and col // 3 == j // 3:
                            return False
                hm[board[i][j]].append([i, j])
        return True