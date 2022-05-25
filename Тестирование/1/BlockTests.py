import unittest
from Drawler2 import Drawler2 as tests
import math


#tests wallchecking, xycounting, distbyencoder
class TestBlock(unittest.TestCase):
    def test_NegativeWallLeft1(self):
        test = tests()
        test.check_left_wall(201, 45)
        self.assertEqual(-1, test.wall_y_left[0], "Test wall left Y1")
        self.assertEqual(-1, test.wall_x_left[0], "Test wall left X1")
        pass

    def test_NegativeWallLeft2(self):
        test = tests()
        test.check_left_wall(220, 170)
        self.assertEqual(-1, test.wall_y_left[0], "Test wall left Y1")
        self.assertEqual(-1, test.wall_x_left[0], "Test wall left X1")
        pass

    def test_NegativeWallLeft3(self):
        test = tests()
        pid = math.pi * test.diametr
        test.check_left_wall(201, 45)
        test.counting_x_mr(374/pid, 374/pid, 90)
        test.counting_y_mr(374/pid, 374/pid, 90)
        self.assertEqual(-1, test.wall_y_left[0], "Test wall left Y1")
        self.assertEqual(-1, test.wall_x_left[0], "Test wall left X1")
        pass

    def test_PositiveWallLeft1(self):
        test = tests()
        pid = math.pi * test.diametr
        test.counting_x_mr(374/pid, 374/pid, 90)
        test.counting_y_mr(374/pid, 374/pid, 90)
        test.check_left_wall(100, 45)
        self.assertEqual(1, test.wall_y_left[0], "Test wall left Y1")
        self.assertEqual(100, test.wall_x_left[0], "Test wall left X1")
        pass

    def test_PositiveWallLeft2(self):
        test = tests()
        pid = math.pi * test.diametr
        for i in range(3):
            test.counting_x_mr(374/pid, 374/pid, 90)
            test.counting_y_mr(374/pid, 374/pid, 90)
        test.check_left_wall(100, 45)
        self.assertEqual(3, test.wall_y_left[0], "Test wall left Y2")
        self.assertEqual(100, test.wall_x_left[0], "Test wall left X2")
        pass

    def test_PositiveWallLeft3(self):
        test = tests()
        pid = math.pi * test.diametr
        for i in range(3):
            test.counting_x_mr(374/pid, 374/pid, 90)
            test.counting_y_mr(374/pid, 374/pid, 90)
            test.check_left_wall(100, 45)
        self.assertEqual(1, test.wall_y_left[0], "Test wall left Y3")
        self.assertEqual(100, test.wall_x_left[0], "Test wall left X3")
        self.assertEqual(3, len(test.wall_x_left), "Test wall left len")
        self.assertEqual(3, len(test.wall_y_left), "Test wall left len")
        pass

    #
    def test_NegativeWallRight1(self):
        test = tests()
        test.check_right_wall(201, 45)
        self.assertEqual(-1, test.wall_y_right[0], "Test wall left Y1")
        self.assertEqual(-1, test.wall_x_right[0], "Test wall left X1")
        pass

    def test_NegativeWallRight2(self):
        test = tests()
        test.check_right_wall(999, 0)
        self.assertEqual(-1, test.wall_y_right[0], "Test wall left Y1")
        self.assertEqual(-1, test.wall_x_right[0], "Test wall left X1")
        pass

    def test_NegativeWallRight3(self):
        test = tests()
        pid = math.pi * test.diametr
        test.check_right_wall(201, 45)
        test.counting_x_mr(374/pid, 374/pid, 90)
        test.counting_y_mr(374/pid, 374/pid, 90)
        self.assertEqual(-1, test.wall_y_right[0], "Test wall left Y1")
        self.assertEqual(-1, test.wall_x_right[0], "Test wall left X1")
        pass

    def test_PositiveWallRight1(self):
        test = tests()
        pid = math.pi * test.diametr
        test.counting_x_mr(374/pid, 374/pid, 90)
        test.counting_y_mr(374/pid, 374/pid, 90)
        test.check_right_wall(100, 45)
        self.assertEqual(101, test.wall_y_right[0], "Test wall left Y1")
        self.assertEqual(0, test.wall_x_right[0], "Test wall left X1")
        pass

    def test_PositiveWallRight2(self):
        test = tests()
        pid = math.pi * test.diametr
        for i in range(3):
            test.counting_x_mr(374/pid, 374/pid, 90)
            test.counting_y_mr(374/pid, 374/pid, 90)
        test.check_right_wall(100, 45)
        self.assertEqual(103, test.wall_y_right[0], "Test wall right Y2")
        self.assertEqual(0, test.wall_x_right[0], "Test wall right X2")
        pass

    def test_PositiveWallRight3(self):
        test = tests()
        pid = math.pi * test.diametr
        for i in range(3):
            test.counting_x_mr(374/pid, 374/pid, 90)
            test.counting_y_mr(374/pid, 374/pid, 90)
            test.check_right_wall(100, 45)
        self.assertEqual(103, test.wall_y_right[2], "Test wall right Y3")
        self.assertEqual(0, test.wall_x_right[0], "Test wall right X3")
        self.assertEqual(3, len(test.wall_y_right), "Test wall right len")
        self.assertEqual(3, len(test.wall_x_right), "Test wall right len")
        pass

    def test_PositiveTestXYcounting1(self):
        test = tests()
        pid = math.pi * test.diametr
        test.counting_x_mr(374/pid, 374/pid, 0)
        test.counting_y_mr(374/pid, 374/pid, 0)
        self.assertEqual(1, test.x[1], "Test counting X1")
        self.assertEqual(0, test.y[1], "Test counting Y1")
        pass

    def test_PositiveTestXYcounting2(self):
        #self.x.append(self.x[-1]+math.cos(degree / 180 * math.pi) * self.dist_by_encoder(le, re))
        test = tests()
        pid = math.pi * test.diametr
        test.counting_x_mr(374/pid, 374/pid, 90)
        test.counting_y_mr(374/pid, 374/pid, 90)
        self.assertEqual(0, test.x[1], "Test counting X2")
        self.assertEqual(1, test.y[1], "Test counting Y2")
        pass

    def test_PositiveTestXYcounting3(self):
        #self.x.append(self.x[-1]+math.cos(degree / 180 * math.pi) * self.dist_by_encoder(le, re))
        test = tests()
        pid = math.pi * test.diametr
        test.counting_x_mr(374/pid, 374/pid, 90)
        test.counting_y_mr(374/pid, 374/pid, 90)
        test.counting_x_mr(374/pid, 374/pid, 60)
        test.counting_y_mr(374/pid, 374/pid, 60)
        self.assertEqual(0.5, round(test.x[2], 2), "Test counting X2")
        self.assertEqual(1.87, round(test.y[2], 2), "Test counting Y2")
        pass

    def test_PositiveDataEncoderToDistance1(self):
        pid = math.pi * tests().diametr
        self.assertEqual(tests().dist_by_encoder(374/pid,374/pid), 1,"Test EncoderToDistance1")
        pass

    def test_PositiveDataEncoderToDistance2(self):
        pid = math.pi * tests().diametr
        self.assertEqual(tests().dist_by_encoder(187/pid,187/pid), 0.5,"Test EncoderToDistance2")
        pass

    def test_PositiveDataEncoderToDistance3(self):
        pid = math.pi * tests().diametr
        self.assertEqual(tests().dist_by_encoder(374/pid,374/pid), 1,"Test EncoderToDistance3")
        pass

unittest.main()