# implementation of card game - Memory

import simplegui
import random

state = 0
WIDTH = 800
HEIGHT = 100
CARD_WIDTH = 50
TURNS = 0
NUM_CARDS = 16

# helper function to initialize globals
def new_game():
    global CARDS
    global exposed
    global TURNS
    state = 0
    CARDS = range(8) + range(8)
    random.shuffle(CARDS)
    exposed = [False] * NUM_CARDS
    TURNS = 0
    label.set_text('Turns = ' + str(TURNS))
     
# define event handlers
def mouseclick(pos):
    global state, card1, card2, TURNS
    if exposed[pos[0]/CARD_WIDTH] == False:
        card_clicked = pos[0]/CARD_WIDTH 
        if state == 0:
            state = 1
            exposed[card_clicked] = True
            card1 = card_clicked
        elif state == 1:
            state = 2
            exposed[card_clicked] = True
            card2 = card_clicked
        elif state == 2:
            TURNS += 1
            state = 1
            if CARDS[card1] != CARDS[card2]:
                exposed[card1] = exposed[card2] = False
            card1 = card_clicked
            exposed[card_clicked] = True
                                                                
# cards are logically 50x100 pixels in size    
def draw(canvas):
    global exposed
    label.set_text('Turns = ' + str(TURNS))
    for i in range(NUM_CARDS):
        if exposed[i]:
            canvas.draw_text(str(CARDS[i]), ((i*CARD_WIDTH)+(CARD_WIDTH-frame.get_canvas_textwidth(str(CARDS[i]),75))*.5, 75), 80, "White")
        else:	
            canvas.draw_polygon([(i*CARD_WIDTH, 0), ((i+1)*CARD_WIDTH, 0), ((i+1)*CARD_WIDTH, 100), (i*CARD_WIDTH, 100)], 1, "Red", "Green")
         
# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Restart", new_game)
label = frame.add_label("Turns = "+str(TURNS))

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()

# Always remember to review the grading rubric
