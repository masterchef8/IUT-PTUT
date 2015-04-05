# -*- coding: utf-8 -*- 

"""
Created by Phylante

Input : longitude : float
Input : latitude : float
Input : filename : georeferenced image

Source : http://nullege.com/codes/show/src%40g%40d%40GDAL-1.10.0%40samples%40val_at_coord.py/36/gdal/python#

Tells to which pixel in the dataset the coordinates belongs.
"""



try:
    from osgeo import gdal
    from osgeo import osr
except ImportError:
    import gdal
  
import sys


  
# =============================================================================
def Usage():
    print 'Usage : coord_to_px longitude latitude filename'
    sys.exit( 1 )
  
# =============================================================================
  
longitude = None
latitude = None
filename = None
  
i = 1
while i < len(sys.argv):
    arg = sys.argv[i]
  
    if longitude is None:
        longitude = float(arg)
  
    elif latitude is None:
        latitude = float(arg)
  
    elif filename is None:
        filename = arg
  
    else:
        Usage()
  
    i = i + 1
  
if longitude is None:
    Usage()
if latitude is None:
    Usage()
if filename is None:
    filename()
  
# Open input dataset
ds = gdal.Open( filename, gdal.GA_ReadOnly )
if ds is None:
    print('Cannot open %s' % filename)
    sys.exit(1)
  
# Build Spatial Reference object based on coordinate system, fetched from the
# opened dataset
X = longitude
Y = latitude
  
# Read geotransform matrix and calculate corresponding pixel coordinates
geomatrix = ds.GetGeoTransform()
(success, inv_geometrix) = gdal.InvGeoTransform(geomatrix)
x = int(inv_geometrix[0] + inv_geometrix[1] * X + inv_geometrix[2] * Y)
y = int(inv_geometrix[3] + inv_geometrix[4] * X + inv_geometrix[5] * Y)
  
print('x=%d, y=%d' % (x, y))
  
if x < 0 or x >= ds.RasterXSize or y < 0 or y >= ds.RasterYSize:
    print('Passed coordinates are not in dataset extent')
    sys.exit(1)


