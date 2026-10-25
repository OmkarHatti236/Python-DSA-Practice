def exists(board,i,j,word,idx):
    if idx==len(word):
        return True

    if i<0 or i>=len(board) or j<0 or j>=len(board[0]) or board[i][j]!=word[idx] or board[i][j]=='*': 
        return False
    
    ch=board[i][j]
    board[i][j]='*'

    result=exists(board,i+1,j,word,idx+1)or\
    exists(board,i,j+1,word,idx+1)or\
    exists(board,i-1,j,word,idx+1)or\
    exists(board,i,j-1,word,idx+1)
    board[i][j]=ch
    return result


board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word="ABCCEDl"

def find(board,word):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j]==word[0] and exists(board,i,j,word,0):
                return True
    return False

if find(board,word):
    print("found")
else:
    print("not found")


        
