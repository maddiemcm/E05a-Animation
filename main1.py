#Copy the contents from http://arcade.academy/examples/move_mouse.html#move-mouse and see if you can figure out what is going on. Add comments to any uncommented lines
import arcade
#this command allows python arcade to run

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
SCREEN_TITLE = "Move Mouse Example"
#determines the size of the screen that pops up when the program runs

class Ball:
    def __init__(self, position_x, position_y, radius, color):

        # Take the parameters of the init function above, and create instance variables out of them.
        self.position_x = position_x
        self.position_y = position_y
        self.radius = radius
        self.color = color

    #defines self and relates parameters like position to the ball
    def draw(self):
        """ Draw the balls with the instance variables we have. """
        arcade.draw_circle_filled(self.position_x, self.position_y, self.radius, self.color)


class MyGame(arcade.Window):

    def __init__(self, width, height, title):

        # Call the parent class's init function
        super().__init__(width, height, title)

        # Make the mouse disappear when it is over the window.
        # So we just see our object, not the pointer.
        self.set_mouse_visible(False)
        #sets the background color as ash grey)
        arcade.set_background_color(arcade.color.ASH_GREY)

        # Create our ball
        self.ball = Ball(50, 50, 15, arcade.color.AUBURN)

    #defines on draw function and renders the program, then draws the ball so it is visible on the screen
    def on_draw(self):
        """ Called whenever we need to draw the window. """
        arcade.start_render()
        self.ball.draw()

    #function of on mouse motion sets the balls position as the mouse's position and updates it
    def on_mouse_motion(self, x, y, dx, dy):
        """ Called to update our objects. Happens approximately 60 times per second."""
        self.ball.position_x = x
        self.ball.position_y = y

    #on mouse press, print "you clicked the button #..." whatever the button is. If that button is the left button which is defined by mouse button left, then set the ball color is black so long as the button is still pressed
    def on_mouse_press(self, x, y, button, modifiers):
        """
        Called when the user presses a mouse button.
        """
        print(f"You clicked button number: {button}")
        if button == arcade.MOUSE_BUTTON_LEFT:
            self.ball.color = arcade.color.BLACK
    #when the user releases the button if the button is the left button then the ball turns auburn.
    def on_mouse_release(self, x, y, button, modifiers):
        """
        Called when a user releases a mouse button.
        """
        if button == arcade.MOUSE_BUTTON_LEFT:
            self.ball.color = arcade.color.AUBURN

#main is the primary program, so the window is the game with all the perameters previously defined and then it has the function that allows the function to run after all of the setup
def main():
    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    arcade.run()


if __name__ == "__main__":
    main()
