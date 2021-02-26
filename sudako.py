import math

class Sudako():
  rowCount = 0
  colCount = 0

  @property
  def Size(self):
    return (self.rowCount, self.colCount)

  @property
  def CellsSolved(self):
    solved = 0
    for cell in self.Cells:
      if(len(cell.Options)==1):
        solved += 1
    return solved

  cells = []
  @property
  def Cells(self):
    return self.cells

  def BoxCells(self, box):
    boxList = []
    for cell in self.cells:
      if(cell.BoxIndex == box):
        boxList.append(cell)
    return boxList

  def ColumnCells(self, column):
    colList = []
    for cell in self.cells:
      if(cell.ColumnIndex == column):
        colList.append(cell)
    return colList

  def RowCells(self, row):
    rowList = []
    for cell in self.Cells:
      if (cell.RowIndex == row):
        rowList.append(cell)
    return rowList

  def SetupPuzzle(self, puzzel):
    x = 0
    for row in puzzel:
      y = 0
      for item in row:
        cell = Cell(self, x, y, item)
        self.Cells.append(cell)
        y += 1
      x += 1
    
    self.rowCount = x
    self.colCount = y

  def RecalculateOptions(self):
    for cell in self.Cells:
      if (cell.Solved):
        #print(cell.Value)
        continue
      cell.Options = self.ReduceOptions(cell)
      
  def MergeOptions(self, cells):
    options = []
    for cell in cells:
      if(cell.Solved):
        continue
      for opt in cell.Options:
        options.append(opt)
    
    for i in range(1, self.Size[0]+1):
      # check if there is only one valid location #
      if(options.count(i) == 1):
        for cell in cells:
          if(i in cell.Options):
            cell.Options = [i]
            return True
    return False

  def RunMerge(self):
    for i in range(self.Size[0]):
        if(self.MergeOptions(self.RowCells(i))):
          return True
        if(self.MergeOptions(self.ColumnCells(i))):
          return True
        if(self.MergeOptions(self.BoxCells(i))):
          return True
    return False

  def ReduceOptions(self, cell):
    options = list(range(1, self.Size[0] + 1))
    matching = [
      self.ColumnCells(cell.ColumnIndex),
      self.RowCells(cell.RowIndex),
      self.BoxCells(cell.BoxIndex),
    ]
    ## eliminate options for solved squares ##
    for group in matching:
      for check in group:
        if (check.Solved == False):
          continue
        
        if (check.Value in options):
          options.remove(check.Value)
    
    if (len(options) == 10):
      print("Solved:", cell.RowIndex, cell.ColumnIndex, options)
      print("Box")
      self.PrintCellValues(self.BoxCells(cell.BoxIndex))
      print("Column")
      self.PrintCellValues(self.ColumnCells(cell.ColumnIndex))
      print("Row")
      self.PrintCellValues(self.BoxCells(cell.RowIndex))


    return options

  def ApplySolvedCells(self):
    solved = 0
    for cell in self.Cells:
      if (cell.Solved):
        continue

      if(len(cell.Options) == 1):
        cell.Value = cell.Options[0]
        solved += 1
    return solved

  def BoxOverlap(self, box, list):
    return

  def PrintCellValues(self, cells):
    line = []
    row = 0
    for cell in cells:
      if(cell.RowIndex != row):
        row = cell.RowIndex
        if(row > 0):
          print(",".join(line))
        line=[]

      if (len(cell.Options) == 1):
        line.append(str(cell.Options))
      elif (cell.Value == 0):
        line.append("   ")
      else:
        line.append(" "+str(cell.value)+" ")
    print(",".join(line))

'''
  def CheckPuzzle(self, solution):
    i = 0
    for row in range(self.Size[0]):
      for col in range(self.Size[1]):
        assert(solution[row][col] == self.cells[i], "Error in row:"+str(row)+" col:"+str(col))
        i += 1
    print("Solution has passed!")
'''

class Cell():
  def __init__(self, sudako, row, col, value):
    self.sudako = sudako
    self.row = row
    self.col = col
    self.value = value

  @property 
  def RowIndex(self):
    return self.row

  @property
  def ColumnIndex(self):
    return self.col

  sudako = Sudako()
  @property
  def Sudako(self):
    return self.sudako
  
  options = []
  @property
  def Options(self, value = None):
    if(value):
      self.options = value
    return self.options

  @Options.setter
  def Options(self, value):
    if (value):
      self.options = value

  @property
  def Solved(self):
    return self.Value > 0

  @property
  def Value(self):
    return self.value

  @Value.setter
  def Value(self, value):
    self.value = value

  @property
  def BoxIndex(self):
    return (math.floor(self.row / 3) * 3) + math.floor(self.col / 3)

class Puzzle():
  @property
  def Puzzle1(self):
    puzzle = []
    puzzle.append([0,3,0, 0,1,0, 0,6,0])
    puzzle.append([7,5,0, 0,3,0, 0,4,8])
    puzzle.append([0,0,6, 9,8,4, 3,0,0])
    puzzle.append([0,0,3, 0,0,0, 8,0,0])
    puzzle.append([9,1,2, 0,0,0, 6,7,4])
    puzzle.append([0,0,4, 0,0,0, 5,0,0])
    puzzle.append([0,0,1, 6,7,5, 2,0,0])
    puzzle.append([6,8,0, 0,9,0, 0,1,5])
    puzzle.append([0,9,0, 0,4,0, 0,3,0])
    return puzzle

  # NYT Easy
  @property
  def Puzzle2(self):
    puzzle = []
    puzzle.append([1,3,9, 8,0,7, 0,0,0])
    puzzle.append([4,0,0, 3,0,0, 6,8,9])
    puzzle.append([6,0,0, 4,0,0, 0,7,0])
    puzzle.append([0,0,0, 7,0,2, 1,6,0])
    puzzle.append([7,9,6, 0,3,0, 0,0,0])
    puzzle.append([0,4,1, 0,0,0, 9,0,7])
    puzzle.append([9,1,0, 0,5,3, 7,0,2])
    puzzle.append([3,0,4, 0,7,0, 0,0,6])
    puzzle.append([0,6,0, 0,4,0, 0,0,3])
    return puzzle

  @property
  def Solution2(self):
    puzzle = []
    puzzle.append([1,3,9, 8,6,7, 4,2,5])
    puzzle.append([4,7,2, 3,1,5, 6,8,9])
    puzzle.append([6,8,5, 4,2,9, 3,7,1])
    puzzle.append([8,5,3, 7,9,2, 1,6,4])
    puzzle.append([7,9,6, 1,3,4, 2,5,8])
    puzzle.append([2,4,1, 5,8,6, 9,3,7])
    puzzle.append([9,1,8, 6,5,3, 7,4,2])
    puzzle.append([3,2,4, 9,7,8, 5,1,6])
    puzzle.append([5,6,7, 2,4,1, 8,9,3])
    return puzzle

  # NYT Medium 
  @property
  def Puzzle3(self):
    puzzle=[]
    puzzle.append([3,0,0, 0,2,0, 0,0,4])
    puzzle.append([0,1,2, 9,0,0, 0,0,0])
    puzzle.append([0,0,6, 0,0,1, 3,0,0])
    puzzle.append([1,0,4, 0,0,0, 0,0,0])
    puzzle.append([0,0,3, 0,0,0, 7,6,0])
    puzzle.append([6,0,0, 0,0,2, 0,4,3])
    puzzle.append([0,8,1, 0,0,7, 0,2,5])
    puzzle.append([2,0,0, 0,4,0, 0,0,0])
    puzzle.append([0,0,7, 0,0,0, 0,0,0])
    return puzzle





def main():
  s = Sudako()
  s.SetupPuzzle(Puzzle().Puzzle3)
  print("--initial setup--")
  s.PrintCellValues(s.Cells)
  s.RecalculateOptions()
  counter = 0
  lastSolved = 0
  while (counter < s.Size[0]*s.Size[1]):
    counter += 1
    s.ApplySolvedCells()
    s.RecalculateOptions()
    s.RunMerge()
    solved = s.CellsSolved
    if(solved == lastSolved):
      break
    else:
      lastSolved = solved
    print("interation:", counter, "solved:", solved)
    s.PrintCellValues(s.cells)

    ## print final solution ##
    print("interation", counter, "solved:", solved)
    s.PrintCellValues(s.cells)

  s.PrintCellValues(s.BoxCells(2))
  #s.CheckPuzzle(Puzzle().Solution2)

if __name__ == '__main__':
  main()


