
# Game timer (30 seconds)
def on_update_interval():
    if game.runtime() >= 30000:
        game.over(True)
icon2: Sprite = None
food2: Sprite = None
# Create the player sprite
my_sprite = sprites.create(img("""
        . . . . f f f f . . . .
            . . f f e e e e f f . .
            . f f e e e e e e f f .
            f f f f 4 e e e f f f f
            f f f 4 4 4 e e f f f f
            f f f 4 4 4 4 e e f f f
            f 4 e 4 4 4 4 4 4 e 4 f
            f 4 4 f 8 4 4 8 f 4 4 f
            f e 4 4 4 4 4 4 4 4 e f
            . f e 4 4 3 3 4 4 e f .
            . f f e 4 4 4 4 e f f .
            e 4 f b 5 5 5 5 b f 4 e
            4 d f 5 5 5 5 5 5 f d 4
            4 4 f 5 5 5 5 5 5 f 4 4
            . . . f f f f f f . . .
            . . . f f . . f f . . .
    """),
    SpriteKind.player)
# Move the player with the arrow keys
controller.move_sprite(my_sprite, 100, 0)
my_sprite.set_flag(SpriteFlag.STAY_IN_SCREEN, True)
computerIconKind = SpriteKind.create()
foodIconKind = SpriteKind.create()
# Create computer icons and food icons lists
computer_icons = [0]
# List for computer icons
food_icons = [0]
# Start the game
info.start_countdown(30)
game.splash("Task Master")

def on_update_interval2():
    global food2
    food2 = sprites.create(img("""
            .............beebbbb............
                    ............eebbbb4bb...........
                    ............eb344bb4bb..........
                    ............e44334bb4bb.........
                    ............eb433344b4be........
                    ............4eb43344444be.......
                    ...........bd4eb43333344bb......
                    ..........b455d4443333444bb.....
                    ..........4d5555d444333444bb....
                    .........4555555dd4b4443444be...
                    ........bd5555d555d4bb444444ee..
                    ........b55ddd665555bb4b44444ee.
                    .......bd5555677655554ebb44444eb
                    .......43222558855555d4eeb44b4ee
                    ......b422332ddd555222d4eebbb4be
                    ......be22232ed55522332db4ebbbbe
                    .....bde22222e555e22232edd4bbbbe
                    .....b52e222e3555e22222eddd4ebee
                    ....bd552eee355552e222e355544eee
                    ....665dd5555555552eee355dd4deee
                    ...6776555555555555555551554d4ee
                    ...4885222555dddd6655551544d4eee
                    ..b45522332555dd677611d444ddeee.
                    ..4d5222232e55555881d44ddd4eee..
                    .bdd5e22222e555115114d54d4ee....
                    .b55d2e222e351144d1d55eeee......
                    bd5ddd2eee3d444555dd4e..........
                    b555115dddd55d544eede...........
                    4511d444d5544ee...4de...........
                    41d4555d4ee........44...........
                    41554eede.......................
                    44ee...4e.......................
        """),
        foodIconKind)
    # Set kind to food
    food2.set_position(randint(10, 150), 0)
    food2.set_velocity(0, randint(40, 80))
    food_icons.append(foodIconKind)
game.on_update_interval(1000, on_update_interval2)

def on_update_interval3():
    global icon2
    icon2 = sprites.create(img("""
            . . . b b b b b b b b b . . . .
                    . . b 1 d d d d d d d 1 b . . .
                    . b 1 1 1 1 1 1 1 1 1 1 1 b . .
                    . b d b c c c c c c c b d b . .
                    . b d c 6 6 6 6 6 6 6 c d b . .
                    . b d c 6 d 6 6 6 6 6 c d b . .
                    . b d c 6 6 6 6 6 6 6 c d b . .
                    . b d c 6 6 6 6 6 6 6 c d b . .
                    . b d c 6 6 6 6 6 6 6 c d b . .
                    . b d c c c c c c c c c d b . .
                    . c b b b b b b b b b b b c . .
                    c b c c c c c c c c c c c b c .
                    c 1 d d d d d d d d d d d 1 c .
                    c 1 d 1 1 d 1 1 d 1 1 d 1 1 c .
                    c b b b b b b b b b b b b b c .
                    c c c c c c c c c c c c c c c .
        """),
        computerIconKind)
    # Set kind to computer
    icon2.set_position(randint(10, 150), 0)
    icon2.set_velocity(0, randint(40, 80))
    computer_icons.append(computerIconKind)
game.on_update_interval(1000, on_update_interval3)

# Computer icon overlap

def on_on_overlap(player22, food):
    food.destroy()
    # Remove the food icon
    info.change_score_by(-1)
sprites.on_overlap(SpriteKind.player, foodIconKind, on_on_overlap)

# Create new computer and food icons every second

def on_on_overlap2(player2, icon):
    icon.destroy()
    # Remove the computer icon
    info.change_score_by(1)
sprites.on_overlap(SpriteKind.player, computerIconKind, on_on_overlap2)

