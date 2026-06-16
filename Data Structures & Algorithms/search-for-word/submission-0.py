class Solution:
    def __init__(self):
        self.move=[
            [1,0],[-1,0],
            [0,1],[0,-1],
            # [1,1],[-1,-1],
            # [1,-1],[-1,1]                   
                ]
        # self.does_exist=False

    def exist(self, board: List[List[str]], word: str) -> bool:
        if not word:
            return True
        # self.does_exist = False
        char_match_pos=0
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == word[char_match_pos]:
                    # print(board[i][j],word[char_match_pos],char_match_pos)
                    if self.dfs(board,word,i,j,char_match_pos):
                        return True
                char_match_pos=0
        return False

    def dfs(self, board, word, i, j, char_match_pos):
        if i<0 or j<0 or i>=len(board) or j>=len(board[i]):
            return False

        if board[i][j] != word[char_match_pos]:
            return False
        
        if char_match_pos==len(word)-1:
            return True

        temp=board[i][j]
        board[i][j]='#'

        for dx,dy in self.move:
            if self.dfs(board,word,i+dx,j+dy,char_match_pos+1):
                return True


        board[i][j]=temp
        return False


