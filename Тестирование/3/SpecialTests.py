import unittest
import sys, os
import time
sys.path.insert(1, '../')
from Drawler2 import Drawler2 as testClass
import cv2

class SpecialTest(unittest.TestCase):
    def test_s1(self):
        file = open("data.txt", 'w')
        re = le = 0
        for i in range(1000):
            txt = "{0} {1} 0 30 3000\n".format(le, re)
            if le > 99:
                le-=100;re-=100
            le+=100;re+=100
            file.write(txt)
        file.close()
        
        start = time.time()
        tst = testClass(200,200)
        tst.read_data(open("data.txt"))
        tst.draw_robot_way()
        tst.draw_left_wall()
        tst.draw_right_wall()
        cv2.imwrite("test1.png", tst.bg)
        finish = time.time()
        print(f'Файл: {os.path.getsize("data.txt")} бит, время работы: {finish - start}, удовлетворяет условию: {finish - start < 1}')
        self.assertEqual(finish-start < 0.1, True, "1 special test")

    def test_s2(self):
        file = open("data2.txt", 'w')
        re = le = 0
        for i in range(100000):
            txt = "{0} {1} 0 30 3000\n".format(le, re)
            if le > 99:
                le-=100;re-=100
            le+=100;re+=100
            file.write(txt)
        file.close()
        
        start = time.time()
        tst = testClass(200,200)
        tst.read_data(open("data2.txt"))
        tst.draw_robot_way()
        tst.draw_left_wall()
        tst.draw_right_wall()
        cv2.imwrite("test1.png", tst.bg)
        finish = time.time()
        print(f'Файл: {os.path.getsize("data.txt")} бит, время работы: {finish - start}, удовлетворяет условию: {finish - start < 1}')
        self.assertEqual(finish-start < 2, True, "2 special test")

    def test_s3(self):
        file = open("data3.txt", 'w')
        re = le = 0
        for i in range(1000000):
            txt = "{0} {1} 0 30 3000\n".format(le, re)
            if le > 99:
                le-=100;re-=100
            le+=100;re+=100
            file.write(txt)
        file.close()
        
        start = time.time()
        tst = testClass(200,200)
        tst.read_data(open("data3.txt"))
        tst.draw_robot_way()
        tst.draw_left_wall()
        tst.draw_right_wall()
        cv2.imwrite("test1.png", tst.bg)
        finish = time.time()
        print(f'Файл: {os.path.getsize("data.txt")} бит, время работы: {finish - start}, удовлетворяет условию: {finish - start < 1}')
        self.assertEqual(finish-start < 20, True, "1 special test")


unittest.main()