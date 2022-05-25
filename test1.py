import sys
import time
import random
import math

#Проблема с направлением, робот оказывается снизу потому что он хз почему на самом деле надо думать
class Program():
  __interpretation_started_timestamp__ = time.time() * 1000
  maxDistanceToWallReading = 150
  minDistanceToWall = 7
  #Расстояние до стены, на котором будет двигаться робот
  reqDistanceToWall = 20
  pi = 3.141592653589793
  width = height = 1
  map = [[0 for i in range(1)] for j in range(1)]
  X=Y=0
  #мощность моторов
  power = 30
  robPos = [0, 0]
  #Размерность одной клетки на карте
  stepSize = 10
  #Значения датчиков расстояние
  dataLeft = brick.sensor(D1).read()
  dataRight = brick.sensor(D2).read()
  #Диаметр колеса робота
  diametr = 5.6
  
  def execMain(self):
    #Поставить робота на начальные координаты
    self.map[self.robPos[0]][self.robPos[1]]='x'
    #Повернуть робота на угол
    self.RotateToAngle(30)
    #Проехать в прямом направлении на расстояние
    self.Moving(30)
    brick.stop()
    return
    
  def WallMoving(self):
    minDist = 30
    tick = (brick.encoder(E3).read() + brick.encoder(E4).read())/2
    differencePower = 10
    #Левая стена
    while self.CheckDistance(self.dataLeft):
      #Стандартные мощности колёс
      pL = pR = self.power
      #обновление данных с датчиков расстояний
      self.dataLeft = brick.sensor(D1).read()
      self.dataRight = brick.sensor(D2).read()
      #Изменить положение робота
      tick = self.ChangePositionRobot(tick)
      #Заполнить карту
      self.PullMap()
      #Минимальное расстояние до стены, для "прикрепления" робота к ней
      if self.dataLeft <= minDist:
        #Если рекомендуемое расстояние до стены отличается от текущего, с небольшой разницей
        if not self.AlmostEqual(self.dataLeft, self.reqDistanceToWall, 3):
          #Расстояние до стены больше рекомендуемого
          if self.dataLeft > self.reqDistanceToWall:
            pL -= differencePower / 2
            pR += differencePower / 2
          elif self.dataLeft < self.reqDistanceToWall:
            pL += differencePower / 2
            pR -= differencePower / 2
      brick.motor(M4).setPower(pL)
      brick.motor(M3).setPower(pR)
      script.wait(30)
      
    #Правая стена
    while self.CheckDistance(self.dataRight):
      #Аналогично левой стене
      #Стандартные мощности колёс
      pL = pR = self.power
      #обновление данных с датчиков расстояний
      self.dataLeft = brick.sensor(D1).read()
      self.dataRight = brick.sensor(D2).read()
      #Изменить положение робота
      tick = self.ChangePositionRobot(tick)
      #Заполнить карту
      self.PullMap()
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
      script.wait(30)
      
    pass
    
  #Проверка расстояния до стены, чтобы оно было между минимумом и максимумом
  def CheckDistance(self, dist):
    return dist <= self.maxDistanceToWallReading and dist >= self.minDistanceToWall
    
  #равенство с погрешностью в msxDifference
  def AlmostEqual(self, num1, num2, maxDifference):
    return abs(num1 - num2) < maxDifference
  
  #Поворот робота до угла в градусах
  def RotateToAngle(self, angle):
    #Установка мощности двигателей
    brick.motor(M3).setPower(self.power)
    brick.motor(M4).setPower(-self.power)
    #Поворот по гироскопу
    while not self.AlmostEqual(-brick.gyroscope().read()[6]/1000, angle, 1):
      script.wait(30)
    #остановка моторов
    brick.motor(M3).setPower(0)
    brick.motor(M4).setPower(0)
    
  #Изменение текущего положение робота по тикам энкодера
  def ChangePositionRobot(self, tick):
    #Предыдущее значение энкодера
    tick0 = tick
    #Текущее положение энкодера
    tick = (brick.encoder(E3).read()+brick.encoder(E4).read())/2
    #Расстояние пройденное роботом за определённый промежуток времени
    dist = self.pi * self.diametr * (tick - tick0) / 374
    #Угол положения робота в пространстве
    angle = -float(brick.gyroscope().read()[6])/1000 / 180 * self.pi
    #Изменение координат робота
    self.X += dist * math.cos(angle)
    self.Y -= dist * math.sin(angle)
    return tick
        
  def Moving(self, distance):
    #ехать 
    #TODO
    #Искать кругом стены и рисовать их
    tick = (brick.encoder(E3).read()+brick.encoder(E4).read())/2
    self.dataLeft = brick.sensor(D1).read()
    self.dataRight = brick.sensor(D2).read()
    self.PullMap()
    tickToEndMove = tick + (distance / (self.pi * self.diametr) * 374)
    #Левое колесо
    brick.motor(M4).setPower(self.power)
    #Правое колесо
    brick.motor(M3).setPower(self.power)
    while tick <= tickToEndMove:
      self.dataLeft = brick.sensor(D1).read()
      self.dataRight = brick.sensor(D2).read()
      #Изменить координаты робота
      tick = self.ChangePositionRobot(tick)
      #Заполнить карту
      self.PullMap()
      #Если найдена стена с одной из сторон двигаться сонаправленно ей
      if self.CheckDistance(self.dataLeft) or self.CheckDistance(self.dataRight):
        self.WallMoving()
        break
      script.wait(30)
    #Остановка робота
    
    brick.motor(M4).setPower(0)
    brick.motor(M3).setPower(0)
    pass
  #Отрисовка карты
  def PrintMap(self):
    fw = open("test.txt", 'w')
    for i in range(self.height):
      for j in range(self.width):
        fw.write(str(self.map[i][j])+' ')
      fw.write("\n")
    fw.close()
      
  def CheckMapAdd(self):
    #Позиция робота на карте
    coordX = int(self.X / self.stepSize)
    coordY = int(self.Y / self.stepSize)
    #Существование стен
    wallLeftExists = False
    wallRightExists = False
    #Угол робота на поверхности
    angleRobot = -float(brick.gyroscope().read()[6])/1000 / 180 * self.pi
    #Проверить левый датчик
    if self.CheckDistance(self.dataLeft):
      #Если стена существует то координаты дальней пустой точки равны координтам робота
      dotXLeft = coordX
      dotYLeft = coordY
      #Стена существует
      wallLeftExists = True
      #Координата видимой для робота точки стены
      wallXLeft = coordX + int(self.dataLeft * math.cos(angleRobot + self.pi / 4)/10)
      wallYLeft = coordY - int(self.dataLeft * math.sin(angleRobot + self.pi / 4)/10)
    #Добавление места в карту для стены
    if wallLeftExists:
      while wallYLeft < 0:
        self.AppendMapToTop()
        wallYLeft += 1
      while wallYLeft >= self.height:
        self.AppendMapToBottom()
      while wallXLeft < 0:
        self.AppendMapToLeft()
        wallXLeft += 1
      while wallXLeft >= self.width:
        self.AppendMapToRight()
    else:
      #если стены нет значит надо добавить видимое пустое пространство для робота
      dotXLeft = coordX + int(self.maxDistanceToWallReading * math.cos(angleRobot + self.pi/4)/10)
      dotYLeft = coordY - int(self.maxDistanceToWallReading * math.sin(angleRobot + self.pi/4)/10)
    #Обновление координат робота на карте
    coordX = int(self.X / self.stepSize)
    coordY = int(self.Y / self.stepSize)
    
    #Проверить правый датчик
    if self.CheckDistance(self.dataRight):
      #Координаты дальней видимой точки(не учитывая видимость стен)
      
      dotXRight = coordX
      dotYRight = coordY
      #Запоминаем существование стены
      wallRightExists = True
      #Координаты видимой роботом части стены
      wallXRight = coordX + int(self.dataRight * math.cos(angleRobot - self.pi / 4)/10)
      wallYRight = coordY - int(self.dataRight * math.sin(angleRobot - self.pi / 4)/10)
    #Добавление места в карту для стен
    if wallRightExists:
      while wallYRight < 0:
        self.AppendMapToTop()
        wallYRight += 1
      while wallYRight >= self.height:
        self.AppendMapToBottom()
      while wallXRight < 0:
        self.AppendMapToLeft()
        wallXRight += 1
      while wallXRight >= self.width:
        self.AppendMapToRight()
    else:
      #Координаты видимые роботом без стен
      dotXRight = coordX + int(self.maxDistanceToWallReading * math.cos(angleRobot - self.pi/4)/10)
      dotYRight = coordY - int(self.maxDistanceToWallReading * math.sin(angleRobot - self.pi/4)/10)
    #Добавление пустых клеток на карту
    #Нету стен с двух сторон
    if not(wallRightExists or wallLeftExists):
      while dotXLeft < 0 and dotXRight < 0:
        dotXLeft += 1
        dotXRight += 1
        self.AppendMapToLeft()
      while dotXLeft < 0:
        dotXLeft += 1
        self.AppendMapToLeft()
      while dotXRight < 0:
        dotXRight += 1
        self.AppendMapToLeft()
        
      while dotXLeft >= self.width-1 and dotXRight >= self.width-1:
        self.AppendMapToRight()
      while dotXLeft >= self.width-1:
        self.AppendMapToRight()
      while dotXRight >= self.width-1:
        self.AppendMapToRight()
        
      while dotYLeft < 0 and dotYRight < 0:
        dotYLeft += 1
        dotYRight += 1
        self.AppendMapToTop()
      while dotYLeft < 0:
        dotYLeft += 1
        self.AppendMapToTop()
      while dotYRight < 0:
        dotYRight += 1
        self.AppendMapToTop()
        
      while dotYLeft >= self.height-1 and dotYRight >= self.height-1:
        self.AppendMapToBottom()
      while dotYLeft >= self.height-1:
        self.AppendMapToBottom()
      while dotYRight >= self.height-1:
        self.AppendMapToBottom()
        
    #Нету стены слево
    if not wallLeftExists:
      while dotXLeft < 0:
        dotXLeft += 1
        self.AppendMapToLeft()
      while dotXLeft >= self.width-1:
        self.AppendMapToRight()
      while dotYLeft < 0:
        dotYLeft += 1
        self.AppendMapToTop()
      while dotYLeft >= self.height-1:
        self.AppendMapToBottom()
        
    #Нету стены справо
    if not wallRightExists:
      while dotXRight < 0:
        dotXRight += 1
        self.AppendMapToLeft()
      while dotXRight >= self.width-1:
        self.AppendMapToRight()
      while dotYRight < 0:
        dotYRight += 1
        self.AppendMapToTop()
      while dotYRight >= self.height-1:
        self.AppendMapToBottom()
      
      
    #Возвращать направления в которых есть стена
    #self.PrintMap()
    if wallLeftExists and wallRightExists:
      return ["left","right"]
    if wallLeftExists:
      return ["left"]
    if wallRightExists:
      return ["right"]
    return []
    
  def PullMap(self):
    #Убираем прошлую позицию робота с карты
    self.map[self.robPos[1]][self.robPos[0]] = 0
    #Угол положения робота на карте
    angleRobot = -float(brick.gyroscope().read()[6])/1000 /180 * self.pi
    #Провереям на добавленеи точек и ставим точки стен на карту
    for dir in self.CheckMapAdd():
      #координаты робота
      coordX = int(self.X / self.stepSize)
      coordY = int(self.Y / self.stepSize)
      #Левая стена
      if dir == "left":
        wallX = coordX + int(self.dataLeft * math.cos(angleRobot + self.pi / 4)/10)
        wallY = coordY - int(self.dataLeft * math.sin(angleRobot + self.pi / 4)/10)
        try:
          self.map[wallY][wallX] = 1
        except:
          print("Сломалась индексация стены слево")
      #Правая стена
      if dir == "right":
        wallX = coordX + int(self.dataRight * math.cos(angleRobot - self.pi / 4)/10)
        wallY = coordY - int(self.dataRight * math.sin(angleRobot - self.pi / 4)/10)
        try:
          self.map[wallY][wallX] = 1
        except:
          print("Сломалась индексация стены справо")
    #Пересчёт координат робота на карте
    coordY = int(self.Y / self.stepSize)
    coordX = int(self.X / self.stepSize)
    #Текущее положение робота
    self.map[coordY][coordX] = 9
    #Запоминаем текущее положение
    self.robPos = [coordX, coordY]
    self.PrintMap()
    pass
    
  #Добавить место в карту слево
  def AppendMapToLeft(self):
    self.X += self.stepSize
    self.width += 1
    map = [[0 for i in range(self.width)] for j in range(self.height)]
    for i in range(self.height):
      for j in range(self.width):
        if j == 0:
          map[i][j] = 0
          continue
        if self.map[i][j-1] != 9:
          map[i][j] = self.map[i][j-1]
        else:
          map[i][j] = 0
    self.map = map
    
  #Добавить место в карту справо
  def AppendMapToRight(self):
    self.width += 1
    map = [[0 for i in range(self.width)] for j in range(self.height)]
    for i in range(self.height):
      for j in range(self.width):
        if j == self.width-1:
          map[i][j] = 0
          continue
        if self.map[i][j] != 9:
          map[i][j] = self.map[i][j]
        else:
          map[i][j] = 0
    self.map = map
    
  #Добавить место в карту сверху
  def AppendMapToTop(self):
    self.height += 1
    self.Y += self.stepSize
    map = [[0 for i in range(self.width)] for j in range(self.height)]
    for i in range(self.height):
      for j in range(self.width):
        if i == 0:
          map[i][j] = 0
          continue
        if self.map[i-1][j] != 9:
          map[i][j] = self.map[i-1][j]
        else:
          map[i][j] = 0
    self.map = map
    
  #Добавить место в карту снизу
  def AppendMapToBottom(self):
    self.height += 1
    map = [[0 for i in range(self.width)] for j in range(self.height)]
    for i in range(self.height):
      for j in range(self.width):
        if i == self.height-1:
          map[i][j] = 0
          continue
        if self.map[i][j] != 9:
          map[i][j] = self.map[i][j]
        else:
          map[i][j] = 0
    self.map = map
    
def main():
  program = Program()
  program.execMain()
  


if __name__ == '__main__':
  main()
