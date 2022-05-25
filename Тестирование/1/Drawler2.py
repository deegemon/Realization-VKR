import arcade
import math

class Drawler2():
    x = [0]
    y = [0]
    ple = 0
    angle_sensor = 45
    pre = 0
    scale = 2
    wall_y_left = []
    wall_x_left = []
    wall_y_right = []
    wall_x_right = []
    diametr = 5.6
    mult = 2
    tick_to_circle = 374

    def __init__(self):
        super().__init__()
        

    def setup(self):
        #Установить бэкграунда
        self.read_data()
        pass

    def read_data(self):
        file = open("Data.txt")
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
        file.close()
        #print(self.wall_x_right, '\n', self.wall_y_right)
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
        if rdist * self.mult > 200:
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
        if abs(degree) > 89 and abs(degree) < 91:
            self.x.append(self.x[-1])
        elif abs(degree) < 179 and abs(degree) > 1:
            self.x.append(self.x[-1]+math.cos(degree / 180 * math.pi) * self.dist_by_encoder(le, re))
        else:
            self.x.append(self.x[-1]+ self.dist_by_encoder(le, re))
        #self.x+=math.cos(degree / 180 * math.pi) * self.dist_by_encoder(le, re)
        pass

    def dist_by_encoder(self, le, re):
        return (((le+re)/2 - (self.ple+self.pre)/2) * math.pi * self.diametr) / self.tick_to_circle

    def counting_y_mr(self, le, re, degree):
        if abs(degree) > 89 and abs(degree) < 91:
            self.y.append(self.y[-1] + self.dist_by_encoder(le, re))
        elif abs(degree) < 179 and abs(degree) > 1:
            self.y.append(self.y[-1]+math.sin(degree / 180 * math.pi) * self.dist_by_encoder(le, re))
        else:
            self.y.append(self.y[-1])
        #self.y+=math.sin(degree / 180 * math.pi) * self.dist_by_encoder(le, re)
        pass