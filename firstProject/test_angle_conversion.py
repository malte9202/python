import unittest
from angle_conversion import angle_conversion

def test_rad_to_degree():
    conversion_type = 1
    angle_to_convert = 0.6
    assert angle_conversion(conversion_type, angle_to_convert) == 34.38 #Should be 34.38

def test_degree_to_rad():
    conversion_type = 2
    angle_to_convert = 90
    assert angle_conversion(conversion_type, angle_to_convert) == 1.57 #Should be 1.57