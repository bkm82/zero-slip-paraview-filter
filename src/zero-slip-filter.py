#This filter applies a zero slip boundary condition to a velocity profile. 
#Inputs needed are a volume mesh with the velocity profile and a surface mesh that you would like to set the surface to zero
#It is required that the mesh points on the surface of the volume mesh line up exactly with the points of the surface mesh.
import logging
logging.basicConfig(level=logging.DEBUG)


import numpy as np
Volume_Input = inputs[0]
Wall_Input = inputs[1]

# Find all of the points in the volume mesh that are on the surface mesh by first finding all of the
# Points in the Volume_Input that are also in Wall_Input. This will create a mask vector that is the 
# same number of rows as the Volume input. If that point is on the surface it will be True, else false
#TODO create a testcase to test that the shape of the mask = the shape of the input
maskX = np.in1d(Volume_Input.Points[:,0], Wall_Input.Points[:,0])
maskY = np.in1d(Volume_Input.Points[:,1], Wall_Input.Points[:,1])
maskZ = np.in1d(Volume_Input.Points[:,2], Wall_Input.Points[:,2])
mask = maskX & maskY & maskZ

#Get the velocity from the volume input mesh
velocity = Volume_Input.PointData['Velocity']
velocity[np.where(mask),:] = 0 #For rows that are on the surface, set all of the velocity columns to zero

logging.debug(f'Input Velocity Shape {shape(velocity)}')
logging.debug(f'Mask Shape {shape(mask)}')



output.PointData.append(velocity,"Velocity")