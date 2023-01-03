#
# @lc app=leetcode id=1222 lang=python3
#
# [1222] Queens That Can Attack the King
#

# @lc code=start
class Solution:
    def queensAttacktheKing(self, queens: List[List[int]], king: List[int]) -> List[List[int]]:
        # board: List[List[int]], create a 8x8 board
        board = [[0 for _ in range(8)] for _ in range(8)]
        # reserve: the king now will attack the queen
        queensCanAttack = []
        # check if the king can attack the queen
        for i in range(len(queens)):
            board[queens[i][0]][queens[i][1]] = 1
        # check the 8 directions
        # up
        for i in range(king[0]-1, -1, -1):
            if board[i][king[1]] == 1:
                queensCanAttack.append([i, king[1]])
                break
        # down
        for i in range(king[0]+1, 8):
            if board[i][king[1]] == 1:
                queensCanAttack.append([i, king[1]])
                break
        # left
        for i in range(king[1]-1, -1, -1):
            if board[king[0]][i] == 1:
                queensCanAttack.append([king[0], i])
                break
        # right
        for i in range(king[1]+1, 8):
            if board[king[0]][i] == 1:
                queensCanAttack.append([king[0], i])
                break
        # left-up
        i = king[0]-1
        j = king[1]-1
        while i >= 0 and j >= 0:
            if board[i][j] == 1:
                queensCanAttack.append([i, j])
                break
            i -= 1
            j -= 1
        # left-down
        i = king[0]+1
        j = king[1]-1
        while i < 8 and j >= 0:
            if board[i][j] == 1:
                queensCanAttack.append([i, j])
                break
            i += 1
            j -= 1
        # right-up
        i = king[0]-1
        j = king[1]+1
        while i >= 0 and j < 8:
            if board[i][j] == 1:
                queensCanAttack.append([i, j])
                break
            i -= 1
            j += 1
        # right-down
        i = king[0]+1
        j = king[1]+1
        while i < 8 and j < 8:
            if board[i][j] == 1:
                queensCanAttack.append([i, j])
                break
            i += 1
            j += 1
        return queensCanAttack
# @lc code=end

