from SudokuCell import SudokuCell as Cell
from Puzzle import Puzzle

class Sudoku():
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
        cell = Cell(x, y, item)
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
            cell.Value = i
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

  def PrintCellOptions(self, cells):
    for cell in cells:
      if (cell.Solved):
        print("Row:", cell.RowIndex, "Column:", cell.ColumnIndex, "Value:", cell.Value)
      else:
        print("Row:", cell.RowIndex, "Column:", cell.ColumnIndex, "Options:", cell.Options)


  def CheckPuzzle(self, solution):
    i = 0
    for row in range(self.Size[0]):
      for col in range(self.Size[1]):
        assert(solution[row][col] == self.cells[i], "Error in row:"+str(row)+" col:"+str(col))
        i += 1
    print("Solution has passed!")
    return True

def main():
  s = Sudoku()
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
    s.RecalculateOptions()
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

if __name__ == '__main__':
  main()


