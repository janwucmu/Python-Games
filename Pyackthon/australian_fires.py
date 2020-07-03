import pygame as pg
import random

#####################################
# Initializing entire Pygame 
#####################################
pg.init()
window = pg.display.set_mode((1000, 800))
pg.display.set_caption("Australian Fires")
# mouse coordinates
mouse_x = 0;
mouse_y = 0;
# dimensions of the forest
forest_row = 10
forest_col = 25
# types of fire
fire_types = ["ground", "surface", "crown"]
# timer
timer = 1
# counters
counterNew = 0
counterGround = 0
counterSurface = 0
counterCrown = 0
counterChemical = 0
counterChemical2 = 0
# keep the program running
running = True
# currect menu
menu = "main"
# current total score
total_score = 0
health_score = 250

#####################################
# Loading Pictures and Resizing
#####################################
width = 40
height = 50

fire_load = pg.image.load("fire.jpeg")
fire = pg.transform.scale(fire_load, (1000, 800))

water_hose_load = pg.image.load("water_hose.jpg")
water_hose = pg.transform.scale(water_hose_load, (90, 60))
water_hose_rect = water_hose.get_rect(topleft=(65,200))
water_hose_clicked = False

axe_load = pg.image.load("axe.jpg")
axe = pg.transform.scale(axe_load, (90, 60))
axe_rect = axe.get_rect(topleft=(155,200))
axe_clicked = False

chemical_load = pg.image.load("chemical.jpg")
chemical = pg.transform.scale(chemical_load, (90, 60))
chemical_rect = chemical.get_rect(topleft=(245,200))
chemical_clicked = False

tree_on_fire_load = pg.image.load("tree_fire.jpeg")
tree_on_fire = pg.transform.scale(tree_on_fire_load, (width, height))

tree_cutdown_load = pg.image.load("tree_cutdown.jpg")
tree_cutdown = pg.transform.scale(tree_cutdown_load, (width, height))

tree_load = pg.image.load("tree.png")
tree_scale = pg.transform.scale(tree_load, (width, height))
trees = []

y_global = 300
for i in range(forest_row):
    x = 0
    tree_temp = []
    for j in range(forest_col):
        tree_scale_rect = tree_scale.get_rect(topleft=(x, y_global))
        #[picture of tree, on fire?, rect of the tree, cut down?, fire_type]
        tree_temp.append([tree_scale, False, tree_scale_rect, False, "none"])
        x += width
    y_global += height
    trees.append(tree_temp)

#####################################
# Menus
#####################################
# draw main menu
def drawMain():
    window.blit(fire, (0, 0))
    drawText("Australian", 500, 250, (255, 255, 255), 115)
    drawText("Fires", 500, 350, (255, 255, 255), 115)
    pg.draw.rect(window, (0, 255, 0), (215, 500, 150, 60))
    pg.draw.rect(window, (0, 255, 0), (635, 500, 150, 60))
    drawText("Start", 290, 530, (0, 0, 0), 20)
    drawText("Awareness", 710, 530, (0, 0, 0), 20)
    for i in range(forest_row):
        for j in range(forest_col):
            curr_tree = trees[i][j]
            curr_tree[0] = tree_scale
            curr_tree[1] = False
            curr_tree[3] = False
            curr_tree[4] = "none"

# draw awareness menu
def drawAwareness():
    description1 = "Forest fires are caused by 3 different ways: naturally, human,"
    drawText(description1, 500, 40, (0, 0, 0), 25)
    description2 = "spontaneous combustion of dry fuel (sawdust or leaves)"
    drawText(description2, 500, 80, (0, 0, 0), 25)
    description3 = "There are 3 types of forest fires: ground, surface, crown"
    drawText(description3, 500, 160, (0, 0, 0), 25)
    description4 = "Ground fires are beneath the leaves,"
    drawText(description4, 500, 200, (0, 0, 0), 25)
    description5 = "surface fires are on the surface of the forest up to 1.3 meters high,"
    drawText(description5, 500, 240, (0, 0, 0), 25)
    description6 = "and crown fires are the most dangerous fires and spread fastest"
    drawText(description6, 500, 280, (0, 0, 0), 25)
    description7 = "How to Fight Fires"
    drawText(description7, 500, 360, (0, 0, 0), 25)
    description8 = "Firefighters use water, chemicals, and firebreaks to stop the spread"
    drawText(description8, 500, 400, (0, 0, 0), 25)
    description9 = "But sometimes it's so dangerous they just let it burn"
    drawText(description9, 500, 440, (0, 0, 0), 25)
    description10 = "These natural fires are caused by global warming"
    drawText(description10, 500, 520, (255, 0, 0), 40)
    description11 = "Make sure to do your part to keep our world safe"
    drawText(description11, 500, 600, (0, 200, 0), 40)
    pg.draw.rect(window, (0, 255, 0), (425, 680, 150, 60))
    drawText("Back", 500, 710, (0, 0, 0), 20)

# draw game menu
def drawGame():
    health, fire, cut = drawAllTrees()
    drawWaterHose()
    drawAxe()
    drawChemical()
    
    drawText("Keep track of your healthy, on fire, and cut down trees", 200, 25, (0, 0, 0), 15)
    drawText("Healthy: " + str(health), 200, 50, (0, 0, 255), 15)
    drawText("On Fire: " + str(fire), 200, 75, (200, 0, 0), 15)
    drawText("Cut Down: " + str(cut), 200, 100, (160, 82, 45), 15)
    drawText("Chemicals Left: " + str(15 - counterChemical), 200, 125, (0, 100, 0), 15)

    drawText("There are 3 kinds of fire: ", 750, 25, (0, 0, 0), 15)
    drawText("Ground fire expands vertically by 1 tree", 750, 50, (0, 0, 0), 15)
    drawText("Surface fire expands horizontally by 2 trees", 750, 75, (0, 0, 0), 15)
    drawText("Crown Fire expands to all its surrrounding trees by 1", 750, 100, (0, 0, 0), 15)
    
    drawText("Defend the Forest with either water, axe, or chemicals", 750, 140, (0, 0, 0), 15)
    drawText("Water puts out one tree, axe stop further spreading", 750, 165, (0, 0, 0), 15)
    drawText("Chemicals put out the tree you click and all its surroundings", 750, 190, (0, 0, 0), 15)
    drawText("Keep in mind only have 15 chemical usage per 100 secs", 750, 215, (0, 0, 0), 15)

    drawText("Each tree you save +1 point, each tree cut down -1 point", 750, 255, (255, 0, 0), 15)
    drawText("Try to get max points", 750, 280, (255, 0, 0), 15)

    pg.draw.rect(window, (0, 255, 0), (425, 15, 150, 60))
    drawText("Back", 500, 45, (0, 0, 0), 20)

    drawText("Total Points: " + str(total_score), 200, 160, (0, 0, 0), 25)
    return health

#####################################
# Drawing Helper Function
#####################################
# draw water hose
def drawWaterHose():
    window.blit(water_hose, (65, 200))
    if water_hose_clicked:
        pg.draw.circle(window, (0, 0, 255), (mouse_x, mouse_y), 7, 7)

# draw axe
def drawAxe():
    window.blit(axe, (155, 200))
    if axe_clicked:
        pg.draw.circle(window, (160, 82, 45), (mouse_x, mouse_y), 7, 7)

# draw chemical
def drawChemical():
    window.blit(chemical, (245, 200))
    if chemical_clicked:
        pg.draw.circle(window, (0, 100, 0), (mouse_x, mouse_y), 7, 7)

# drawing all the tree
def drawAllTrees():
    countCut = 0
    countHealth = 0
    countFire = 0
    for i in range(forest_row):
        for j in range(forest_col):
            curr_tree = trees[i][j]
            if (not curr_tree[1] and not curr_tree[3]):
                curr_tree[0] = tree_scale
            elif curr_tree[1]:
                curr_tree[0] = tree_on_fire
            elif curr_tree[3]:
                curr_tree[0] = tree_cutdown
            # update the data
            if curr_tree[3]:
                countCut += 1
            elif curr_tree[1]:
                countFire += 1
            else:
                countHealth += 1
            window.blit(curr_tree[0], curr_tree[2])
    return countHealth, countFire, countCut

# put text on the pygame window
def drawText(text, x, y, color, fontsize):
    largeText = pg.font.Font('freesansbold.ttf', fontsize)
    textSurface = largeText.render(text, True, color)
    textRect = textSurface.get_rect()
    textRect.center = (x, y)
    window.blit(textSurface, textRect)

#####################################
# Drawing Entire Code
#####################################
def redrawWindow():
    window.fill((255, 255, 255))
    health = 0
    if menu == "main":
        drawMain()
    elif menu == "awareness":
        drawAwareness()
    else:
        health = drawGame()
    pg.display.update()
    return health

#####################################
# Catching Fire (hunger games)
#####################################
def randomFireType():
    return random.choice(fire_types)

def randomTree():
    row = random.randint(0, forest_row - 1)
    col = random.randint(0, forest_col - 1)
    return (row, col)

def startFire(row, col, fire_type):
    if row >= 0 and row < forest_row and col >= 0 and col < forest_col:
        if not (trees[row][col])[1] and not (trees[row][col])[3]:
            (trees[row][col])[1] = True
            (trees[row][col])[4] = fire_type

def spreadFire(fire_type):
    # making a copy of the forest with fire_type and is on fire
    temp = []
    for i in range(forest_row):
        for j in range(forest_col):
            tree = trees[i][j]
            if tree[1] and tree[4] == fire_type:
                temp.append(tree)

    # spreading the fires depending on what type of fire
    for fire in temp:
        fire_y, fire_x = fire[2].x // width, (fire[2].y - 300) // height
        if fire_type == "ground":
            for this_row in range(fire_x - 1, fire_x + 2):
                startFire(this_row, fire_y, "ground")
        elif fire_type == "surface":
            for this_col in range(fire_y - 2, fire_y + 3):
                startFire(fire_x, this_col, "surface")
        elif fire_type == "crown":
            for this_row in range(fire_x - 1, fire_x + 2):
                for this_col in range(fire_y - 1, fire_y + 2):
                    startFire(this_row, this_col, "crown")

#####################################
# Putting out Fire
#####################################
def sprayWater(total_score):
    j = mouse_x // width
    i = (mouse_y - 300) // height
    on_fire = (trees[i][j])[1]
    if on_fire:
        tree_rect = (trees[i][j])[2]
        if tree_rect.collidepoint(mouse_x, mouse_y):
            total_score = endFire(i, j, total_score)
    return total_score

def cutDownTrees(total_score):
    j = mouse_x // width
    i = (mouse_y - 300) // height
    cut_down = (trees[i][j])[3]
    on_fire = (trees[i][j])[1]
    if not cut_down and not on_fire:
        tree_rect = (trees[i][j])[2]
        if tree_rect.collidepoint(mouse_x, mouse_y):
            (trees[i][j])[3] = True
            total_score -= 1
    return total_score

def sprayChemical(counterChemical, total_score):
    j = mouse_x // width
    i = (mouse_y - 300) // height
    tree_rect = (trees[i][j])[2]
    if tree_rect.collidepoint(mouse_x, mouse_y):
        counterChemical += 1
        for this_row in range(i - 1, i + 2):
            for this_col in range(j - 1, j + 2):
                total_score = endFire(this_row, this_col, total_score)
    return counterChemical, total_score

def endFire(row, col, total_score):
    if row >= 0 and row < forest_row and col >= 0 and col < forest_col:
        if (trees[row][col])[1]:
            (trees[row][col])[1] = False
            (trees[row][col])[4] = "none"
            total_score += 1
    return total_score

#####################################
# Running Mainloop
#####################################
clock = pg.time.Clock()
pg.time.set_timer(pg.USEREVENT, 1000)
while running:
    health_score = redrawWindow()

    for event in pg.event.get():
        # only quit when clicked quit
        if event.type == pg.QUIT:
            running = False
        
        # handling time (every second)
        if event.type == pg.USEREVENT: 
            timer += 1
            counterNew = 0
            counterGround = 0
            counterSurface = 0
            counterCrown = 0
            counterChemical2 = 0
       
        # position of the mouse
        mouse_x, mouse_y = pg.mouse.get_pos()
        if event.type == pg.MOUSEBUTTONDOWN:
            # the direction to menu of each button 
            if menu == "main":
                if 500 <= mouse_y and mouse_y <= 560:
                    if 215 <= mouse_x and mouse_x <= 415:
                        menu = "game"
                        timer = 1
                    elif 635 <= mouse_x and mouse_x <= 835:
                        menu = "awareness"
            elif menu == "awareness":
                if 680 <= mouse_y and mouse_y <= 740:
                    if 425 <= mouse_x and mouse_x <= 575:
                        timer = 1
                        menu = "main"
            elif menu == "game":
                if 15 <= mouse_y and mouse_y <= 75:
                    if 425 <= mouse_x and mouse_x <= 575:
                        menu = "main"
                        total_score = 0
                        counterChemical = 0
            # selection of tools
            if water_hose_rect.collidepoint(event.pos):
                water_hose_clicked = True
                axe_clicked = False
                chemical_clicked = False
            elif axe_rect.collidepoint(event.pos):
                axe_clicked = True
                water_hose_clicked = False
                chemical_clicked = False
            elif chemical_rect.collidepoint(event.pos):
                chemical_clicked = True
                water_hose_clicked = False
                axe_clicked = False
            # do something when clicked with tools
            if health_score > 0:
                if water_hose_clicked:
                    total_score = sprayWater(total_score)
                elif axe_clicked:
                    total_score = cutDownTrees(total_score)
                elif chemical_clicked:
                    if (counterChemical < 15):
                        counterChemical, total_score = sprayChemical(counterChemical, total_score)

    # dealing with timing
    clock.tick(60)

    if health_score > 0:
        # limiting the number of chemical usage
        if timer % 100 == 0:
            if counterChemical2 == 0:
                counterChemical = 0
            counterGround += 1
        
        # types of fires to spread
        if timer % 10 == 0:
            if counterCrown == 0:
                spreadFire("crown")
            counterCrown += 1
        elif timer % 5 == 0:
            if counterSurface == 0:
                spreadFire("surface")
            counterSurface += 1
        elif timer % 3 == 0:
            if counterGround == 0:
                spreadFire("ground")
            counterGround += 1
        
        # every 3 secs a new fire starts
        if timer % 2 == 0:
            if counterNew == 0:
                row, col = randomTree()
                fire_type = randomFireType()
                startFire(row, col, fire_type)
            counterNew += 1