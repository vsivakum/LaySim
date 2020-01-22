import os
import sys
#import numpy
from PIL import Image
import numpy as np
from os import path
files = [f for f in os.listdir("C:\Python27\layoutimageexamples") if path.isfile(path.join("C:\Python27\layoutimageexamples",f))]
print len(files)
ref=[[0 for x in range(82)] for x in range(82)] 
roi=[[0 for x in range(82)] for x in range(82)] 
maxc=[[0 for x in range(82)] for x in range(82)] 
minc=[[0 for x in range(82)] for x in range(82)] 
dot=[0 for x in range(len(files))]
w, h = 82, 82
refcolor = np.zeros((h, w, 3), dtype=np.uint8)
maxcolor = np.zeros((h, w, 3), dtype=np.uint8)
mincolor = np.zeros((h, w, 3), dtype=np.uint8)
with open(path.join("C:\Python27\layoutimageexamples",files[0]),'r') as reffile:
  for line in reffile:
    l1= line.strip()
    if l1 and '#' not in line:  #want to skip blank lines and lines with #
      x = int(l1.split(',')[0])
      print x
      y = int(l1.split(',')[1])
      print y  
      ref[x][y] = float(l1.split(',')[2])
      refcolor[x,y] = [255*ref[x][y],0,0]
img = Image.fromarray(refcolor, mode='RGB')
refcolor[x,y] = [255*ref[x][y],0,255-(255*ref[x][y])]
img.save('my.png')
img.show()
maxval=0
maxpos=0
maxfile=""
minval=10000000
minpos=0
minfile=""
for i in range(0,len(files)):
  dot[i]=0
  if i == 0:continue
  with open(path.join("C:\Python27\layoutimageexamples",files[i]),'r') as roifile:
    for line in roifile:
      l1= line.strip()
      if l1 and '#' not in line:
        x = int(l1.split(',')[0])
        y = int(l1.split(',')[1])
        roi[x][y] = float(l1.split(',')[2])
        dot[i]=dot[i]+(roi[x][y]*ref[x][y])
  #print i
  if dot[i] > maxval:
    if dot[i]<3646.97376543:
      maxval = dot[i]
      print maxval
      maxpos = i
      print maxpos
      maxfile = files[i]
  if dot[i] < minval:
    minval = dot[i]
    print minval
    minpos = i
    print minpos
    minfile = files[i]
print len(files)	
print path.join("C:\Python27\layoutimageexamples",files[0])
print 0
print path.join("C:\Python27\layoutimageexamples",maxfile)
print maxval
print maxpos
print path.join("C:\Python27\layoutimageexamples",minfile)
print minval
print minpos
with open(path.join("C:\Python27\layoutimageexamples",maxfile),'r') as maxf:
  for line in maxf:
    l1= line.strip()
    if l1 and '#' not in line:  #want to skip blank lines and lines with #
      x = int(l1.split(',')[0])
      y = int(l1.split(',')[1])
      maxc[x][y] = float(l1.split(',')[2])
      maxcolor[x,y] = [255*maxc[x][y],0,0]
img = Image.fromarray(maxcolor, mode='RGB')
maxcolor[x,y] = [255*maxc[x][y],0,255-(255*maxc[x][y])]
img.save('C:\Python27\layoutimageexamples\max.png')
img.show()
with open(path.join("C:\Python27\layoutimageexamples",minfile),'r') as minf:
  for line in minf:
    l1= line.strip()
    if l1 and '#' not in line:  #want to skip blank lines and lines with #
      x = int(l1.split(',')[0])
      y = int(l1.split(',')[1])
      minc[x][y] = float(l1.split(',')[2])
      mincolor[x,y] = [255*minc[x][y],0,0]
img = Image.fromarray(mincolor, mode='RGB')
mincolor[x,y] = [255*minc[x][y],0,255-(255*minc[x][y])]
img.save('C:\Python27\layoutimageexamples\min.png')
img.show()