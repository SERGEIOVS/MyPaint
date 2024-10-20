import pygame as pg , pyautogui , time , random , math , sys , pickle , sys , os
pg.font.init()

window_width   = 1280
window_height  = 720

picture_width  = 800
picture_height = 600

sc = pg.display.set_mode ( ( window_width , window_height ) ) 

welcome = 'Привет!'
pg.display.set_caption( welcome )
pos = pg.mouse.get_pos()


shapes = [

'circle' , 'rectangle' , 'triangle' , 'line' , 'elipse' , 'polygon'

]

shape = shapes[ 1 ]


Fontname = 'serif'
fontsize = 20
f1 = pg.font.SysFont(Fontname, fontsize)



radius = 10
radius1 = 10

rect_width = 50
rect_height = 50

line_width1 = 50
line_width2 = 0

draw_dist = 25

horizontal_offset = 10
vertical_offset   = 10


pos = pg.mouse.get_pos()

WHITE   = ( 255 , 255 , 255 )
RED     = ( 255 , 0   , 0   )
ORANGE  = ( 255 , 125 , 0   )
YELLOW  = ( 255 , 255 , 0   )
GREEN   = ( 0   , 225 , 0   )
L_BLUE  = ( 0   , 125 , 255 )
BLUE    = ( 0   , 0   , 255 )
D_BLUE  = ( 0   , 0   , 125 )
PURPLE  = ( 128 , 0   , 255 )
LIME    = ( 0   , 255 , 0   )
OLIVE   = ( 128 , 128 , 0   )
GREY    = ( 128 , 128 , 128 )
BLACK   = ( 0   , 0   , 0   ) 
BROWN   = ( 101 , 67  , 33  )
AQUA    = ( 0   , 255 , 255 )
SILVER  = ( 192 , 192 , 192 )
MAGENTA = ( 255 , 0   , 255 )
GOLD    = ( 255 , 215 , 0   )

BGCOLOR = WHITE

measure_units = ['|Радиус : ' , '|Длина : ' , '|Ширина : ' , '|Кол-во вершин : '   ]

measure_unit1 = measure_units[ 0 ]
measure_unit1 = measure_units[ 0 ]
measure_unit1 = measure_units[ 0 ]
measure_unit1 = measure_units[ 0 ]
measure_unit1 = measure_units[ 0 ]



text_color = ( 180 , 0 , 0 )
text1 = f1.render( measure_unit1 + str( radius )  + ' | ' , True , text_color )

Colors = [

RED   , ORANGE , YELLOW , GREEN , L_BLUE , BLUE , PURPLE ,
LIME  , OLIVE  , GREY   , BLACK , BROWN  , AQUA , SILVER ,
MAGENTA , GOLD

]

surf_scale = 1

ColorsCoords_x = [ ]
ColorsCoords_y = [ ]

for i in range( len( Colors ) ) :
    i = ColorsCoords_x.append( 20 + i * draw_dist + radius1 )
    i = ColorsCoords_y.append( radius1 * 4 )

main_color = Colors[ 1 ]
colors_max = len( Colors )
step = 1




layers_panel_color = ( 50 , 50 , 50)

layers_panel = pg.draw.rect( sc , ( layers_panel_color ) , ( 90  , 90 , 200 , window_height ) )

img_surf = pg.Surface(( picture_width * surf_scale , picture_height * surf_scale) )

color_depth = 1



options  =  ['File'  , 'Edit' , 'View' , 'References' , 'Layout']
options1 =  []
layers   =  ['Layer' , 'Edit' , 'View' , 'References' , 'Layout']
layers1  =  []



for i in range(len(layers)):
    i = f1.render( str(layers[i]) , True , text_color )
    layers1.append(i)

for i in range(len(options)):
    i = f1.render( str(options[i]) , True , text_color )
    options1.append(i)

f = pg.font.SysFont( Fontname , fontsize )

img_size1  = int(picture_width)
img_size2  = int(picture_height)

img_size_full = f1.render('Image size: ' + str(img_size1) + ' * ' + str(img_size2) , True , text_color )
img_size_full_x = int(window_width)  // 2
img_size_full_y = 0


sc.fill( BGCOLOR )

def Update():
    global options_panel_height , options_panel_width , options_panel_x , options_panel_y

    #options_panel    
    options_panel_x = 0
    options_panel_y = 0
    options_panel_width = window_width
    options_panel_height = 90


    #layers panel
    layers_panel_width = 200
    layers_panel_height = window_height
    layers_panel_x = window_width  - layers_panel_width
    layers_panel_y = options_panel_height
    
    panel        = pg.draw.rect( sc , ( GREY ) , ( options_panel_x , options_panel_y , window_width , options_panel_height ) )
    layers_panel = pg.draw.rect( sc , ( layers_panel_color ) , ( layers_panel_x , layers_panel_y ,layers_panel_width , layers_panel_height ) )
    

    sc.blit(img_surf , ( 100 , 100 ))


    for i in range(len(options)):
        pg.draw.rect( sc , ( (150 * color_depth , 150 , 150)) , ( 5 * i + 90 * i + 15 , options_panel_y , fontsize / 2 + fontsize * len(options[i]) / 2 + fontsize / 2 , fontsize + 6 ), 1 , 5 )
        sc.blit(options1[i] , ( 10 + fontsize / 2 + i * 10 + 90 * i , options_panel_y  ) ) 


    for i in range(len(layers)):
        pg.draw.rect( sc , ( (150 * color_depth , 150 , 150)) , ( layers_panel_x  + 25 , layers_panel_y * i + 100 , fontsize / 2 + fontsize * len(options[i])  / 2 + fontsize / 2   , fontsize + 6 ), 0 , 5 )
        sc.blit(layers1[i] , ( layers_panel_x + 25  , layers_panel_y * i + 100 ) ) 


    for i in range( len( Colors ) ):
        i = pg.draw.circle( sc , Colors[ i ] , ( ColorsCoords_x[ i ] , ColorsCoords_y[ i ] ) , radius1 )



    sc.blit( text1 , ( 20 , 50 ) )
    
    img_size_full_x = int(window_width)  // 2
    img_size_full_y = 0
    
    sc.blit(img_size_full , ( int(img_size_full_x) , int(img_size_full_y)))  


    current_color_num = 0
    
    current_color_selector = pg.draw.circle( sc , Colors[ current_color_num ] , ( ColorsCoords_x[ 0 ] , 35 ) , 5 )

    pg.display.update()
    sc.fill( BGCOLOR )

while True:

    for event in pg.event.get() :
        pressed = pg.mouse.get_pressed()
        pos     = pg.mouse.get_pos()

        if pressed[ 2 ] and shape == shapes[ 0 ] :
            pg.draw.circle ( img_surf , main_color , event.pos , radius )
            Update()

        if pressed[ 2 ] and shape == shapes[ 2 ] :
            pg.draw.line( img_surf , main_color , [ 10 , 30 ] , [ 290 , 15 ] , 1 ) 
            Update()


        if pressed[ 2 ] and shape == shapes[ 3 ] :
            pg.draw.ellipse( img_surf , main_color , ( 10 , 50 , 280 , 100 ) , 1 )
            Update()

        if pressed[ 2 ] and shape == shapes[ 4 ] :

            pg.draw.polygon( img_surf , main_color , [ [ 250 , 110 ] , [ 280 , 150 ] , [ 190 , 190 ] , [ 130 , 130 ] , [ 0 , 300 ] ] )
            Update()

        if event.type == pg.QUIT :
            sys.exit()


        if event.type == pg.KEYDOWN :
            if event.key == pg.K_1:
                step       = ColorsCoords_x[ 0 ]
                main_color = Colors[ 0 ]
                text1 = f1.render( measure_unit1 + str( radius )  + ' | ' , True , text_color )
                current_color_num = 0
                Update()


            if event.key == pg.K_3 :
                step = ColorsCoords_x[ 2 ]
                main_color = Colors[ 2 ]
                text1 = f1.render( measure_unit1 + str( radius )  + ' | ' , True , text_color )
                current_color_num = 2
                Update()

            if event.key == pg.K_4 :
                step = ColorsCoords_x[ 3 ]
                main_color = Colors[ 3 ]
                text1 = f1.render( measure_unit1 + str( radius )  + ' | ' , True , text_color )
                current_color_num = 3                
                Update()

            if event.key == pg.K_5 :
                step = ColorsCoords_x[ 4 ]
                main_color = Colors[ 4 ]
                text1 = f1.render( measure_unit1 + str( radius )  + ' | ' , True , text_color )
                current_color_num = 4
                Update()


            if event.key == pg.K_6 :
                step = ColorsCoords_x[ 5 ]
                main_color = Colors[ 5 ]
                text1 = f1.render( measure_unit1 + str( radius )  + ' | ' , True , text_color )
                current_color_num = 5
                Update()
        

            """
            
            shapes = [ 'circle' , 'rectangle' , 'triangle' , 'line' , 'elipse' , 'polygon' ]
            
            measure_units = ['|Радиус : ' , '|Длина : ' , '|Ширина : ' , '|Кол-во вершин : '   ]
            
            measure_unit = measure_units[ 0 ]
            
            """

            #circle drawing
            if event.key == pg.K_c :
                Update()
                shape = shapes[ 0 ]

            #rectangle drawing
            if  event.key == pg.K_r :
                Update()
                shape = shapes[ 1 ]

            #triangle drawing
            if  event.key == pg.K_p:
                Update()
                shape = shapes[ 2 ]

            #line drawing
            if  event.key == pg.K_l :
                Update()
                shape = shapes[ 3 ]
                
            #elipse drawing
            if  event.key == pg.K_e :
                Update()
                shape = shapes[ 4 ]

            if  event.key == pg.K_p:
                Update()
                shape = shapes[ 5 ]
            
            if event.key == pg.K_LCTRL :
                if not os.path.exists('img'):
                    os.makedirs('img')
                pg.image.save(img_surf, 'img/test.png')


            if event.key == pg.K_g:
                    opened_img = pg.image.load('img/test.png')
                    img_surf.blit(opened_img , ( 0 , 0 ))
                    Update()


            if event.key == pg.K_F1:
                window_width   = 800
                window_height  = 600
                
                picture_width  = int(window_width ) // 2 
                picture_height = int(window_height) // 2 

                img_size_full_x = int(window_width)  // 2
                img_size_full_y = 0

                sc = pg.display.set_mode ( ( window_width , window_height ) )
                welcome = 'Привет!'
                pg.display.set_caption( welcome )
                img_size_full = f1.render('Image size: ' + str(img_size1) + ' * ' + str(img_size2) , True , text_color )
                img_surf = pg.Surface(( picture_width * surf_scale , picture_height * surf_scale) )

                Update()
            
            if event.key == pg.K_F2:
                window_width = 1280
                window_height = 720

                picture_width  = 400
                picture_height = 400

                img_size_full_x = int(window_width)  // 2
                img_size_full_y = 0

                sc = pg.display.set_mode ( ( window_width , window_height ) )
                welcome = 'Привет!'
                pg.display.set_caption( welcome )
                img_size_full = f1.render('Image size: ' + str(img_size1) + ' * ' + str(img_size2) , True , text_color )
                img_surf = pg.Surface(( picture_width * surf_scale , picture_height * surf_scale) )

                Update()


            if event.key == pg.K_F3:
                
                window_width = 1920
                window_height = 1080
                
                picture_width = 1280
                picture_height = 720

                img_size_full_x = int(window_width)  // 2
                img_size_full_y = 0
                

                sc = pg.display.set_mode ( ( window_width , window_height ) )
                welcome = 'Привет!'
                pg.display.set_caption( welcome )
                img_size_full = f1.render('Image size: ' + str(img_size1) + ' * ' + str(img_size2) , True , text_color )
                img_surf = pg.Surface(( picture_width * surf_scale , picture_height * surf_scale) )
                Update()


            if event.key == pg.K_F4:
                
                window_width   = 3840
                window_height  = 2160
                
                picture_width  = 1920
                picture_height = 1080

                img_size_full_x = int(window_width)  // 2
                img_size_full_y = 0

                layers_panel_width = 200
                layers_panel_height = window_height
                layers_panel_x = window_width  - layers_panel_width
                layers_panel_y = options_panel_height

                sc = pg.display.set_mode ( ( window_width , window_height ) )
                welcome = 'Привет!'
                pg.display.set_caption( welcome )     
                img_size_full = f1.render('Image size: ' + str(img_size1) + ' * ' + str(img_size2) , True , text_color )
                img_surf = pg.Surface(( picture_width * surf_scale , picture_height * surf_scale) )

                Update()


            if event.key == pg.K_b :
                BGCOLOR = main_color
            
            
            if event.key == pg.K_q :
                pg.event = pg.quit()


        if event.type == pg.MOUSEBUTTONDOWN :

            if event.button == 1:
                pg.draw.rect( sc , main_color, ( pos[ 0 ] - rect_width / 2 , pos[ 1 ] - rect_height / 2  , rect_width, rect_height ) )
                pg.display.update()
            
            #if shape is a circle
            if event.button == 4  and shape == shapes[0] :
                radius -= 3
                text1 = f1.render( measure_unit1 + str( radius )  + ' | ' , True , text_color )
                Update()

            if event.button == 5  and shape == shapes[0] :
                radius += 3
                text1 = f1.render( measure_unit1 + str( radius )  + ' | ' , True , text_color )
                Update()
            
            if event.button == 5 and shape == shapes[0] :
                radius += 3
                text1 = f1.render( measure_unit1 + str( radius )  + ' | ' , True , text_color )
                Update()



            #if shape is a rect
            if event.button == 4  and shape == shapes[1] :
                rect_width  += 3
                rect_height += 3
                text1 = f1.render( measure_units[1] + str( rect_width )  + ' / ' + measure_units[2] + str ( rect_height ) + ' | ' , True , text_color )
                Update()

    Update()
