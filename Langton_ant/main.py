import os
import shutil
import glob
import random
from tqdm import tqdm
import cv2
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import patches
import matplotlib.animation as animation
from matplotlib.animation import FuncAnimation

class LangtonAnt:
  def __init__(self,Name_):
    self.name      = Name_
    self.state     = 0
    self.direction = 0
    # print(self.name, "generated")
    self.position=np.zeros([2],dtype=int)
    x_init= random.randint(0, ngrid-1)
    y_init= random.randint(0, ngrid-1)
    self.position=np.array([x_init,y_init],dtype=int)
    # self.position=np.array([int(ngrid-1),int(ngrid-1)],dtype=int)

  def check_position(self,map):
    x=self.position[0]
    y=self.position[1]
    self.state=map.return_cordinate(x,y)
    map.change_field_state(x,y)

  def action(self,map):
    self.check_position(map)
    if( self.state==1 ):
      self.direction=self.direction+1
    else:
      self.direction=self.direction-1

    if( self.direction<0 ):
      self.direction=3
    elif( self.direction>3 ):
      self.direction=0

    if( self.direction==0 ):
      if( self.position[0]==ngrid ):
        self.position[0]=0
      else:
        self.position[0]=self.position[0]+1
    elif( self.direction==1 ):
      if( self.position[1]==ngrid ):
        self.position[1]=0
      else:
        self.position[1]=self.position[1]+1
    elif( self.direction==2 ):
      if( self.position[0]==0 ):
        self.position[0]=ngrid
      else:
        self.position[0]=self.position[0]-1
    elif( self.direction==3 ):
      if( self.position[1]==0 ):
        self.position[1]=ngrid
      else:
        self.position[1]=self.position[1]-1

class gridmap:
  def __init__(self,ngrid):
    range=[-int(ngrid/2),int(ngrid/2)]
    xs=np.linspace(range[0],range[1],ngrid+1)
    ys=np.linspace(range[0],range[1],ngrid+1)
    self.grid_x,self.grid_y=np.meshgrid(xs,ys)
    self.field=np.zeros_like(self.grid_x)
    self.field[int(ngrid/2)][int(ngrid/2)+1]=1
    self.field[int(ngrid/2)+1][int(ngrid/2)]=1

  def return_cordinate(self,arg1,arg2):
    state_grid=self.field[arg1][arg2]
    return state_grid

  def change_field_state(self,arg1,arg2):
    if( self.field[arg1][arg2]==1 ):
      self.field[arg1][arg2]=0
    else:
      self.field[arg1][arg2]=1

shutil.rmtree('./figures')
os.mkdir('./figures')
shutil.rmtree('./videos')
os.mkdir('./videos')

ngrid = 100  # Size of the grid
niter = 5000 # Number of iterations
nants = 10  # Number of ants
map = gridmap(ngrid)

# Initialize two Langton's ants
ants=[]
for iant in range(nants):
  ants.append(LangtonAnt("Ant "+str(iant+1)))


for iter in range(niter):
  fig=plt.figure(figsize=(10, 10))
  plt.gca().axis('off')
  axis=fig.add_subplot(111)
  axis.set_xlim(-int(ngrid/2),int(ngrid/2))
  axis.set_ylim(-int(ngrid/2),int(ngrid/2))
  # axis.set_xticks(np.linspace(-int(ngrid/2),int(ngrid/2),ngrid+2))
  axis.tick_params(labelbottom=False, labelleft=False, labelright=False, labeltop=False)
  # axis.set_yticks(np.linspace(-int(ngrid/2),int(ngrid/2),ngrid+2))
  # axis.grid()

  for iant in range(nants):
    ant = ants[iant]
    ant.action(map)
  # ant_x = map.grid_x[ant.position[0]][ant.position[1]]
  # ant_y = map.grid_y[ant.position[0]][ant.position[1]]
  # axis.plot(ant_x, ant_y, marker='.', markersize=1, color='red')

  for i in range(ngrid):
    for j in range(ngrid):
      if map.field[i][j]==1:
        box = patches.Rectangle((map.grid_x[i][j]-0.5, map.grid_y[i][j]-0.5), 
                                1.0, 
                                1.0, 
                                linewidth=0, 
                                edgecolor='black', 
                                facecolor='black')
        axis.add_patch(box)


  figname='./figures/step'+str(iter+1).zfill(8)+'.png'
  fig.savefig(figname, dpi=70, bbox_inches='tight')
  plt.close()


path_video='./videos/video.mp4'

files = glob.glob(os.path.join('./figures', '*.png'))
files.sort()
frames=len(files)
assert frames!=0, 'not found images in ./figures'

img = cv2.imread(files[0])
h,w,channel = img.shape[:3]

codec = cv2.VideoWriter_fourcc(*'mp4v')
writer = cv2.VideoWriter(path_video, codec, 1000, (w, h),1)

bar= tqdm(total=frames, dynamic_ncols=True, desc='Creating video')
for file in files:
  img = cv2.imread(file)
  writer.write(img)
  bar.update(1)

bar.close()
writer.release()