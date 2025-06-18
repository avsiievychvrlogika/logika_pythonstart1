#робота зі списками 3 завдання

coordinates = [12, 45, 34, 23, 50, 60, -10, 15, 25, 25]
l=[]
for i in range(0,len(coordinates),2):
    x=coordinates[i]
    y=coordinates[i+1]
    if 0<=x<=50 and 0<=y<=50:
        l.append(x)
        l.append(y)
for i in range(0,len(l),2):  
    print(f"x: {l[i]} ; y: {l[i+1]}")

# 2

valid_chars = "0123456789ABCDEFabcdef"

#функція перевірки кольору
def chek_color(color):
    if color[0]=="#" and len(color)==7:
        for c in color[1:]:
            if not c in valid_chars:
                return False
        return True
    else:
        return False
a=input("Color")
c=[]
while a!="0":
    if chek_color(a):
        c.append(a)
    else:
        print("Некоректно введений колір.")
    a=input("Color")
print(c)

#3


# Початковий список курсорів
cursors = ["arrow", "turtle", "circle", "square", "triangle", "classic"]

#Функція, що виводить список курсорів у стовпчик.
def display_cursors():
    for c in cursors:
        print(c)
        
display_cursors()
a=input("Який курсор видалити")
while(a!="0"):
    if a in cursors:
        cursors.remove(a)
        print(f"Курсор '{a}' видалено.")
    else:
        print("Такого курсора немає у списку. Спробуйте ще раз.")
    display_cursors()
    a=input("Який курсор видалити")
print(cursors)


### малюємо за кодом
# 1

from art import *
colors_map = ["#f8efc0", "#547734", "#a42c20", "#fdfdfd","#0b0b0b"]
pic_map = [ "11122222222111",
            "11222222222211",
            "11222222222221", 
            "13333333333321",
            "13333333333321",
            "11300000003133", 
            "11304000403133",
            "13300020003311",
            "33303333303331", 
            "33333020333331",
            "33333333333331", 
            "13333333333311",
            "11333333333111"]
            
def draw(x,y,pixel,pic,colors):
    x0=x
    for l in pic:
        for c in l:
            start(x,y)
            color=colors[int(c)]
            square_fill(pixel,color)
            x+=pixel
        x=x0
        y-=pixel
speed(0)
draw(-100,100,10,pic_map,colors_map)

#3 

#підключи свій модуль art
#підключи модуль turtle
#встанови швидкість(speed) черепашки - 0 
#перший малюнок - список кольорів та закодований малюнок
colors_map1 = ["#a7adad", "#fafafa", "#4064f9 ", "#080808","#f09510 "]
pic_map1 = [ "------000------",
            "------000------",
            "-----11111-----",
            "---111111111---",
            "--11111111111--",
            "-1111221221111-",
            "-1111231231111-",
            "111111144111111",
            "111111444441111",
            "111311144444411",
            "111333311133111",
            "-1113333331111-",
            "-1111333331111-",
            "--11113331111--",
            "---111111111---",
            "-----11111-----"]
#другий малюнок - список кольорів та закодований малюнок
colors_map2 = ["#613c05", "#af7725", "#f8d7a8", "#020202","#cf1c0d"]
pic_map2 = ["0--------------0",
            "0--------------0",
            "00--0------0--00",
            "00-00------0-000",
            "-0000-0--0-0000-",
            "-000000--000000-",
            "---0000--0000---",
            "-----00--00-----",
            "-111-111111-111-",
            "-12111111111121-",
            "-11111111111111-",
            "---1113113111---",
            "---1113113111---",
            "---1111111111---",
            "--112222222211--",
            "-11224444442211-",
            "-12244444444221-",
            "-22444444444422-",
            "-22444444444422-",
            "-22244444444222-",
            "--222244442222--",
            "-----222222-----"]
#третій малюнок - список кольорів та закодований малюнок
colors_map3 = ["#fafafa","#f9e2e0","#000000","#e53021","#46a7ea","#4eecf4"]
pic_map3 = ["----000----",
            "--0000000--",
            "-000110000-",
            "-001111100-",
            "-012111210-",
            "-011111110-",
            "-001131100-",
            "--00111000-",
            "---442400--",
            "--4444400--",
            "-44544400--",
            "11554440511",
            "-554444455-",
            "55444444455",
            "55444444455"]
pixel_sizes = 10
coordinates = [-200,0,140,160,-20,50]

# намалюй задній фон(великий квадрат) для малюнків кольором  "#bbeef9"
from art import *
def draw(x,y,pixel,pic,colors):
    x0=x
    for l in pic:
        for c in l:
            start(x,y)
            if c!="-":
                color=colors[int(c)]
                square_fill(pixel,color)
            x+=pixel
        x=x0
        y-=pixel

speed(0)
start(-200,-200)
square_fill(1000,"#bbeef9")
draw(coordinates[0],coordinates[1],pixel_sizes,pic_map1,colors_map1)

draw(coordinates[2],coordinates[3],pixel_sizes,pic_map2,colors_map2)

draw(coordinates[4],coordinates[5],pixel_sizes,pic_map3,colors_map3)

