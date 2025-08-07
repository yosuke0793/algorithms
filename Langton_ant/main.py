import numpy as np
import matplotlib.pyplot as plt

class LangtonAnt:
  def __init__(self,Name_):
    self.name      = Name_
    self.state     = 0
    self.direction = int(4)
    print(self.name, "generated")
    self.position=np.zeros([2],dtype=int)
    self.position=np.array([int(ngrid/2),int(ngrid/2)],dtype=int)

  def check_position(self,map,state):
    x=self.position[0]
    y=self.position[1]
    print(self.name, 'Position')
    print('Index: (', x, ',' ,y, ')')
    map.return_cordinate(x,y,state)
    map.change_field_state(x,y)

  def action(self,map):
    self.check_position(map,self.state)
    print(self.name,', State=', self.state)
    if( self.state==0 ):
      self.direction+=1
    else:
      self.direction+=-1

    if( self.direction<0 ):
      self.direction=3
    elif( self.direction>3 ):
      self.direction=0

    print(self.position)
    if( self.direction==0 ):
      self.position[0]+=1
    elif( self.direction==1 ):
      self.position[1]+=-1
    elif( self.direction==2 ):
      self.position[0]+=-1
    elif( self.direction==3 ):
      self.position[1]+=1
    print(self.position)

    print('Direction ', self.direction)

class gridmap:
  def __init__(self,ngrid):
    range=[-int(ngrid/2),int(ngrid/2)]
    xs=np.linspace(range[0],range[1],ngrid+1)
    ys=np.linspace(range[0],range[1],ngrid+1)
    self.grid_x,self.grid_y=np.meshgrid(xs,ys)
    self.field=np.zeros_like(self.grid_x)
    self.field[int(ngrid/2)][int(ngrid/2)+1]=1
    self.field[int(ngrid/2)+1][int(ngrid/2)]=1
    # print(self.grid_x)
    # print(self.grid_y)
    # print(self.field)

  def return_cordinate(self,arg1,arg2,state_grid):
    print('Coordinate:', self.grid_x[arg1][arg2], ',' ,self.grid_y[arg1][arg2])
    print('Grid State:', self.field[arg1][arg2] )
    state_grid=self.field[arg1][arg2]
    return state_grid

  def change_field_state(self,arg1,arg2):
    if( self.field[arg1][arg2]==1 ):
      self.field[arg1][arg2]=0
    else:
      self.field[arg1][arg2]=1
    print(self.field)


ngrid = 100
map = gridmap(ngrid)
ant1 = LangtonAnt("Ant 1")

fig=plt.figure()
axis=fig.add_subplot(111)
axis.set_xlim(-int(ngrid/2),int(ngrid/2))
axis.set_ylim(-int(ngrid/2),int(ngrid/2))
axis.set_xticks(np.linspace(-int(ngrid/2),int(ngrid/2),ngrid+2))
axis.tick_params(labelbottom=False, labelleft=False, labelright=False, labeltop=False)
# axis.set_xticklabels([])
axis.set_yticks(np.linspace(-int(ngrid/2),int(ngrid/2),ngrid+2))
# axis.set_yticklabels([])
axis.grid()

for i in range(2):
  ant1.action(map)

fig.savefig('./figures/figure.png')

