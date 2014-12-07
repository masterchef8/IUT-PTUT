"""Stores functions and classes we could use for images computing
without taking in account actual pixels but working with matrix. Images will
probably only be treated as pixels arrays, so it will be easy to change.
"""
__author__ = 'Gabriel Augendre'


def region_growing(matrix, beginning):
    """Region growing algorithm adapted to our problem.

    :param matrix: An array filled with zeros and ones (alpha layer).
    :param beginning: Start case coordinates.
    :return: A list of pixels belonging to the region.
    """
    if len(matrix) == 0 or len(matrix[0]) == 0:
        return None
    if beginning.vert >= len(matrix) or beginning.hor >= len(matrix[0]):
        return None
    if matrix[beginning.vert][beginning.hor] == 0:
        return None

    neighbouring_pixels = [beginning]
    neighbouring_pixels.extend(
        beginning.compute_neighbours(len(matrix), len(matrix[0])))
    returned_set = set()
    returned_set.add(beginning)
    beginning.region = True

    for pixel in neighbouring_pixels:
        if matrix[pixel.vert][pixel.hor] == 1 and not pixel.region:
            returned_set.add(pixel)
            pixel.region = True
            set(neighbouring_pixels).update(
                pixel.compute_neighbours(len(matrix), len(matrix[0])))

    return returned_set


class Pixel:
    """Class used to represent a pixel with two coordinates."""
    def __init__(self, vert, hor):
        """Constructor

        :param vert: Vertical coordinate
        :param hor: Horizontal coordinate
        """
        self.hor = hor
        self.vert = vert
        self.region = False

    def compute_neighbours(self, height, width):
        """Computes the list of neighbouring pixels.

        :return: A list containing all the neighbours of the considered pixel.
        """
        neighbours = set()
        if self.hor - 1 >= 0:
            if self.vert - 1 >= 0:
                neighbours.add(Pixel(self.vert - 1, self.hor - 1))
            if self.vert + 1 < height:
                neighbours.add(Pixel(self.vert + 1, self.hor - 1))
            neighbours.add(Pixel(self.vert, self.hor - 1))
        if self.hor + 1 < width:
            if self.vert - 1 >= 0:
                neighbours.add(Pixel(self.vert - 1, self.hor + 1))
            if self.vert + 1 < height:
                neighbours.add(Pixel(self.vert + 1, self.hor + 1))
            neighbours.add(Pixel(self.vert, self.hor + 1))

        if self.vert - 1 >= 0:
            neighbours.add(Pixel(self.vert - 1, self.hor))
            neighbours.add(Pixel(self.vert + 1, self.hor))

        return neighbours

    def __repr__(self):
        return "Pixel ({}, {})".format(self.vert, self.hor)

    def __eq__(self, other):
        if other is None or not isinstance(other, Pixel):
            return False
        else:
            return self.vert == other.vert and self.hor == other.hor

    def __hash__(self):
        return hash((self.hor, self.vert))


if __name__ == "__main__":
    matrix = [[0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1],
              [1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1],
              [1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
              [0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0],
              [1, 1, 1, 1, 0, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0],
              [0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0]]
    region = region_growing(matrix, Pixel(1, 1))
    print(region)

    print(Pixel(0, 0) == Pixel(0, 0))
    print(Pixel(0, 0) == Pixel(0, 1))