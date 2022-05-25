import unittest
import os
import sys
sys.path.insert(1, '../')
from Drawler2 import Drawler2 as testClass
import cv2
from PIL import Image, ImageChops

class IntegrationTest(unittest.TestCase):
    def test_integration1(self):
        tst = testClass(200, 200)
        tst.read_data(open("data1.txt"))
        tst.draw_robot_way()
        tst.draw_left_wall()
        tst.draw_right_wall()
        cv2.imwrite("test1.png", tst.bg)
        img1 = Image.open("input1.png")
        img2 = Image.open("test1.png")
        self.assertEqual(ImageChops.difference(img1, img2).getbbox(), None, "Integration test 1")
        os.remove("test1.png")
        pass
    
    def test_integration2(self):
        tst = testClass(400, 200)
        tst.read_data(open("data2.txt"))
        tst.draw_robot_way()
        tst.draw_left_wall()
        tst.draw_right_wall()
        cv2.imwrite("test2.png", tst.bg)
        img1 = Image.open("input2.png")
        img2 = Image.open("test2.png")
        self.assertEqual(ImageChops.difference(img1, img2).getbbox(), None, "Integration test 2")
        os.remove("test2.png")
        pass

    def test_integration3(self):
        tst = testClass(400, 200)
        tst.read_data(open("data3.txt"))
        tst.draw_robot_way()
        tst.draw_left_wall()
        tst.draw_right_wall()
        cv2.imwrite("test3.png", tst.bg)
        img1 = Image.open("input3.png")
        img2 = Image.open("test3.png")
        self.assertEqual(ImageChops.difference(img1, img2).getbbox(), None, "Integration test 3")
        os.remove("test3.png")
        pass

    def test_integration4(self):
        tst = testClass(400, 200)
        tst.read_data(open("data4.txt"))
        tst.draw_robot_way()
        tst.draw_left_wall()
        tst.draw_right_wall()
        cv2.imwrite("test4.png", tst.bg)
        img1 = Image.open("input4.png")
        img2 = Image.open("test4.png")
        self.assertEqual(ImageChops.difference(img1, img2).getbbox(), None, "Integration test 4")
        
        os.remove("test4.png")
        pass

    def test_integration_by_defoult_data(self):
        tst = testClass(430, 370)
        tst.read_data(open("C:/TRIKStudio/NewData.txt"))
        tst.draw_robot_way()
        tst.draw_left_wall()
        tst.draw_right_wall()
        cv2.imwrite("test.png", tst.bg)
        img1 = Image.open("input.png")
        img2 = Image.open("test.png")
        self.assertEqual(ImageChops.difference(img1, img2).getbbox(), None, "Integration test by normal Data")
        os.remove("test.png")


#unittest.main()