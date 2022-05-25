import arcade
import math

class Drawler2(arcade.Window):
    def __init__(self, w, h):
        super().__init__(w,h)
        self.x = [0]
        self.y = [0]
        self.maxDistToWall = 100
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
        self.file = open("C:/TRIKStudio/NewData.txt")

    def setup(self):
        #Установить бэкграунда
        arcade.set_background_color(arcade.color.WHITE)
        self.read_data()
        pass

    def on_draw(self):
        arcade.start_render()
        self.draw_robot_way()
        self.draw_left_wall()
        self.draw_right_wall()
        pass
    def update(self, delta_time):
        pass

    def draw_left_wall(self):
        midX = self.width // 2
        midY = self.height // 2
        for i in range(len(self.wall_x_left)-1):
            if self.wall_x_left[i+1] == -1 or self.wall_x_left[i] == -1:
                continue
            sX = midX + self.wall_x_left[i]/self.scale
            sY = midY - self.wall_y_left[i]/self.scale
            
            eX = midX + self.wall_x_left[i+1]/self.scale
            eY = midY - self.wall_y_left[i+1]/self.scale
            arcade.draw_line(sX, sY, eX, eY, arcade.color.BLACK, 1)
        pass

    def draw_right_wall(self):
        midX = self.width // 2
        midY = self.height // 2
        for i in range(len(self.wall_x_right)-1):
            if self.wall_x_right[i+1] == -1 or self.wall_x_right[i] == -1:
                continue
            sX = midX + self.wall_x_right[i]/self.scale
            sY = midY - self.wall_y_right[i]/self.scale
            
            eX = midX + self.wall_x_right[i+1]/self.scale
            eY = midY - self.wall_y_right[i+1]/self.scale
            arcade.draw_line(sX, sY, eX, eY, arcade.color.BLACK, 1)
        pass

    def draw_robot_way(self):
        midX = self.width // 2
        midY = self.height // 2
        for i in range(len(self.x)-1):
            sX = midX + self.x[i]/self.scale
            sY = midY - self.y[i]/self.scale
            
            eX = midX + self.x[i+1]/self.scale
            eY = midY - self.y[i+1]/self.scale
            arcade.draw_line(sX, sY, eX, eY, arcade.color.RED, 2)
        pass

    def read_data(self):
        file = open("C:/TRIKStudio/NewData.txt")
        for line in file:
            re = int(line.split(' ')[0])
            le = int(line.split(' ')[1])
            degree = float(line.split(' ')[2])
            rdist = int(line.split(' ')[3])
            ldist = int(line.split(' ')[4])
            if ldist < 300:
                print(ldist)
            self.counting_x_mr(le, re, degree)
            self.counting_y_mr(le, re, degree)

            self.check_left_wall(ldist/self.mult, degree)
            self.check_right_wall(rdist/self.mult, degree)
            self.ple = le
            self.pre = re
        #print(self.wall_x_left, self.wall_y_left)
        pass

    def check_left_wall(self, ldist, degree):
        if ldist * self.mult  > self.maxDistToWall:
            self.wall_y_left.append(-1)
            self.wall_x_left.append(-1)
            return
        angle = degree - self.angle_sensor
        if abs(angle) > 89 and abs(angle) < 91:
            self.wall_x_left.append(self.x[-1])
            self.wall_y_left.append(self.y[-1] + ldist * self.mult*math.sin(angle / 180 * math.pi))
        elif abs(angle) < 179 and abs(angle) > 1:
            self.wall_x_left.append(self.x[-1] + ldist * self.mult*math.cos(angle / 180 * math.pi))
            self.wall_y_left.append(self.y[-1] + ldist * self.mult*math.sin(angle / 180 * math.pi))
        else:
            self.wall_x_left.append(self.x[-1] + ldist * self.mult*math.cos(angle / 180 * math.pi))
            self.wall_y_left.append(self.y[-1])

    def check_right_wall(self, rdist, degree):
        if rdist * self.mult > self.maxDistToWall:
            self.wall_y_right.append(-1)
            self.wall_x_right.append(-1)
            return
        angle = degree + self.angle_sensor
        
        if abs(angle) > 89 and abs(angle) < 91:
            self.wall_x_right.append(self.x[-1])
            self.wall_y_right.append(self.y[-1] + rdist * self.mult*math.sin(angle / 180 * math.pi))
        elif abs(angle) < 179 and abs(angle) > 1:
            self.wall_x_right.append(self.x[-1] + rdist * self.mult*math.cos(angle / 180 * math.pi))
            self.wall_y_right.append(self.y[-1] + rdist * self.mult*math.sin(angle / 180 * math.pi))
        else:
            self.wall_x_right.append(self.x[-1] + rdist * self.mult*math.cos(angle / 180 * math.pi))
            self.wall_y_right.append(self.y[-1])
    def counting_x_mr(self, le, re, degree):
        self.x.append(self.x[-1]+math.cos(degree / 180 * math.pi) * self.dist_by_encoder(le, re))
        pass

    def dist_by_encoder(self, le, re):
        return (((le+re)/2 - (self.ple+self.pre)/2) * math.pi * self.diametr) / self.tick_to_circle

    def counting_y_mr(self, le, re, degree):
        self.y.append(self.y[-1]+math.sin(degree / 180 * math.pi) * self.dist_by_encoder(le, re))
        #self.y+=math.sin(degree / 180 * math.pi) * self.dist_by_encoder(le, re)
        pass
window = Drawler2(1000, 750)
window.setup()
arcade.run()