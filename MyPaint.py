from colors import *
from settings import *
from interface import *


pos = pg.mouse.get_pos()
BGCOLOR = WHITE

measure_units = [

'Radius : ','lenght : ','width : ','Points : ','Verticles : '

]

measure_unit = measure_units[0]
value = 3
text_color = (180 , 0 , 0)
text1 = f1.render( measure_unit + str( radius ) , True , text_color )
Show_screen_size = f1.render( 'Window : ' + str(screen_width) + ' * ' + str(screen_height) , True , text_color )
Show_image_size = f1.render( 'Image : ' + str(screen_width) + ' * ' + str(screen_height) , True , text_color )

def Update():

    sc.fill( BGCOLOR )
    panel1 = pg.draw.rect( sc , ( GREY ) , ( panel_x , panel_y , screen_width , panel_height ) )
    panel2 = pg.draw.rect( sc , ( GREY ) , ( 0 ,panel_height , 150,screen_height ) )

    for i in range( len( Colors ) ) :
        sc.blit(cell.image , ( i * 25 , 0 ) )
        sc.blit(cell.image , (  0 ,panel_height + i * 75 ) )
        sc.blit(cell.image , ( 0 ,panel_height) )
        i = pg.draw.circle( sc , Colors[ i ] , ( radius1 * 2 + 2 + i * 25 , radius1 * 2 + 2 ) , radius1 )

    sc.blit( text1 , ( 20 , 75 ) )
    sc.blit( Show_screen_size , ( 20 , 50 ) )
    sc.blit(cancel_icon.image , ( cancel_icon_x,cancel_icon_y ) )
    image = sc.blit(cell.image ,( 0 , 0 )  )

    for i in range(len(MyShapesList)):
        i

    pg.display.update()

def make_screenshot() :
    screenshot = pyautogui.screenshot( 'снимки экрана/screenshot.png' , region = ( 100 , 100 ,1920,1080 ) )

while True:
    for event in pg.event.get() :
        pressed = pg.mouse.get_pressed()
        pos = pg.mouse.get_pos()

        #Правая кнопка мыши
        #Круг
        if pressed[ 2 ] and shape == shapes[ 0 ] :
            MyShapesList.append(pg.draw.circle ( sc , main_color , event.pos , radius ))
            Update()
            print(MyShapesList)

        #Правая кнопка мыши
        #квадрат    
        if pressed[ 2 ] and shape == shapes[ 1 ] :
            MyShapesList.append(pg.draw.rect(sc, main_color, ( pos[ 0 ] - rect_width / 2 , pos[ 1 ] - rect_height / 2  , rect_width, rect_height ) ))
            Update()
            print(MyShapesList)
            
        #Правая кнопка мыши
        #линия
        if pressed[ 2 ] and shape == shapes[ 2 ] :
            MyShapesList.append(pg.draw.line( sc , main_color , event.pos , [ 290 , 15 ] , 1 ) )
            Update()
            print(MyShapesList)

        #Правая кнопка мыши
        #полигон
        if pressed[ 2 ] and shape == shapes[ 4 ] :
            MyShapesList.append(pg.draw.polygon( sc , main_color , [ [ 250 , 110 ] , [ 280 , 150 ] , [ 190 , 190 ] , [ 130 , 130 ] , [ 0 , 300 ] ] ))
            Update()
            print(MyShapesList)
        
        if event.type == pg.QUIT :
            sys.exit()

        if event.type == pg.KEYDOWN :

            if event.key == pg.K_c :
                shape = shapes[ 0 ]
                
                Update()

                print(MyShapesList)

            if  event.key == pg.K_r :
                shape = shapes[ 1 ]

                Update()
                print(MyShapesList)

            if  event.key == pg.K_l:
                shape = shapes[ 2 ]

                Update()
                print(MyShapesList)

            if  event.key == pg.K_e :
                shape = shapes[ 3 ]
                Update()
                print(MyShapesList)

            if  event.key == pg.K_p:
                shape = shapes[ 4 ]
                Update()
                print(MyShapesList)

            if event.key == pg.K_s :
                make_screenshot()

            if event.key == pg.K_F12 :
                quit()

            if event.key == pg.K_F5 :
                screen_width = 1920
                screen_height = 1080
                sc = pg.display.set_mode ( ( screen_width , screen_height ) )
                welcome = welcome
                pg.display.set_caption( welcome )

            if event.key == pg.K_b :
                BGCOLOR = main_color
            
            if event.key == pg.K_u :
                Update()

        if event.type == pg.MOUSEBUTTONDOWN :

            #левая кнопка мыши
            if event.button == 1 and pos[0] >= 50 and pos[1] >= panel_height:
                MyShapesList.append(pg.draw.rect(sc, main_color, ( pos[ 0 ] - rect_width / 2 , pos[ 1 ] - rect_height / 2  , rect_width, rect_height ) ))
                pg.display.update()

                for i in range(len(MyShapesList)):
                    i

            #колесо мыши к монитору
            if event.button == 4  and shape == shapes[0] :
                radius -= value
                text1 = f1.render( measure_unit + str( radius ) , True , text_color )
                Update()

            #колесо мыши к себе
            if event.button == 5  and shape == shapes[0] :
                radius += value
                text1 = f1.render( measure_unit + str( radius ) , True , text_color )
                Update()

            #колесо мыши к монитору
            if event.button == 4  and shape == shapes[1] :
                rect_width -= value
                rect_height -= value
                text1 = f1.render( measure_units[1] + str( rect_width )  + ' / ' + measure_units[2] + str ( rect_height ) , True , text_color )
                Update()

            #колесо мыши к себе
            if event.button == 5  and shape == shapes[1] :
                rect_width += value
                rect_height += value
                text1 = f1.render( measure_units[1] + str( rect_width )  + ' / ' + measure_units[2] + str ( rect_height )  , True , text_color )
                Update()

            #колесо мыши к себе
            if event.button == 5 and shape == shapes[0] :
                radius += 3
                text1 = f1.render( measure_unit + str( radius )   , True , text_color )
                Update()

            #колесо мыши / средняя кнопка мыши
            if event.button == 2 :
                Update()


"""ColorsCoords_x = []

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
"""                