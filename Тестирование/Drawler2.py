import math
import cv2
import numpy as np

class Drawler2():
    
    def __init__(self, width, height):
        self.x = [0]
        self.y = [0]
        self.ple = 0
        self.angle_sensor = 45
        self.pre = 0
        self.scale = 2
        self.wall_y_left = []
        self.wall_x_left = []
        self.wall_y_right = []
        self.wall_x_right = []
        self.diametr = 5.6
        self.mult = 2
        self.tick_to_circle = 374

        self.bg = np.ones((height, width, 3)) * 255
        self.width = width
        self.height = height
        super().__init__()
       

    def setup(self):
        #Установить бэкграунда
        self.read_data(open("C:/TRIKStudio/NewData.txt"))
        self.on_draw()
        pass

    def on_draw(self):
        self.draw_robot_way()
        self.draw_left_wall()
        self.draw_right_wall()
        cv2.imwrite("input.png", self.bg)
        pass
    def update(self, delta_time):
        pass

    def draw_left_wall(self):
        midX = self.width // 2
        midY = self.height // 2
        for i in range(len(self.wall_x_left)-1):
        #for i in range(30):
            if self.wall_x_left[i+1] == -1 or self.wall_x_left[i] == -1:
                continue
            sX = int(midX + self.wall_x_left[i]/self.scale)
            sY = int(midY + self.wall_y_left[i]/self.scale)
            
            eX = int(midX + self.wall_x_left[i+1]/self.scale)
            eY = int(midY + self.wall_y_left[i+1]/self.scale)
            cv2.line(self.bg, (sX, sY), (eX, eY), (0,0,0), thickness=2)
            
            #print(self.wall_x_left[i], self.x[i])
        pass

    def draw_right_wall(self):
        midX = self.width // 2
        midY = self.height // 2
        for i in range(len(self.wall_x_right)-1):
            if self.wall_x_right[i+1] == -1 or self.wall_x_right[i] == -1:
                continue
            sX = int(midX + self.wall_x_right[i]/self.scale)
            sY = int(midY +self.wall_y_right[i]/self.scale)
            
            eX = int(midX + self.wall_x_right[i+1]/self.scale)
            eY = int(midY +self.wall_y_right[i+1]/self.scale)
            cv2.line(self.bg, (sX, sY), (eX, eY), (0,0,0), thickness=2)
            #print(sX, sY, eX, eY)
        pass

    def draw_robot_way(self):
        midX = self.width // 2
        midY = self.height // 2
        for i in range(len(self.x)-1):
            sX = int(midX + self.x[i]/self.scale)
            sY = int(midY +self.y[i]/self.scale)
            
            eX = int(midX + self.x[i+1]/self.scale)
            eY = int(midY +self.y[i+1]/self.scale)
            cv2.line(self.bg, (sX, sY), (eX, eY), (0,0,255), thickness=2)
            #print(x, y)
        pass

    def read_data(self, file):
        for line in file:
            re = int(line.split(' ')[0])
            le = int(line.split(' ')[1])
            degree = float(line.split(' ')[2])
            rdist = int(line.split(' ')[3])
            ldist = int(line.split(' ')[4])
            self.counting_x_mr(le, re, degree)
            self.counting_y_mr(le, re, degree)

            self.check_left_wall(ldist/self.mult, degree)
            self.check_right_wall(rdist/self.mult, degree)
            self.ple = le
            self.pre = re
        #print(self.wall_x_right, '\n', self.wall_y_right)
        file.close()
        pass

    def check_left_wall(self, ldist, degree):
        if ldist * self.mult > 250:
            self.wall_y_left.append(-1)
            self.wall_x_left.append(-1)
            return
        angle = degree - self.angle_sensor
        #wX=rX+dist*cos(angle)
        #yX=yX-dist*sin(angle)
        if abs(angle) > 89 and abs(angle) < 91:
            self.wall_x_left.append(self.x[-1])
            self.wall_y_left.append(self.y[-1] + ldist*math.sin(angle / 180 * math.pi))
        elif abs(angle) < 179 and abs(angle) > 1:
            self.wall_x_left.append(self.x[-1] + ldist*math.cos(angle / 180 * math.pi))
            self.wall_y_left.append(self.y[-1] + ldist*math.sin(angle / 180 * math.pi))
        else:
            self.wall_x_left.append(self.x[-1] + ldist*math.cos(angle / 180 * math.pi))
            self.wall_y_left.append(self.y[-1])

    def check_right_wall(self, rdist, degree):
        if rdist * self.mult > 250:
            self.wall_y_right.append(-1)
            self.wall_x_right.append(-1)
            return
        angle = degree + self.angle_sensor
        
        if abs(angle) > 89 and abs(angle) < 91:
            self.wall_x_right.append(self.x[-1])
            self.wall_y_right.append(self.y[-1] + rdist*math.sin(angle / 180 * math.pi))
        elif abs(angle) < 179 and abs(angle) > 1:
            self.wall_x_right.append(self.x[-1] + rdist*math.cos(angle / 180 * math.pi))
            self.wall_y_right.append(self.y[-1] + rdist*math.sin(angle / 180 * math.pi))
        else:
            self.wall_x_right.append(self.x[-1] + rdist*math.cos(angle / 180 * math.pi))
            self.wall_y_right.append(self.y[-1])
    def counting_x_mr(self, le, re, degree):
        self.x.append(self.x[-1]+math.cos(degree / 180 * math.pi) * self.dist_by_encoder(le, re))
        #self.x+=math.cos(degree / 180 * math.pi) * self.dist_by_encoder(le, re)
        pass

    def dist_by_encoder(self, le, re):
        return (((le+re)/2 - (self.ple+self.pre)/2) * math.pi * self.diametr) / self.tick_to_circle

    def counting_y_mr(self, le, re, degree):
        self.y.append(self.y[-1]+math.sin(degree / 180 * math.pi) * self.dist_by_encoder(le, re))
        #self.y+=math.sin(degree / 180 * math.pi) * self.dist_by_encoder(le, re)
        pass
window = Drawler2(430, 370)
window.setup()