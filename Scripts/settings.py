import pygame as pg , pyautogui , time , random , math , sys , pickle , sys
from time import *

pg.font.init()

screen_width , screen_height  = 800 , 600
picture_width , picture_height = 800 , 600
fontsize = 25
f1 = pg.font.Font( None , fontsize ) 
sc = pg.display.set_mode ( ( screen_width , screen_height ) ) 
welcome = 'My Paint'
pg.display.set_caption( welcome )

shapes = [ 

'circle' , 'rectangle' , 'line' , 'elipse' , 'polygon' , 'star' ,'squareframe' , 'sun' , 'grid' , 'door' ,
'window' , 'text' , 'plus' , 'cross' , 'messageicon' , 'circleframe', 'cilinder'

]

shape = shapes[1]
radius , radius1 = 5 , 5
rect_width , rect_height = 50, 50
line_width1 , line_width2 = 50 , 0
draw_dist = 25
horizontal_offset , vertical_offset = 10 , 10
cancel_icon_x ,cancel_icon_y = screen_width - 50 , 10
cancel_icon_width , cancel_icon_height = 25 , 25

