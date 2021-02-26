
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
    puzzle.append([6,0,0, 0,0,2, 0,9,0])
    puzzle.append([0,8,1, 0,0,7, 0,2,5])
    puzzle.append([2,0,0, 0,4,0, 0,0,0])
    puzzle.append([0,0,7, 0,0,0, 0,0,0])
    return puzzle
