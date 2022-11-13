from settings import *
from colors import *

class interface :
    def __init__( self, x , y , width , height , image ) :
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.image = image
cell = interface( screen_width / 2 ,50 , 50 , 50 , pg.image.load( 'картинки/cell.png' ) )
currentcell = interface( screen_width / 2 ,50 , 50 , 50 , pg.image.load( 'картинки/current_cell.png' ) )
button = interface(2100,210,200,50,pg.image.load( 'картинки/button.png' ) )
left_pointer = interface(  50 , 100 ,20 , 20 , pg.image.load( 'картинки/pointer_left.png' ) )
right_pointer = interface(200 , 100 , 20 , 20 , pg.image.load( 'картинки/pointer_right.png' ) )
cancel_icon = interface(  50 , 25 , 20 , 20 , pg.image.load( 'картинки/cancel_icon.png' ) )
MyShapesList = []
ColorsCoords_x = []
ColorsCoords_y = []

for i in range( len( Colors ) ) :

    i = ColorsCoords_x.append(20 + i * draw_dist + radius1)
    
    i = ColorsCoords_y.append(radius1 * 2)

main_color = Colors[0]
colors_max = len(Colors)
step = 0
panel_width , panel_height = screen_width , 100
panel_x , panel_y = 0 , 0
Fontnames = ['serif']
Fontname = Fontnames[0]
f = pg.font.SysFont( Fontname , fontsize )