import pgzrun
WIDTH = 600
HEIGHT = 600
basket = Actor("basket")
basket.pos = (300, 550)
score = 0
currentlevel = 0
game_over = False
game_complete = False
items = []
levels = [("fresh", "rotten"),("clean", "dirty"),("picmat", "torn"),("potato", "crisps")]
def make_items():
    global items
    items = []
    for i in levels[currentlevel]:
        item = Actor(i)
        items.append(item)
    items[0].pos = (200, 0)
    items[1].pos = (400, 0)
    animate(items[0], y=HEIGHT, duration=5)
    animate(items[1], y=HEIGHT, duration=5)
def draw():
    screen.blit("picnic", (0, 0))
    if game_over:
        screen.draw.text("GAME OVER Score: " + str(score), (150, 300))
    elif game_complete:
        screen.draw.text("YOU WIN Score: " + str(score), (150, 300))
    else:
        basket.draw()
        for i in items:
            i.draw()
        screen.draw.text("Score: " + str(score), (10, 10))
def update():
    global score, currentlevel, game_over, game_complete
    if game_over or game_complete:
        return
    if keyboard.a:
        basket.x -= 10
    if keyboard.d:
        basket.x += 10
    basket.x = max(0, min(WIDTH, basket.x))
    if basket.colliderect(items[0]):
        score += 50
        currentlevel += 1
        if currentlevel > 3:
            game_complete = True
        else:
            make_items()
    if basket.colliderect(items[1]):
        score -= 50
        game_over = True
    if items and items[0].y >= HEIGHT:
        game_over = True
make_items()
pgzrun.go()
