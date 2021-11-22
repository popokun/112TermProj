from cmu_112_graphics import *
import random

# Ideas about generating levels
    # creating grid to place platforms
    # floor height remains constant
    # randomize lengths of floor sections? so that there are pit falls
    # app width and height are constant (for now)
    # width=600, height=300

# floor height = 270 (27th row cell)

# have to calculate grid size i.e. length and width of each grid cell

# platform ideas
    # for now, spawn max 5 platforms
    # when spawning platforms, must be <= 270 (floor height) (27th row)
    # platforms cannot intersect
    # platforms shouldn't be exactly at the top or exactly at the floor level
    # generate random lengths for platforms 
    # limit to number of platforms?
    # platform height = 20 (2 cells)
    # platform width shold vary (can't be less than 50 (5 cells), but should be less than 150 (15 cells))

# in the actual game file, max level x distance is 1200, so platform columns should be limited to <= 108 cells

def appStarted(app):
    app.rows = app.height//10
    app.cols = app.width//10
    app.platforms = [] 
    randomizePlatform(app)

# retrieves the bounds of the cell in coordinates
def getCellBounds(app, row, col):
    cellWidth = app.width / app.cols
    cellHeight = app.height / app.rows
    x0 = col*cellWidth
    x1 = (col+1)*cellWidth
    y0 = row*cellHeight
    y1 = (row+1)*cellHeight
    return (x0, y0, x1, y1)

# randomizes the positions of the platforms at the start of each level
def randomizePlatform(app):
    while len(app.platforms) < 5:
        x0 = random.randint(7, 20)
        x1 = x0+2
        y0 = random.randint(8, 45)
        y1 = y0+random.randint(5, 15)
        print(x0, y0, x1, y1, app.platforms)
        if len(app.platforms) != 0 and platformIntersects(app, x0, x1, y0, y1):
            continue
        app.platforms.append((x0, y0, x1, y1))

# checks if the randomized platform intersects with the latest platform added to the list
def platformIntersects(app, x0, x1, y0, y1):
    if (app.platforms[-1][0] <= x0 <= app.platforms[-1][2] or 
        app.platforms[-1][0] <= x1 <= app.platforms[-1][2]):
        return True
    # if (app.platforms[-1][1] <= y0 < (app.platforms[-1][3]+3) or 
    #     (y1+3) > app.platforms[-1][1]):
    #     return True
    return False

def redrawAll(app, canvas):
    # Drawing grid
    # for row in range(app.rows):
    #     for col in range(app.cols):
    #         (x0, y0, x1, y1) = getCellBounds(app, row, col)
    #         canvas.create_rectangle(x0, y0, x1, y1, outline='black')

    # drawing the floor with cells
    for row in range(27, 30):
        for col in range(60):
            (x0, y0, x1, y1) = getCellBounds(app, row, col)
            canvas.create_rectangle(x0, y0, x1, y1, outline='green', fill='green')
    
    # drawing platforms with cells
    # for row in range(15, 17):
    #     for col in range(8, 15):
    #         (x0, y0, x1, y1) = getCellBounds(app, row, col)
    #         canvas.create_rectangle(x0, y0, x1, y1, outline='black', fill='black')
   #print(app.platforms)

   # draws all the randomized platforms
    for platform in app.platforms:
        row0, col0, row1, col1 = platform
        for row in range(row0, row1):
            for col in range(col0, col1):
                (x0, y0, x1, y1) = getCellBounds(app, row, col)
                canvas.create_rectangle(x0, y0, x1, y1, outline='black', fill='black')

runApp(width=600, height=300)