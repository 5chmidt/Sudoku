from SudokuCell import SudokuCell as Cell
from Puzzle import Puzzle
import Helper

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

  ''' 
  Initialize cell.Options values, by eliminating all solved numbers sharing a row, column or box.
  '''
  def DefaultPuzzleOptions(self):
    for cell in self.Cells:
      if (cell.Solved):
        continue
      if (not cell.Options):
        cell.Options = self.DefaultCellOptions(cell)

  '''
  Create a single list of option values from a group of cells.
  The list will have repeated values according to the number of cells each option appears in.
  '''
  def ListGroupOptions(self, cells):
    options = []
    for cell in cells:
      if(cell.Solved):
        continue
      for opt in cell.Options:
        options.append(opt)
    return options

  '''
  Check each group, if there is only one cell that is valid for a given option, set as the solved value.
  '''
  def MergeGroupOptions(self, cells):
    options = self.ListGroupOptions(cells)   
    for i in range(1, self.Size[0]+1):
      # check if there is only one valid location #
      if(options.count(i) == 1):
        for cell in cells:
          if(i in cell.Options and not cell.Solved):
            cell.Options = [i]
            cell.Value = i
            self.RemoveSolvedOptions(cell)
            return True
    return False

  def RunMerge(self):
    for i in range(self.Size[0]):
        if(self.MergeGroupOptions(self.RowCells(i))):
          return True
        if(self.MergeGroupOptions(self.ColumnCells(i))):
          return True
        if(self.MergeGroupOptions(self.BoxCells(i))):
          return True
    return False

  '''
  Populate default options 1-9 for a grid cell.
  Eliminate solved values from the list by row, column or box.
  '''
  def DefaultCellOptions(self, cell):
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
    
    return options

  def RemoveSolvedOptions(self, cell):
    if(not cell.Solved):
      return
    
    dataSet = [
      self.RowCells(cell.RowIndex),
      self.ColumnCells(cell.ColumnIndex),
      self.BoxCells(cell.BoxIndex),
    ]
    for cells in dataSet:
      for c in cells:
        if (cell.Value in c.Options):
          c.Options.remove(cell.Value)

  def BoxLineMerge(self, box, list):
    for i in range(self.Size[0]):
      cells = self.BoxCells(i)
      options = self.ListGroupOptions(cells)

      for opt in Helper.DistinctList(options):
        row = []
        col = []
        for cell in cells:
          if(opt in cell.Options):
            row.append(opt.RowIndex)
            col.append(opt.ColumnIndex)
        
        found = False
        ## eliminate conflicting rows ##
        if (len(row) > 1 and row.count(opt) == 1):
          for c in self.RowCells(row[0]):
            if (c.BoxIndex == i or c.Solved):
              continue

            if (opt in c.Options):
              c.Options.remove(opt)
              found = True
        
        if(len(col) > 1 and col.count(opt) == 1):
          for c in self.ColumnCells(col[0]):
            if (c.BoxIndex == i or c.Solved):
              continue

            if (opt in c.Options):
              c.Options.remove(opt)
              found = True
        
        if(found):
          return found
    
    return False

  def PrintCellValues(self, cells, heading = ""):
    if (heading):
      print(heading)

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
  s.PrintCellValues(s.Cells, "--initial setup--")
  counter = 0
  lastSolved = 0
  while (counter < s.Size[0]*s.Size[1]):
    counter += 1
    s.DefaultPuzzleOptions()
    i = 0
    while (s.RunMerge() and i < s.Size[0]*s.Size[1]):
      print("merge", i)
      i += 1
    
    solved = s.CellsSolved
    if(solved == lastSolved):
      print("solved", solved)
      break
    else:
      lastSolved = solved


    ## print final solution ##
    print("interation", counter, "solved:", solved)
    s.PrintCellValues(s.cells)

if __name__ == '__main__':
  main()


