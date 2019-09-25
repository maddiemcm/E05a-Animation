#Copy the contents from http://arcade.academy/examples/move_keyboard.html#move-keyboard and see if you can figure out what is going on. Add comments to any uncommented lines
import arcade

#sets and defines screen perameters, title and the movement speed
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
SCREEN_TITLE = "Move Keyboard Example"
MOVEMENT_SPEED = 3

# the class of ball is for all the specifics of game function relating to ball
class Ball:
    def __init__(self, position_x, position_y, change_x, change_y, radius, color):

        # Take the parameters of the init function above, and create instance variables out of them.
        self.position_x = position_x
        self.position_y = position_y
        self.change_x = change_x
        self.change_y = change_y
        self.radius = radius
        self.color = color
        # above definitions are defining all of these different aspects of the ball like its position, the change in position, the radius and the color

    # this function draws/creates the ball on the screen and makes it a filled circle. then it gives it the previously defined perameters
    def draw(self):
        """ Draw the balls with the instance variables we have. """
        arcade.draw_circle_filled(self.position_x, self.position_y, self.radius, self.color)

    #updates the state of the ball/self with the position of y by calculating the change in position and then does the same for x, also asks a series of if statements concerning state of direction of the ball
    def update(self):
        # Move the ball
        self.position_y += self.change_y
        self.position_x += self.change_x

        # See if the ball hit the edge of the screen. If so, change direction
        if self.position_x < self.radius:
            self.position_x = self.radius
        #if the ball position along the x- axis is beyond the screen width minus the ball's radius then do not allow it to pass the screen width
        if self.position_x > SCREEN_WIDTH - self.radius:
            self.position_x = SCREEN_WIDTH - self.radius
        #if the ball position along y is within the radius then the ball is doing the right thing and can continue moving, being visible, its current state whatever
        if self.position_y < self.radius:
            self.position_y = self.radius
        #same ideas as before but with y axis
        if self.position_y > SCREEN_HEIGHT - self.radius:
            self.position_y = SCREEN_HEIGHT - self.radius

#class of my game is a series of functions concerning game functions and setup specifically
class MyGame(arcade.Window):
    #sets self, width, height and title of screen/game
    def __init__(self, width, height, title):

        # Call the parent class's init function
        super().__init__(width, height, title)

        # Make the mouse disappear when it is over the window.
        # So we just see our object, not the pointer.
        self.set_mouse_visible(False)
        #sets arcade background color to ash grey
        arcade.set_background_color(arcade.color.ASH_GREY)

        # Create our ball
        self.ball = Ball(50, 50, 0, 0, 15, arcade.color.AUBURN)

    #on draw of game/self, render the game and draw the ball on the screen
    def on_draw(self):
        """ Called whenever we need to draw the window. """
        arcade.start_render()
        self.ball.draw()
    #updates thte ball movements in relation to the screen and movement time
    def update(self, delta_time):
        self.ball.update()
    #on key press, identifies keys, modifiers and the window
    def on_key_press(self, key, modifiers):
        """ Called whenever the user presses a key. """
        #if the pressed key is the arcade key left, then move ball left among the x axis
        if key == arcade.key.LEFT:
            self.ball.change_x = -MOVEMENT_SPEED
        #if the pressed key is right, then move the ball right along the x axis
        elif key == arcade.key.RIGHT:
            self.ball.change_x = MOVEMENT_SPEED
        #if the key pressed is up then move the ball up along the y axis
        elif key == arcade.key.UP:
            self.ball.change_y = MOVEMENT_SPEED
        #if the key pressed is down, move the ball down along the y axis 
        elif key == arcade.key.DOWN:
            self.ball.change_y = -MOVEMENT_SPEED
    #on the key release, stop movement no matter the axis or position
    def on_key_release(self, key, modifiers):
        """ Called whenever a user releases a key. """
        if key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.ball.change_x = 0
        elif key == arcade.key.UP or key == arcade.key.DOWN:
            self.ball.change_y = 0

# main game function, run game and set previously defined parameters
def main():
    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    arcade.run()


if __name__ == "__main__":
    main()
