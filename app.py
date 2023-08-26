
import pygame 
import sys
import time
from pygame import gfxdraw
import pygame.freetype






Notes_Input = [1,2,3,4,3,2,1]
Notes_Input = [1,3,5,8,5,3,1]
Notes_Input = [1,5,3,5,1]
Notes_Input = [1,4,2.5,1]




#config
PREPTIME = 4
TEMPO = 0.33
LOOPS = 2

#window config 
WINDOW_WIDTH =1600
WINDOW_HEIGHT = 900
BG_COLOR = (173,216,230)



#note config 
NOTE_SIZE = 50
NOTE_SEPARATION_SCALE = 2
NOTE_BORDER_SIZE = int(NOTE_SIZE/10)
NOTE_BORDER_COLOR = (1, 87, 170)
NOTE_COLOR = (2, 119, 189)

START_OFFSET_X = NOTE_SIZE +   ( WINDOW_WIDTH/(NOTE_SIZE*NOTE_SEPARATION_SCALE)-len(Notes_Input) )/2 *NOTE_SIZE*NOTE_SEPARATION_SCALE 
START_OFFSET_Y = NOTE_SIZE + ( WINDOW_HEIGHT/(NOTE_SIZE*NOTE_SEPARATION_SCALE)-max(Notes_Input) )/2 *NOTE_SIZE*NOTE_SEPARATION_SCALE 





pygame.init() #start pygame 
pygame.mixer.init()  # Initialize the audio module.
MainScreen = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))



#custom function to prepare images for pygame
def ConvertImage(path, scaleX, scaleY):  
    image = pygame.transform.scale(pygame.image.load(path), (scaleX, scaleY))
    return image

#Sounds# load sounds 
Click = pygame.mixer.Sound('Sounds/Click.wav')  
Note1 = pygame.mixer.Sound('Sounds/Note1.wav')
Note2 = pygame.mixer.Sound('Sounds/Note2.wav')
Note3 = pygame.mixer.Sound('Sounds/Note3.wav')
Note4 = pygame.mixer.Sound('Sounds/Note4.wav')
Note5 = pygame.mixer.Sound('Sounds/Note5.wav')



#draw circle func
def DrawCircle(surface, x, y, radius, color):
    gfxdraw.aacircle(surface, x, y, radius, color)
    gfxdraw.filled_circle(surface, x, y, radius, color)


def DrawNoteOutlines(notes):

    #draw each note outline
    for pos_index, note_num in enumerate(notes):

        x = int(pos_index * NOTE_SIZE*NOTE_SEPARATION_SCALE +START_OFFSET_X)
        y = int(WINDOW_HEIGHT - ((note_num-1) *NOTE_SIZE*NOTE_SEPARATION_SCALE) - START_OFFSET_Y)

        DrawCircle(MainScreen,  x, y,  NOTE_SIZE, NOTE_BORDER_COLOR)
        DrawCircle(MainScreen,  x, y,  NOTE_SIZE-NOTE_BORDER_SIZE, NOTE_COLOR)



def PlayNote(note_index, note_type):

    x = int(note_index * NOTE_SIZE*NOTE_SEPARATION_SCALE +START_OFFSET_X)
    y = int(WINDOW_HEIGHT - ((note_type-1) *NOTE_SIZE*NOTE_SEPARATION_SCALE) - START_OFFSET_Y)


    try:
        pass
        #eval(f"Note{round(note_type)}.play()")
    except:
        pass

    #myfont = pygame.font.SysFont('arial', 32)
    #textsurface = myfont.render('♪', False, (0, 0, 0))
    #MainScreen.blit(textsurface,(x+5,y-5))

    DrawCircle(MainScreen,  x, y,  NOTE_SIZE-NOTE_BORDER_SIZE, (2, 48, 75))

    #MainScreen.blit(ConvertImage("Note.png",NOTE_SIZE,int(NOTE_SIZE*1.5)), (x-NOTE_SIZE/2,y-(NOTE_SIZE*1.5)/2))

    
#wait for load 
MainScreen.fill(BG_COLOR)
pygame.display.update()
time.sleep(0.5)

#start preptime
for i in reversed(range(PREPTIME)):

    

    MainScreen.fill(BG_COLOR)


    ft_font = pygame.freetype.SysFont('ArialBold', 500)
    text_str = f'{i+1}'
    text_rect = ft_font.get_rect(text_str)
    text_rect.center = MainScreen.get_rect().center
    ft_font.render_to(MainScreen, text_rect, text_str, NOTE_BORDER_COLOR)

    pygame.display.update() #draw all of the elements into the screen


    # Play click sound.
    Click.play() 

    
    time.sleep(0.5)


#play notes
for _ in range(LOOPS):

    for i,note in enumerate(Notes_Input):

        

        #darw bg and note outlines 
        MainScreen.fill(BG_COLOR)
        DrawNoteOutlines(Notes_Input)


        #DrawCircle(MainScreen,int(WINDOW_WIDTH/2),int(WINDOW_HEIGHT/2),NOTE_SIZE,(0,0,0))  #center circle aligner 

        #play current note 
        PlayNote(i, note)

        pygame.display.update() #draw all of the elements into the screen

        # Play click sound.
        Click.play() 

        if type(note) == int:
            time.sleep(TEMPO)
        else: # if note is decimal 
            #time.sleep(TEMPO/2)
            time.sleep(TEMPO)

    #claen screen
    DrawNoteOutlines(Notes_Input)
    pygame.display.update() #draw all of the elements into the screen

    time.sleep(2)



time.sleep(3)
pygame.quit() 
sys.exit()

while False:

    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            pygame.quit() 
            sys.exit() 
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                pass
        


    
   
    MainScreen.fill(BG_COLOR)
    DrawNoteOutlines(input_example)


    pygame.display.update() #draw all of the elements into the screen
    time.sleep(1)
    
    