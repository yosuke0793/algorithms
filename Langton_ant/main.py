import numpy as np
import matplotlib.pyplot as plt

class LangtonAnt:
  def __init__(self,Name_):
    self.name = Name_
    print(self.name, "generated")
    self.position=np.zeros([2],dtype=int)

  def check_position(self,arg1):
    x=self.position[0]
    y=self.position[1]
    print(self.name, 'Position')
    print('Index: (', x, ',' ,y, ')')
    arg1.return_cordinate(x,y)

  def action(self,arg1):
    self.check_position(arg1)

class gridmap:
  def __init__(self,ngrid):
    range=[0,ngrid]
    xs=np.linspace(range[0],range[1],ngrid+1)
    ys=np.linspace(range[0],range[1],ngrid+1)
    self.grid_x,self.grid_y=np.meshgrid(xs,ys)
    self.field=np.zeros_like(self.grid_x)

  def return_cordinate(self,arg1,arg2):
    print('Coordinate:', self.grid_x[arg1][arg2], ',' ,self.grid_y[arg1][arg2])
    print('Grid State:', self.field[arg1][arg2] )

ngrid = 3
map = gridmap(ngrid)
# map.return_cordinate(1,1)

ant1 = LangtonAnt("Ant 1")
# ant1.check_position(map)
ant1.action(map)