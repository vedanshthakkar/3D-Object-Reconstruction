# 3D-Object-Reconstruction
This repository consist of python code, input and output images for generating a point cloud obtained from a depth map image of a stereo image pair. 

Prerequisites:
1. Install the pointcloud library. It can be found on https://github.com/daavoo/pyntcloud/blob/master/docs/installation.rst
2. Install OpenCV library with the following included:
   numpy
   numba
   scipy
   pandas
   matplotlib

Description of the contents:

The images 1.jpg and 2.jpg form a stereo image pair which are used as an input image to generate a depth map image. The depth map is Depth.png.

The code for generating the disparity map image (or a depth map) is named as Depth.py.
The code for generating point cloud is named as Point_Cloud_Generation. 

The generated point cloud is saved in the .ply format and is diaplayed in the software named MeshLab. This software is used to display the 3d meshes.

The output images are named as snapshot01-04.

If you need any help, please feel free to write me at vedansh.thakkar@vanderbilt.edu
