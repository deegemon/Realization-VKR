import sys
import time
import random
import math

#Проблема с направлением, робот оказывается снизу потому что он хз почему на самом деле надо думать
class Program():
  __interpretation_started_timestamp__ = time.time() * 1000
  maxDistanceToWallReading = 100
  minDistanceToWall = 7
  zacepDist = 30
  #Приемлимое отклонение
  priemotkl = 3
  #коэфициент уравнение y = kx + b  
  k=0
  b=0
  #Координаты конечной точки назначения
  toX=250
  toY=100
  #Расстояние до стены, на котором будет двигаться робот
  reqDistanceToWall = 20
  #pi = 3.141592653589793
  X=Y=0
  #мощность моторов
  power = 20
  #Значения датчиков расстояние
  dataLeft = brick.sensor(D1).read()
  dataRight = brick.sensor(D2).read()
  #Диаметр колеса робота
  diametr = 5.6
  
  def execMain(self):
    #Поставить робота на начальные координаты
    
    self.k = self.toX/self.toY
    print(self.k)

    open("NewData.txt", 'w')
    #Повернуть робота на угол
    self.startAngle = math.atan(self.toY/self.toX)/math.pi * 180
    self.RotateToAngle(self.startAngle)
    print(self.X, self.Y)
    #Проехать в прямом направлении на расстояние
    self.Moving(math.sqrt(self.toX**2+self.toY**2))
    print(self.X, self.Y)
    brick.stop()
    return
    
  def WallMoving(self):
    print("цепка")
    minDist = 30
    tick = (brick.encoder(E3).read() + brick.encoder(E4).read())/2
    differencePower = 10
    #Левая стена
    
    
    while self.CheckDistance(self.dataLeft):
      #Нужны проверки на свободность пространства
      if self.dataRight == 150:
        #Если предполагемый x будет больше, чем финальная точка и слева нет препядствий уходим от стены
        x = self.X + 50 * math.cos((-brick.gyroscope().read()[6]/1000-45)/180*math.pi)
        y = self.Y + 50 * math.sin((-brick.gyroscope().read()[6]/1000-45)/180*math.pi)
        if (x > self.toX or y > self.toY) and self.X < self.toX:
          return
      #Проверка на возвращение к прямой функции
      if abs(self.Y-self.X*self.k-self.b) < 0.1:
        #Нужно ли уходить от стены или продолжать движение
        if self.Y > self.toY:
          return
      
      #Стандартные мощности колёс
      pL = pR = self.power
      #обновление данных с датчиков расстояний
      self.dataLeft = brick.sensor(D1).read()
      self.dataRight = brick.sensor(D2).read()
      #Изменить положение робота
      tick = self.ChangePositionRobot(tick)
      #Минимальное расстояние до стены, для "прикрепления" робота к ней
      if self.dataLeft <= minDist:
        #Расстояние до стены больше рекомендуемого
        if self.dataLeft > self.reqDistanceToWall:
          pL -= differencePower / 2
          pR += differencePower / 2
        elif self.dataLeft < self.reqDistanceToWall:
          pL += differencePower / 2
          pR -= differencePower / 2
      brick.motor(M4).setPower(pL)
      brick.motor(M3).setPower(pR)
      script.wait(50)
      
    #Правая стена
    while self.CheckDistance(self.dataRight):
      #Нужны проверки на свободность пространства
      if self.dataLeft == 150:
        #Если предполагемый x будет больше, чем финальная точка и слева нет препядствий уходим от стены
        x = self.X + 50 * math.cos((-brick.gyroscope().read()[6]/1000+45)/180*math.pi)
        y = self.Y + 50 * math.sin((-brick.gyroscope().read()[6]/1000+45)/180*math.pi)
        if (x > self.toX or y > self.toY) and self.Y < self.toY:
          return
      #Проверка на возвращение к прямой функции
      if (abs(self.Y-self.X*self.k-self.b) < 0.1):
        print("Вернулся")
        if self.Y > self.toY:
          return
      #Аналогично левой стене
      #Стандартные мощности колёс
      pL = pR = self.power
      #обновление данных с датчиков расстояний
      self.dataLeft = brick.sensor(D1).read()
      self.dataRight = brick.sensor(D2).read()
      #Изменить положение робота
      tick = self.ChangePositionRobot(tick)
      #Минимальное расстояние до стены, для "прикрепления" робота к ней
      if self.dataRight <= minDist:
        #Если рекомендуемое расстояние до стены отличается от текущего, с небольшой разницей
        if not self.AlmostEqual(self.dataRight, self.reqDistanceToWall, 3):
          #Расстояние до стены больше рекомендуемого
          if self.dataRight > self.reqDistanceToWall:
            pL += differencePower / 2
            pR -= differencePower / 2
          elif self.dataRight < self.reqDistanceToWall:
            pL -= differencePower / 2
            pR += differencePower / 2
      brick.motor(M4).setPower(pL)
      brick.motor(M3).setPower(pR)
      script.wait(50)
      
    pass
    
  #Проверка расстояния до стены, чтобы оно было между минимумом и максимумом
  def CheckDistance(self, dist):
    return dist <= self.zacepDist and dist >= self.minDistanceToWall
    
  #равенство с погрешностью в msxDifference
  def AlmostEqual(self, num1, num2, maxDifference):
    return abs(num1 - num2) < maxDifference
  
  #Поворот робота до угла в градусах
  def RotateToAngle(self, angle):
    #Установка мощности двигателей
    if angle > 180:
      angle-=360
    #Поворот по гироскопу
    if -brick.gyroscope().read()[6]/1000 < angle:
      brick.motor(M3).setPower(self.power/5)
      brick.motor(M4).setPower(-self.power/5)
      while not self.AlmostEqual(-brick.gyroscope().read()[6]/1000, angle, 0.4):
        script.wait(50)
    if -brick.gyroscope().read()[6]/1000 > angle:
      brick.motor(M3).setPower(-self.power/5)
      brick.motor(M4).setPower(self.power/5)
      while not self.AlmostEqual(-brick.gyroscope().read()[6]/1000, angle, 0.4):
        script.wait(50)
    #остановка моторов
    brick.motor(M3).setPower(0)
    brick.motor(M4).setPower(0)
    
  #Изменение текущего положение робота по тикам энкодера
  def ChangePositionRobot(self, tick):
    self.PrintMap()
    #Предыдущее значение энкодера
    tick0 = tick
    #Текущее положение энкодера
    tick = (brick.encoder(E3).read()+brick.encoder(E4).read())/2
    #Расстояние пройденное роботом за определённый промежуток времени
    dist = math.pi * self.diametr * (tick - tick0) / 374
    #Угол положения робота в пространстве
    angle = -float(brick.gyroscope().read()[6])/1000 / 180 * math.pi
    #Изменение координат робота
    self.X += dist * math.cos(angle)
    self.Y += dist * math.sin(angle)
    return tick
        
  def Moving(self, distance):
    #Искать кругом стены и рисовать их
    tick = (brick.encoder(E3).read()+brick.encoder(E4).read())/2
    self.dataLeft = brick.sensor(D1).read()
    self.dataRight = brick.sensor(D2).read()
    tickToEndMove = tick + (distance / (math.pi * self.diametr) * 374)
    #Левое колесо
    brick.motor(M4).setPower(self.power)
    #Правое колесо
    brick.motor(M3).setPower(self.power)
    while tick <= tickToEndMove:
      if self.AlmostEqual(self.X, self.toX, self.priemotkl) and self.AlmostEqual(self.Y, self.toY, self.priemotkl):
        print("Приехали")
        return
      self.dataLeft = brick.sensor(D1).read()
      self.dataRight = brick.sensor(D2).read()
      #Изменить координаты робота
      tick = self.ChangePositionRobot(tick)
      #Если найдена стена с одной из сторон двигаться сонаправленно ей
      if self.CheckDistance(self.dataLeft) or self.CheckDistance(self.dataRight):
        self.WallMoving()
        self.Moving(50)
        print("Вычисляем новую прямую")
        print(self.k, self.b, self.startAngle)
        self.newCoef()
        print(self.k, self.b, self.startAngle)
        if self.AlmostEqual(self.X, self.toX, self.priemotkl) and self.AlmostEqual(self.Y, self.toY, self.priemotkl):
          print("Пришли")
          return
        #Проверка на положение робота относительно конечной точки  TODO
        elif self.Y < self.toY:
          self.RotateToAngle(self.startAngle)
          self.Moving(math.sqrt((self.X-self.toX)**2+(self.Y-self.toY)**2))
        else:
          self.RotateToAngle(180-self.startAngle)
          self.Moving(math.sqrt((self.X-self.toX)**2+(self.Y-self.toY)**2))
      script.wait(50)
    #Остановка робота
    
    brick.motor(M4).setPower(0)
    brick.motor(M3).setPower(0)
    pass

  def newCoef(self):
    self.k = (self.toY - self.Y) / (self.toX - self.X)
    self.b = self.Y-self.k*self.X
    self.startAngle = math.atan(self.k)/math.pi*180
    if self.startAngle < 0:
      self.startAngle += 180
  #Отрисовка карты
  def PrintMap(self):
    fileNewData = open("NewData.txt", 'a')
    #Правый энкодер, Левый энкодер, показания гироскопа, данные правого датчика, данные левого датчика
    fileNewData.write(str(brick.encoder(E3).read()) + " " + str(brick.encoder(E4).read()) + " " +  
        str(brick.gyroscope().read()[6]/1000) + " " +  str(brick.sensor(D2).read()) + " " +  
        str(brick.sensor(D1).read()) + "\n")    

def main():
  program = Program()
  program.execMain()
  


if __name__ == '__main__':
  main()
