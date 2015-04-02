try:
    from osgeo import gdal
    from osgeo import osr
except ImportError:
    import gdal
  
import sys

"""
Input : longitude : float
Input : latitude : float
Input : filename : georeferenced image

Auteur : Phylante

Tells to which pixel in the dataset the coordinates belongs.
"""
  
# =============================================================================
def Usage():
    print 'Usage : px_to_coord abscissa ordinate filename'
    sys.exit( 1 )
  
# =============================================================================
  
abscissa = None
ordinate = None
filename = None
  
i = 1
while i < len(sys.argv):
    arg = sys.argv[i]
  
    if abscissa is None:
        abscissa = int(arg)
  
    elif ordinate is None:
        ordinate = int(arg)
  
    elif filename is None:
        filename = arg
  
    else:
        Usage()
  
    i = i + 1
  
if abscissa is None:
    Usage()
if ordinate is None:
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
X = abscissa
Y = ordinate
  
# Read geotransform matrix and calculate corresponding pixel coordinates
geomatrix = ds.GetGeoTransform()
x = int(geomatrix[0] + geomatrix[1] * X + geomatrix[2] * Y)
y = int(geomatrix[3] + geomatrix[4] * X + geomatrix[5] * Y)
  
print('x=%d, y=%d' % (x, y))