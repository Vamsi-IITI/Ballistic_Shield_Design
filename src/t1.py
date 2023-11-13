## Main parameters
cell_size = 0.006
cell_wall_thickness = 0.002
node_length = 0.004
facesheet_thickness = 0.005

# Fixed constants
structure_length = 0.1
structure_breadth = 0.1

# Import libraries
import numpy as np
import matplotlib.pyplot as plt

# Additional calculation 
L = cell_size/ np.sqrt(3)
offset_x = cell_size + cell_wall_thickness
offset_y = 1.5*L + cell_wall_thickness*(np.sin(np.pi/3))
Nx = int(structure_length / offset_x) + 1
Ny = int(structure_breadth / offset_y) + 1

from ansys.mapdl.core import launch_mapdl

# start mapdl
mapdl = launch_mapdl()
print(mapdl)

## reset mapdl
mapdl.clear()

## enter the preprocessor
mapdl.prep7()

mapdl.units('SI')      # SI unit system

## Create geometry of honeycomb core
mapdl.block(0, structure_length, 0, structure_breadth, 0, node_length)
for i in range(0,Nx):                                                                                   ## column number
    for j in range(0,Ny):
        if j%2 == 0:                                                                                    ## even row number
            mapdl.rpr4(6, i*offset_x , j*offset_y, L, 90, node_length)
        else:                                                                                           ## odd row number
            mapdl.rpr4(6, i*offset_x + offset_x/2 , j*offset_y, L, 90, node_length)
mapdl.vsbv(1,'all')
honeycomb_core = mapdl.cm("CORE", "VOLU")

## Generate geometry of facesheets
front_facesheet = mapdl.block(0, structure_length, 0, structure_breadth, node_length, node_length + facesheet_thickness)  ## Top facesheet
rear_facesheet = mapdl.block(0, structure_length, 0, structure_breadth, -1*facesheet_thickness, 0)                        ## Bottom facesheet

mapdl.clocal( 11, 0, structure_length/2, structure_breadth/2, 0)                                         ## Making local coordinate system
mapdl.wpcsys('', 11,)                                                                                    ## Shift working plane

initial_distance = node_length + facesheet_thickness + 0.02                                              ## 20 mm from center of front facesheet of sandwich panel

# Generate Geometry of 0.44 Remington Magnum Bullet
mapdl.cone(0.0052, 0.005486, initial_distance , initial_distance + 0.00825)
mapdl.cone(0.00569, 0.005805, initial_distance + 0.00825 , initial_distance + 0.04089 )
mapdl.vadd(3,4)
bullet = mapdl.cm("BULLET","VOLU")

mapdl.vplot('all')

## Define material properties
mapdl.mp("EX", 1, 2e5)  # Youngs modulus
mapdl.mp("PRXY", 1, 0.3367)  # Poissons ratio

## Define element attributes
mapdl.et(1, "SOLID185") # 3D 8-Node Layered Solid

## Define mesh controls

mapdl.lesize("ALL", 0.001, layer1=1)
# mapdl.smrtsize(1)

# Mesh facesheets
mapdl.mshape(0, "3D")    # mesh the volume with 3D Hexahedral elements
mapdl.mshkey(1)          # mapped mesh
mapdl.vmesh('2')
mapdl.mshape(0, "3D")    # mesh the volume with 3D Hexahedral elements
mapdl.mshkey(1)          # mapped mesh
mapdl.vmesh('1')

# Mesh honeycomb core
mapdl.mshape(1, "3D")    # mesh the volume with 3D Tetrahedral elements
mapdl.mshkey(0)          # free mesh
mapdl.vmesh('CORE')

# Mesh bullet
mapdl.mshape(1, "3D")    # mesh the volume with 3D Tetrahedral elements
mapdl.mshkey(0)          # free mesh
mapdl.vmesh('BULLET')