import math

class SudokuCell():
  def __init__(self, row, col, value):
    self.row = row
    self.col = col
    self.value = value

  @property 
  def RowIndex(self):
    return self.row

  @property
  def ColumnIndex(self):
    return self.col
  
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
    return self.Value > 0 or len(self.Options) == 1

  @property
  def Value(self):
    if (not self.value and len(self.Options) == 1):
        self.value = self.Options[0]
        
    return self.value

  @Value.setter
  def Value(self, value):
    self.value = value

  @property
  def BoxIndex(self):
    return (math.floor(self.row / 3) * 3) + math.floor(self.col / 3)
