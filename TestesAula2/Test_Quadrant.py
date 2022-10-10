from Coordinate import Coordinate
from Quadrant import Quadrant


def test_one():
    # Arrange / Setup
    a = 12             #
    b = 8
    coordinates = Coordinate(a, b)
    quadrant = Quadrant(coordinates)

    # Act / Action
    result = quadrant.get_quadrant_coordinate()

    # Assert
    assert result == "First"


def test_two():
    # Arrange / Setup
    a = -6             
    b = 9
    coordinates = Coordinate(a, b)
    quadrant = Quadrant(coordinates)

    # Act / Action
    result = quadrant.get_quadrant_coordinate()

    # Assert
    assert result == "Second"

def test_three():
    # Arrange / Setup
    a = -20
    b = -36
    coordinates = Coordinate(a, b)
    quadrant = Quadrant(coordinates)

    # Act / Action
    result = quadrant.get_quadrant_coordinate()

    # Assert
    assert result == "Third"


def test_four():
    # Arrange / Setup
    a = 6
    b = -10
    coordinates = Coordinate(a, b)
    quadrant = Quadrant(coordinates)

    # Act / Action
    result = quadrant.get_quadrant_coordinate()

    # Assert
    assert result == "Fourth"



