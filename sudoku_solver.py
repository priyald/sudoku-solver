import math

class Sudoku:
    def __init__ (self, sud):
        self.sudoku = sud
        self.max_val = 9
        self.block_s = 3

    #purpose: print the solved sudoku
    #input: N/A
    #output: N/A
    def print_sud(self):
        ans = self.solve(self.sudoku,0,0)[0]
        for i in range(self.max_val):
                if i%self.block_s==0:
                   print("_"*self.max_val)
                for j in range(self.max_val):
                    if j%self.block_s==0:
                        print("|",end=" ")
                    print (ans[i][j],end=" ")
                print()
        print()

    #purpose: create a deepcopy of sudoku so that we can pass-by-value
    #input: sudoku
    #output: deepcopied sudoku
    def deepcopy(self, sud):
        cpy = []
        for i in sud:
            cpy.append(i[:])
        return cpy

    #purpose: to check which values can be filled in a sudoku cell
    #input: the sudoku grid. the row and col number of the cell to be checked
    #output: an array of all integers that can be filled 
    def checkAvail(self, sud, row, col):
        ans = []

        #add all possible values that can be filled in a block
        for i in range(1,self.max_val+1):
            ans.append(i)
        
        #check row
        for i in sud[row]:
            try:
                ans.remove(i)
            except:
                pass

        #check column
        for j in sud:
            try:
                ans.remove(j[col])
            except:
                pass

        #check block
        block_row = row//self.block_s
        block_col = col//self.block_s

        for r in range(self.block_s):
            for c in range(self.block_s):
                try:
                    ans.remove(sud[block_row*self.block_s+r][block_col*self.block_s+c])
                except:
                    pass

        return ans


    #purpose: fill sudoku sudoku cell with nearest correct solution using backtracking
    #         and see whether that makes a valid answer to the sudoku
    #input: sudoku grid. the row and col of the cell whose value needs to be determined
    #output: the sudoku grid with the correct value filled and boolean for whether it is valid
    def solve(self, sud, row, col):
        cpy = self.deepcopy(sud)

        #if last cell is being checked
        if row==self.max_val-1 and col==self.max_val-1:
            #if value already has been filled
            if cpy[row][col]!=0:
                return cpy, True
            #if value needs to be found
            values = self.checkAvail(cpy, row, col)
            if len(values)==1:
                cpy[self.max_val-1][self.max_val-1]=values[0]
                return cpy, True
            else:
                return cpy, False


        #next cell row and column values for backtracing
        next_row = row
        next_col = col+1

        if col==self.max_val-1:
                next_row = row+1
                next_col = 0

        #if current cell is already filled with a value
        if cpy[row][col]!=0:
            return self.solve(cpy, next_row, next_col)
        
        #if value needs to be found
        values = self.checkAvail(cpy, row, col)
        for i in values:
            cpy[row][col]=i
            ans = self.solve(cpy, next_row, next_col)
            if ans[1]==True:
                return ans
            cpy[row][col]=0
            
        return cpy, False