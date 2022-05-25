import arcade
SCREEN_WIDTH = 630
SCREEN_HEIGHT = 630


def GetMap():
    #Открываем файл на чтение
    f = open('C:/TRIKStudio/test.txt')
    #Инициализируем список
    mapInList = []
    #Читаем файл по строкам
    for line in f:
        tempList = []
        #Разбиваем строку по пробелам
        for char in line.split(" "):
            #Добавляем в список(карту) только значения чисел
            try:
                tempList.append(int(char))
            except:
                continue
        mapInList.append(tempList)
    #Закрываем файл
    f.close()
    return mapInList
    
def PrintMap():
    #Задаем размеры окна и заголовок
    arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, "Final map")
    #Задаем цвет бэкграунда
    arcade.set_background_color(arcade.color.WHITE)
    arcade.start_render()
    #Клеточная отрисовка карты
    for i in range(listH):
        for j in range(listW):
            if map[i][j] == 1:
                #Получаем координаты клетки для отрисовки
                x = j*cellW+cellW/2
                y = (listH-i)*cellH-cellH/2
                arcade.draw_rectangle_filled(x, y,cellW,cellH, arcade.color.BLACK)

    arcade.finish_render()
    arcade.run()
if __name__ == "__main__":
    #Получаем карту с файла
    map = GetMap()
    #Количество столбцов в карте
    listW = len(map[0])
    #Количество строк в карте
    listH = len(map)
    #Ширина и высота одной клетки
    cellW = SCREEN_WIDTH/listW
    cellH = SCREEN_HEIGHT/listH

    PrintMap()