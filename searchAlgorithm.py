# ----------
# User Instructions:
# 
# Define a function, search() that returns a list
# in the form of [optimal path length, row, col]. For
# the grid shown below, your function should output
# [11, 4, 5].
#
# If there is no valid path from the start point
# to the goal, your function should return the string
# 'fail'
# ----------

# Grid format:
#   0 = Navigable space
#   1 = Occupied space


grid = [[0, 1, 1, 0, 0, 0],
        [0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 1, 0],
        [0, 0, 1, 1, 1, 0],
        [0, 0, 0, 0, 1, 0]]
init = [0, 0]
goal = [len(grid)-1, len(grid[0])-1]
cost = 1

delta = [[-1, 0], # go up
         [ 0,-1], # go left
         [ 1, 0], # go down
         [ 0, 1]] # go right

delta_name = ['^', '<', 'v', '>']


def search(grid,init,goal,cost):
    # ----------------------------------------
    # insert code here
    # ----------------------------------------
    i = init[0]
    j = init[1]
    g_value = 0 
    all_path = [ [i,j ]]
    path = []
    for k in range(len(all_path)):
        g_value +=1
        new_path = []
        x , y  = expand( i , j , g_value)
     
        for m in range (len(x)):
            new_path.append(x[m])
        
        for m in range(len(path)):
            path.append(y[m][2])
                
        if k == (   len(all_path) -1    ) :
             all_path = new_path
             k = 0 
    path = [ goal[0] , goal [1] , min(path)]
    return path
    
def expand( i , j , g_value  , goal ):
    res = []
    for k in range(len(delta)):
        NEW_WAY = 0 #flag for new way
        x = i+delta[k][0]
        y = j+delta[k][1]
        n = grid[x][y] # 
        goal_arriv = []
        res = []
         
        if n == 0 :
            if x == goal[0] and y == goal[1]:
                goal_arriv.append([x , y , g_value])
            else:
                res.append([x , y ])

    return res , goal_arriv