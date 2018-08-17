import pygame
# imports pygame to be used
pygame.init()
# initializes all imported pygame modules/basically makes pygame work
window_width=1301
window_height=800
# changes the size of the window when the code is run
size = (window_width, window_height)
screen = pygame.display.set_mode(size)
# references the variables window_width, window_height,
# and size into the function to set the size of the window
pygame.display.toggle_fullscreen()
class Background(pygame.sprite.Sprite):
    def __init__(self, image_file):
        pygame.sprite.Sprite.__init__(self)  #call Sprite initializer
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        #self.rect.left, self.rect.top = location

background_image = Background("space.jpg")
# references the image file as long as it is in the same folder as the pygame file
start = '''
You are fixing the exterior of the ship's engine when you receive
a call from a crew member. You answer it.
'''
story_one = '''
    "Ada is calling about the refrigerator being broken. She want you to come and help her. Type 'continue' to continue the introduction."
    '''
story_two = '''
    "You use your jets on the bottom of your feet to travel back to the exit. When you get there, you go to the supplies area to find Ada pulling the handle of refrigerator with all her might."
    '''
story_three = '''
    "'This damn fridge won't open. I've tried everything and it keeps on giving me the same message,' Ada explains. 'Fix it now, Sophia.'"
    '''
story_four = '''
    "'The refrigerator cannot be opened because the food limit has been reached,' you try to explain. But Ada cuts you off."
    '''
story_five = '''
    "'I don't care what the fridge says about the food. I'm literally starving! Open it now or I'll shut you down for disobedience.'"
    '''
story_five = '''
    "Type 'open' to continue the introduction."
    '''
story_six = '''
    "You open the back of the refrigerator to find the machinery within. You manipulate it into thinking it's never been open so that unlimited access is allowed."
    '''
story_seven = '''
    "'I do not think this will benefit you in the foreesable future, Ada. As the food supplies are predicted to not last very long at the rate you and Grace eat. The ship is sceduled to reach the planet in two weeks,' you warn Ada."
    '''
story_eight = '''
    "'Yeah, yeah. Bug off and do whatever robots do.' Ada then leaves back to the cockpit of the ship and you are left to your own devices."
    '''
story_nine = '''
    "Type 'go to Grace' or 'check the supplies' to continue the story.")
    '''
story_ten = '''
    "You go to Grace to find her tinkering in her research lab. She is not aware of your existence until she hears the tell-tale clink of your feet against the metal lab floor.
    She turns around and greets you with a smile. Between both women, Grace is the nicer of the two."
    '''
story_eleven = '''
    "'Grace, Ada has been taking more food than allowed by the ship's program. Do you not find this detrimental to the mission?'"
    '''
story_twelve = '''
    "'Really? I was unaware of that. Well, not the first thing she's done wrong since we've been out here. She's been telling me about not informing NASA when we find the planet. Now why in the world would she even suggest such a thing?'"
'''
story_thirteen = '''
    "'This is against the mission. Anyone against the mission should be removed from the mission, as stated by NASA themselves.'"
    '''
story_fourteen = '''
    "'No, no. There's no need for that. We can simply lock the cockpit so that she can't access it for a couple of days. That'll teach her a lesson.'"
    '''
story_fifteen = '''
    "Type 'shut off cockpit' to make the ship go on complete auto-pilot."
    '''
story_sixteen = '''
    "You go to the power system and shut down the co-pilot."
    '''
story_seventeen = '''
    "Type 'Go to Ada' to tell Ada about what is happening."
    '''
story_eighteen = '''
    "You go to Ada to find her trying to use her ID card to open the cockpit to no avail. She turns around and glares at you. 'What the hell is going on with the ship. You said you fixed the door issue. So why can't I get in?"
    '''
story_nineteen = '''
    "'Grace has instructed me to stop you from accessing the cockpit because of your need to take more food than necessary.'"
    '''
story_twenty = '''
    "'Oh, so you think you can go running to Grace when something doesn't go your way? Is that what I'm hearing right now? Well, guess what? The ship's on the wrong course, and if you don't open it and let me in, then the ship won't ever reach the planet and we'll die regardless of how much food we have.'"
    '''
story_twentyone = '''
    "Type 'open the cockpit' to trust Ada's word."
    '''
story_twentytwo = '''
    "You open the cockpit, trusting Ada when she says this. Your program demands that you do everything in your power to assure the women make it to the new planet."
    '''
story_twentythree = '''
    "Ada goes into the cockpit, and you hear the lock being turned. You attempt to open the door to find that she locked it. You notice that the ship is still going in the wrong direction."
    '''
story_twentyfour = '''
    "Type 'go to exit' to find a way to remove Ada out of the cockpit."
    '''
story_twentyfive = '''
    "You decide to go to the exit and find the power system, which allows for complete control over the ship's functions in case of an emergency. You pull the emergency exit option for the cockpit and hear it open. You see Ada's body flying out the ship, into the abyss of space. She was jeopardizing the mission."
    '''
story_twentysix = '''
    "You watch her body go, making sure it is far enough that the naked eye cannot see it, before going over to Grace to tell her what happened."
    '''
story_twentyseven = '''
    "Type 'go to Grace'"
    '''
story_twentyeight = '''
    "You go to Grace and find her now with a cup of coffee in hand and her body covered in soot. Appaerently she failed at her experiment."
    '''
story_twentynine = '''
    "'Ada is in the cockpit and she has locked herself within. She is detrimental to the mission,' you proudly(?) tell her."
    '''
story_thirty = '''
    "'She's always doing something. You know, Sophia, I don't think I want to hear anymore of that woman's nonsense. Just go to your charging dock.'"
    '''
story_thirtyone = '''
    "You find yourself feeling upset(?) at Grace's reaction. You wish to push her to what you want(?) to hear, but decide it is best to do as she says to not make her more upset. You go to the bedroom, albeit reluctantly...(END?)"
    '''
story_thirtytwo = '''
    "About Me:
    Jennifer Bernal - rising senior, HTML, wanted to see a game with a female cast, set up the elevator pitch and wrote the story for Grace, fun fact: made another game based on the classic ping pong
    '''
story_thirtythree = '''
    Nicole Murillo - rising senior, CSS, wanted to better prepare herself for upcoming bigger projects, created the mobile version, the art, and wrote Ada's story, fun fact: watches anime and her favorite is Dragonball Z
    '''
story_thirtyfour = '''
    Quaylin Johnson - rising senior, Python, played games since she was little, created PC version and wrote the story for Sophia, fun fact: loves to write and completed first manuscript
    '''
# these variables are used to hold the text that will be placed on the surface later
font = pygame.font.SysFont(None, 19)
# changes the font(used None because the process of downloading
# a font was not a priority)
text = font.render(start, True, (255, 165 , 0))
# font.render is used to change the color
rect = text.get_rect(center = (600, 200))
# get_rect is used to make a place for the text to reside in on the surface
text1 = font.render(story_one, True, (255,165 , 0))
text2 = font.render(story_two, True, (255, 165, 0))
text3 = font.render(story_three, True, (255, 165 , 0))
text4 = font.render(story_four, True, (255, 165 , 0))
text5 = font.render(story_five, True, (255, 165, 0))
text6 = font.render(story_six, True, (255, 165, 0))
text7 = font.render(story_seven, True, (255, 165 , 0))
text8 = font.render(story_eight, True, (255, 165 , 0))
text9 = font.render(story_nine, True, (255, 165, 0))
text10 = font.render(story_ten, True, (255,165, 0))
text11 = font.render(story_eleven, True, (255,165, 0))
text12 = font.render(story_twelve, True, (255,165, 0))
text13 = font.render(story_thirteen, True, (255,165, 0))
text14 = font.render(story_fourteen, True, (255,165, 0))
text15 = font.render(story_fifteen, True, (255,165, 0))
text16 = font.render(story_sixteen, True, (255,165, 0))
text17 = font.render(story_seventeen, True, (255,165, 0))
text18 = font.render(story_eighteen, True, (255,165, 0))
text19 = font.render(story_nineteen, True, (255,165, 0))
text20 = font.render(story_twenty, True, (255,165, 0))
text21 = font.render(story_twentyone, True, (255,165, 0))
text22 = font.render(story_twentytwo, True, (255,165, 0))
text23 = font.render(story_twentythree, True, (255,165, 0))
text24 = font.render(story_twentyfour, True, (255,165, 0))
text25 = font.render(story_twentyfive, True, (255,165, 0))
text26 = font.render(story_twentysix, True, (255,165, 0))
text27 = font.render(story_twentyseven, True, (255,165, 0))
text28 = font.render(story_twentyeight, True, (255,165, 0))
text29 = font.render(story_twentynine, True, (255,165, 0))
text30 = font.render(story_thirty, True, (255,165, 0))
text31 = font.render(story_thirtyone, True, (255,165, 0))
text32 = font.render(story_thirtytwo, True, (255, 165, 0))
text33 = font.render(story_thirtytwo, True, (255, 165, 0))
text34 = font.render(story_thirtytwo, True, (255, 165, 0))
rect1 = text1.get_rect(center =(600, 240))
rect2 = text2.get_rect(center =(600, 280))
rect3 = text3.get_rect(center =(600, 320))
rect4 = text4.get_rect(center =(600, 360))
rect5 = text5.get_rect(center =(600, 400))
rect6 = text6.get_rect(center =(600, 440))
rect7 = text7.get_rect(center =(600, 480))
rect8 = text8.get_rect(center =(600, 520))
rect9 = text9.get_rect(center =(600, 560))
rect10 = text10.get_rect(center =(600, 240))
rect11 = text11.get_rect(center =(600, 280))
rect12 = text12.get_rect(center =(600, 320))
rect13 = text13.get_rect(center =(600, 360))
rect14 = text14.get_rect(center =(600, 400))
rect15 = text15.get_rect(center =(600, 440))
rect16 = text16.get_rect(center =(600, 480))
rect17 = text17.get_rect(center =(600, 520))
rect18 = text18.get_rect(center =(600, 560))
rect19 = text19.get_rect(center =(600, 240))
rect20 = text20.get_rect(center =(600, 280))
rect21 = text21.get_rect(center =(600, 320))
rect22 = text22.get_rect(center =(600, 360))
rect23 = text23.get_rect(center =(600, 400))
rect24 = text24.get_rect(center =(600, 440))
rect25 = text25.get_rect(center =(600, 480))
rect26 = text26.get_rect(center =(600, 520))
rect27 = text27.get_rect(center =(600, 560))
rect28 = text28.get_rect(center =(600, 240))
rect29 = text29.get_rect(center =(600, 280))
rect30 = text30.get_rect(center =(600, 320))
rect31 = text31.get_rect(center =(600, 360))
rect32 = text31.get_rect(center =(600, 200))
rect33 = text31.get_rect(center =(600, 240))
rect34 = text31.get_rect(center =(600, 280))
pygame.display.set_caption("Rocket Into Danger")
# gives the window a title, much like the title of a web page when you open it
running = True
# used to help with running the main loop and making sure it is possible to close the window


x = text
y = rect
# making the text and rect variables makes it easier
# to reference the other text and rect when placing in the loop
count = 0
# count is important to making sure each line of text
# pops up and stays up when not clicking by making it
# so that the next line is only brought up through
# the condition being met
while(running==True):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        screen.blit(background_image.image, background_image.rect)
        # screen.blit places the image as the background of the window
        screen.blit(x, y)
        # same as image but places the text
        if event.type == pygame.MOUSEBUTTONDOWN and count==0:
            # pygame.MOUSEBUTTONDOWN is used to let the
            # file know that the mouse is being used to control
            pos = pygame.mouse.get_pos()
            # is used to make sure the mouse click only works when the
            # rectangle holding the text is clicked
            if y.collidepoint(pos):
                x = text1
                y = rect1
                count += 1
                # everytime the text is clicked, the next one only pops up if +1 is
                # added to the count variable
        if event.type == pygame.MOUSEBUTTONDOWN and count==1:
            pos = pygame.mouse.get_pos()
            if y.collidepoint(pos):
                x = text2
                y = rect2
                count += 1
        if event.type == pygame.MOUSEBUTTONDOWN and count==2:
            pos = pygame.mouse.get_pos()
            if y.collidepoint(pos):
                x = text3
                y = rect3
                count += 1
        if event.type == pygame.MOUSEBUTTONDOWN and count==3:
            pos = pygame.mouse.get_pos()
            if y.collidepoint(pos):
                x = text4
                y = rect4
                count += 1
        if event.type == pygame.MOUSEBUTTONDOWN and count==4:
            pos = pygame.mouse.get_pos()
            if y.collidepoint(pos):
                x = text5
                y = rect5
                count += 1
        if event.type == pygame.MOUSEBUTTONDOWN and count==5:
            pos = pygame.mouse.get_pos()
            if y.collidepoint(pos):
                x = text6
                y = rect6
                count += 1
        if event.type == pygame.MOUSEBUTTONDOWN and count==6:
            pos = pygame.mouse.get_pos()
            if y.collidepoint(pos):
                x = text7
                y = rect7
                count += 1
        if event.type == pygame.MOUSEBUTTONDOWN and count==7:
            pos = pygame.mouse.get_pos()
            if y.collidepoint(pos):
                x = text8
                y = rect8
                count += 1
        if event.type == pygame.MOUSEBUTTONDOWN and count==8:
            pos = pygame.mouse.get_pos()
            if y.collidepoint(pos):
                x = text9
                y = rect9
                count += 1
        if event.type == pygame.MOUSEBUTTONDOWN and count==9:
            pos = pygame.mouse.get_pos()
            if y.collidepoint(pos):
                x = text10
                y = rect10
                count += 1
        if event.type == pygame.MOUSEBUTTONDOWN and count==10:
            pos = pygame.mouse.get_pos()
            if y.collidepoint(pos):
                x = text11
                y = rect11
                count += 1
        if event.type == pygame.MOUSEBUTTONDOWN and count==11:
            pos = pygame.mouse.get_pos()
            if y.collidepoint(pos):
                x = text12
                y = rect12
                count += 1
        if event.type == pygame.MOUSEBUTTONDOWN and count==12:
            pos = pygame.mouse.get_pos()
            if y.collidepoint(pos):
                x = text13
                y = rect13
                count += 1
        if event.type == pygame.MOUSEBUTTONDOWN and count==13:
            pos = pygame.mouse.get_pos()
            if y.collidepoint(pos):
                x = text14
                y = rect14
                count += 1
        if event.type == pygame.MOUSEBUTTONDOWN and count==14:
            pos = pygame.mouse.get_pos()
            if y.collidepoint(pos):
                x = text15
                y = rect15
                count += 1
        if event.type == pygame.MOUSEBUTTONDOWN and count==15:
            pos = pygame.mouse.get_pos()
            if y.collidepoint(pos):
                x = text16
                y = rect16
                count += 1
        if event.type == pygame.MOUSEBUTTONDOWN and count==16:
            pos = pygame.mouse.get_pos()
            if y.collidepoint(pos):
                x = text17
                y = rect17
                count += 1
        if event.type == pygame.MOUSEBUTTONDOWN and count==17:
            pos = pygame.mouse.get_pos()
            if y.collidepoint(pos):
                x = text18
                y = rect18
                count += 1
        if event.type == pygame.MOUSEBUTTONDOWN and count==18:
            pos = pygame.mouse.get_pos()
            if y.collidepoint(pos):
                x = text19
                y = rect19
                count += 1
        if event.type == pygame.MOUSEBUTTONDOWN and count==19:
            pos = pygame.mouse.get_pos()
            if y.collidepoint(pos):
                x = text20
                y = rect20
                count += 1
        if event.type == pygame.MOUSEBUTTONDOWN and count==20:
            pos = pygame.mouse.get_pos()
            if y.collidepoint(pos):
                x = text21
                y = rect21
                count += 1
        if event.type == pygame.MOUSEBUTTONDOWN and count==21:
            pos = pygame.mouse.get_pos()
            if y.collidepoint(pos):
                x = text22
                y = rect22
                count += 1
        if event.type == pygame.MOUSEBUTTONDOWN and count==22:
            pos = pygame.mouse.get_pos()
            if y.collidepoint(pos):
                x = text23
                y = rect23
                count += 1
        if event.type == pygame.MOUSEBUTTONDOWN and count==22:
            pos = pygame.mouse.get_pos()
            if y.collidepoint(pos):
                x = text24
                y = rect24
                count += 1
        if event.type == pygame.MOUSEBUTTONDOWN and count==23:
            pos = pygame.mouse.get_pos()
            if y.collidepoint(pos):
                x = text25
                y = rect25
                count += 1
        if event.type == pygame.MOUSEBUTTONDOWN and count==23:
            pos = pygame.mouse.get_pos()
            if y.collidepoint(pos):
                x = text26
                y = rect26
                count += 1
        if event.type == pygame.MOUSEBUTTONDOWN and count==24:
            pos = pygame.mouse.get_pos()
            if y.collidepoint(pos):
                x = text27
                y = rect27
                count += 1
        if event.type == pygame.MOUSEBUTTONDOWN and count==25:
            pos = pygame.mouse.get_pos()
            if y.collidepoint(pos):
                x = text28
                y = rect28
                count += 1
        if event.type == pygame.MOUSEBUTTONDOWN and count==26:
            pos = pygame.mouse.get_pos()
            if y.collidepoint(pos):
                x = text29
                y = rect29
                count += 1
        if event.type == pygame.MOUSEBUTTONDOWN and count==27:
            pos = pygame.mouse.get_pos()
            if y.collidepoint(pos):
                x = text30
                y = rect30
                count += 1
        if event.type == pygame.MOUSEBUTTONDOWN and count==28:
            pos = pygame.mouse.get_pos()
            if y.collidepoint(pos):
                x = text31
                y = rect31
                count += 1
        if event.type == pygame.MOUSEBUTTONDOWN and count==29:
            pos = pygame.mouse.get_pos()
            if y.collidepoint(pos):
                x = text32
                y = rect32
                count += 1
        if event.type == pygame.MOUSEBUTTONDOWN and count==30:
            pos = pygame.mouse.get_pos()
            if y.collidepoint(pos):
                x = text33
                y = rect33
                count += 1
        if event.type == pygame.MOUSEBUTTONDOWN and count==31:
            pos = pygame.mouse.get_pos()
            if y.collidepoint(pos):
                x = text34
                y = rect34
                count += 1
        pygame.display.flip()
        # updates the screen so that the background and text
        # don't disappear whenever a new event happens
        # it only updates what rectangles changed on the surface
