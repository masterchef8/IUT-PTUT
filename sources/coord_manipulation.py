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


def usage_px_to_coord():
    print 'Usage : px_to_coord abscissa ordinate filename'
    sys.exit(1)


def usage_coord_to_px():
    print 'Usage : coord_to_px longitude latitude filename'
    sys.exit(1)


def exit_file_error(filename):
    print 'Cannot open ' + filename
    sys.exit(1)


def px_to_coord(abscissa, ordinate, filename):
    gdal.UseExceptions()
    if abscissa is None:
        usage_px_to_coord()
    if ordinate is None:
        usage_px_to_coord()
    if filename is None:
        filename()

    # Open input dataset
    try:
        ds = gdal.Open(filename, gdal.GA_ReadOnly)
    except RuntimeError:
        exit_file_error(filename)

    if ds is None:
        exit_file_error(filename)

    # Build Spatial Reference object based on coordinate system,
    # fetched from the opened dataset
    X = abscissa
    Y = ordinate

    # Read geotransform matrix and calculate corresponding pixel coordinates
    geomatrix = ds.GetGeoTransform()
    x = int(geomatrix[0] + geomatrix[1] * X + geomatrix[2] * Y)
    y = int(geomatrix[3] + geomatrix[4] * X + geomatrix[5] * Y)

    return x, y


def coord_to_px(longitude, latitude, filename):
    if longitude is None:
        usage_coord_to_px()
    if latitude is None:
        usage_coord_to_px()
    if filename is None:
        filename()

    # Open input dataset
    try:
        ds = gdal.Open(filename, gdal.GA_ReadOnly)
    except RuntimeError:
        exit_file_error(filename)

    if ds is None:
        exit_file_error(filename)

    # Build Spatial Reference object based on coordinate system,
    # fetched from the opened dataset
    X = longitude
    Y = latitude

    # Read geotransform matrix and calculate corresponding pixel coordinates
    geomatrix = ds.GetGeoTransform()
    (success, inv_geometrix) = gdal.InvGeoTransform(geomatrix)
    x = int(inv_geometrix[0] + inv_geometrix[1] * X + inv_geometrix[2] * Y)
    y = int(inv_geometrix[3] + inv_geometrix[4] * X + inv_geometrix[5] * Y)

    if x < 0 or x >= ds.RasterXSize or y < 0 or y >= ds.RasterYSize:
        raise RuntimeError('Passed coordinates are not in dataset extent')

    return x, y
