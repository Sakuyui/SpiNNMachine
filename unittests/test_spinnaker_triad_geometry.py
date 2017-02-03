import unittest
from spinn_machine import spinnaker_triad_geometry as geom


class TestingGeometry(unittest.TestCase):
    def test_geom(self):
        # This table was produced using the code in Rig
        delta_table = [
            [(0, 0), (-1, 0), (-2, 0), (-3, 0), (-4, 0), (-1, -4),
             (-2, -4), (-3, -4), (-4, -4), (-5, -4), (-6, -4), (-7, -4)],
            [(0, -1), (-1, -1), (-2, -1), (-3, -1), (-4, -1), (-5, -1),
             (-2, -5), (-3, -5), (-4, -5), (-5, -5), (-6, -5), (-7, -5)],
            [(0, -2), (-1, -2), (-2, -2), (-3, -2), (-4, -2), (-5, -2),
             (-6, -2), (-3, -6), (-4, -6), (-5, -6), (-6, -6), (-7, -6)],
            [(0, -3), (-1, -3), (-2, -3), (-3, -3), (-4, -3), (-5, -3),
             (-6, -3), (-7, -3), (-4, -7), (-5, -7), (-6, -7), (-7, -7)],
            [(-4, 0), (-1, -4), (-2, -4), (-3, -4), (-4, -4), (-5, -4),
             (-6, -4), (-7, -4), (0, 0), (-1, 0), (-2, 0), (-3, 0)],
            [(-4, -1), (-5, -1), (-2, -5), (-3, -5), (-4, -5), (-5, -5),
             (-6, -5), (-7, -5), (0, -1), (-1, -1), (-2, -1), (-3, -1)],
            [(-4, -2), (-5, -2), (-6, -2), (-3, -6), (-4, -6), (-5, -6),
             (-6, -6), (-7, -6), (0, -2), (-1, -2), (-2, -2), (-3, -2)],
            [(-4, -3), (-5, -3), (-6, -3), (-7, -3), (-4, -7), (-5, -7),
             (-6, -7), (-7, -7), (0, -3), (-1, -3), (-2, -3), (-3, -3)],
            [(-4, -4), (-5, -4), (-6, -4), (-7, -4), (0, 0), (-1, 0),
             (-2, 0), (-3, 0), (-4, 0), (-1, -4), (-2, -4), (-3, -4)],
            [(-4, -5), (-5, -5), (-6, -5), (-7, -5), (0, -1), (-1, -1),
             (-2, -1), (-3, -1), (-4, -1), (-5, -1), (-2, -5), (-3, -5)],
            [(-4, -6), (-5, -6), (-6, -6), (-7, -6), (0, -2), (-1, -2),
             (-2, -2), (-3, -2), (-4, -2), (-5, -2), (-6, -2), (-3, -6)],
            [(-4, -7), (-5, -7), (-6, -7), (-7, -7), (0, -3), (-1, -3),
             (-2, -3), (-3, -3), (-4, -3), (-5, -3), (-6, -3), (-7, -3)]]
        g = geom.SpiNNakerTriadGeometry.get_spinn5_geometry()
        for x in range(12):
            for y in range(12):
                px, py = delta_table[y][x]
                q = g.get_local_chip_coordinate(x, y)
                qx, qy = q
                self.assertEqual(
                    (-px, -py), q,
                    "x at ({},{}): expected ({},{}) but got ({},{})".format(
                        x, y, -px, -py, qx, qy))

if __name__ == '__main__':
    unittest.main()
