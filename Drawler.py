import arcade

class Drawler(arcade.Window):
    #Карта
    map = []
    #Координаты робота
    X = 0
    Y = 0
    def __init__(self, width, height):
        super().__init__(width, height)


    def setup(self):
        #Получение карты
        self.UpdateMap()
        #Установить бэкграунда
        arcade.set_background_color(arcade.color.WHITE)
        pass

    def on_draw(self):
        #Размеры клетки
        cellWidth = 30
        cellHeight = 30
        #Получаем координаты левой нижней части карты для отрисовки
        start_x = self.X - 10
        #Обрабатываем граничные случаи
        if start_x < 0:
            start_x = 0
        #Аналогично Х
        start_y = self.Y - 10
        if start_y < 0:
            start_y = 0
        arcade.start_render()
        #i0 и j0 координаты относительно левой нижней границы
        i0 = 0
        for i in range(start_y, start_y+21):
            j0 = 0
            for j in range(start_x, start_x+21):
                #Провера на выход за границы списка
                try:
                    self.map[i][j]
                except:
                    continue
                #Отрисовка стены
                if self.map[i][j] == 1:
                    x = j0*cellWidth+cellWidth/2
                    y = (21-i0)*cellHeight-cellHeight/2
                    arcade.draw_rectangle_filled(x, y,cellWidth,cellHeight, arcade.color.BLACK)
                #Отрисовка робота
                if self.map[i][j] == 9:
                    x = j0*cellWidth+cellWidth/2
                    y = (21-i0)*cellHeight-cellHeight/2
                    arcade.draw_rectangle_filled(x, y,cellWidth,cellHeight, arcade.color.RED)
                j0 += 1
            i0 += 1

    def update(self, delta_time): 
        self.UpdateMap()
        pass

    def UpdateMap(self):
        #Открываем файл на чтение
        f = open('C:/TRIKStudio/test.txt')
        #Инициализируем список для хранения карты
        mapInList = []
        #Инициализируем x и y для получения координат робота
        y = 0
        #Читаем файл построчно
        for line in f:
            x = 0
            #Временный список для хранения строки карты
            tempList = []
            #Разбиваем строки файла по пробелам
            for char in line.split(" "):
                #Добавляем в списки только целочисленные значения
                try:
                    tempList.append(int(char))
                    #9 - "метка" робота
                    if int(char) == 9:
                        self.X = x
                        self.Y = y
                except:
                    continue
                x += 1
            mapInList.append(tempList)
            y += 1
        f.close()
        self.map = mapInList

draw = Drawler(630, 630)
draw.setup()

arcade.run()