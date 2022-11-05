import random

from game.casting.actor import Actor
from game.casting.artifact import Artifact
from game.casting.cast import Cast

from game.directing.director import Director

from game.services.keyboard_service import KeyboardService
from game.services.video_service import VideoService

from game.shared.color import Color
from game.shared.point import Point


FRAME_RATE = 12
MAX_X = 900
MAX_Y = 600
CELL_SIZE = 15
FONT_SIZE = 15
COLS = 60
ROWS = 40
CAPTION = "Greed"
# DATA_PATH = os.path.dirname(os.path.abspath(__file__)) + "/data/messages.txt" # Not needed (Zack D.)
WHITE = Color(255, 255, 255)
DEFAULT_ARTIFACTS = 40


def main():
    
    # create the cast
    cast = Cast()
    
    # create the banner
    banner = Actor()
    banner.set_text("")
    banner.set_font_size(FONT_SIZE)
    banner.set_color(WHITE)
    banner.set_position(Point(CELL_SIZE, 0))
    cast.add_actor("banners", banner)

    
    
    # We will also need to make changes here so the player starts at the bottom of the screen
    # create the player
    x = int(MAX_X / 2)
    y = int(MAX_Y - 15)
    # Changed y positioning to put player at the bottom center (Jordan)
    position = Point(x, y)

    robot = Actor()
    # Changed the player shape to a basket looking shape, baskets are good for catching gems right lol? (Jordan)
    # I changed it to just a underscore because it was dificult to line up the gems with the player (Zack D.)
    robot.set_text("_")
    robot.set_font_size(FONT_SIZE)
    robot.set_color(WHITE)
    robot.set_position(position)
    cast.add_actor("robots", robot)
    
    # create the gems and rocks

    # We will need to change things here to get the gems to move and make them look the way we want (Zack D.)
    for n in range(DEFAULT_ARTIFACTS):
        text = random.choice(['*', '0'])
        # message = messages[n]

        x = random.randint(1, COLS - 1)
        y = random.randint(1, ROWS - 1)
        #Changed y value here to make objects start at the top of the screen (Jordan)
        position = Point(x, y)
        position = position.scale(CELL_SIZE)

        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        color = Color(r, g, b)
        
        artifact = Artifact()
        artifact.set_text(text)
        artifact.set_font_size(FONT_SIZE)
        artifact.set_color(color)
        artifact.set_position(position)
        cast.add_actor("artifacts", artifact)
        # We will also need to set a velocity so the artifacts move (Zack D.)
        artifact.set_velocity(Point(0,random.choice([3,5])))
        # Assign a value to the rocks
        if artifact.get_text() == "0":
            artifact.set_value(-1)

        #Trying to use turtle ycor to make the object fall from the top but can't figure out why it won't work, I'm not sure which
        # variable to use to identify the gems and stones (Jordan)
        # y = artifact(t.sety)
        # y -= 3
        # artifact(t.sety)
    
    # start the game
    keyboard_service = KeyboardService(CELL_SIZE)
    video_service = VideoService(CAPTION, MAX_X, MAX_Y, CELL_SIZE, FRAME_RATE)
    director = Director(keyboard_service, video_service)
    director.start_game(cast)

if __name__ == "__main__":
    main()
