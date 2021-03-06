"""
Your chance to explore Loops and Turtles!

Authors: David Mutchler, Dave Fisher, Vibha Alangar, Amanda Stouder,
         their colleagues and Ethan.
"""
###############################################################################
# Done: 1.
#   On Line 5 above, replace  PUT_YOUR_NAME_HERE  with your own name.
###############################################################################

###############################################################################
# TODO: 2.
#   You should have RUN the  m5e_loopy_turtles  module and READ its code.
#   (Do so now if you have not already done so.)
#
#   Below this comment, add ANY CODE THAT YOU WANT, as long as:
#     1. You construct at least 2 rg.SimpleTurtle objects.
#     2. Each rg.SimpleTurtle object draws something
#          (by moving, using its rg.Pen).  ANYTHING is fine!
#     3. Each rg.SimpleTurtle moves inside a LOOP.
#
#   Be creative!  Strive for way-cool pictures!  Abstract pictures rule!
#
#   If you make syntax (notational) errors, no worries -- get help
#   fixing them at either this session OR at the NEXT session.
#
#   Don't forget to COMMIT-and-PUSH when you are done with this module.
###############################################################################
import rosegraphics as rg

bloggy = rg.SimpleTurtle('turtle')
bloggy.pen = rg.Pen('Midnight Blue', 10)
criggy = rg.SimpleTurtle()
criggy.pen = rg.Pen('Green', 10)
window = rg.TurtleWindow()
criggy.speed = 30
size = 5
bloggy.speed = 40


for x in range(200):
    bloggy.right(45)
    bloggy.forward(size)
    bloggy.right(80)
    bloggy.forward(size)
    criggy.left(45)
    criggy.forward(size)
    criggy.left(80)
    criggy.forward(size)
    size += 5

window.close_on_mouse_click()
