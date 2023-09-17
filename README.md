<h1 align="center">Digital Whiteboard</h1>
</br>

<div align="center">
<img src="https://github.com/SidneyTeodoroJr/digital_whiteboard/blob/main/digital_whiteboard.png" alt="Digital Whiteboard">
</div>
</br>
</br>

This Python script creates a simple whiteboard application with a graphical interface using the tkinter library. The application allows the user to draw lines on a virtual whiteboard, choose pen colors, import images and adjust line thickness with a slider. Here is a description of the main parts of the script:

## Library Import:

The script starts by importing several tkinter libraries to create the graphical interface, manipulate colors, work with files, and perform other graphical tasks.

## Main Window Configuration:


A main window is created using `tk.Tk()`, with a title ("WHITE BOARD"), fixed size and background color set.


## Drawing Manipulation Functions

. `locate_xy(event)`: Records the mouse coordinates when the button is pressed.

. `addline(event)`: Draws a line on the screen between the previously recorded coordinates and the current mouse coordinates.

. `show_color(new_color)`: Updates the pen color.

. `new_canvas()`: Cleans the whiteboard, removing all drawings.

. `insertimage()`: Allows the user to select and insert an image into the whiteboard, which can be dragged.

. `my_callback(event)`: Moves the inserted image to the mouse position when the right mouse button is pressed and dragged.

## Icons and Graphical Interface

. Icons and buttons are added to the main window for functions such as clearing the whiteboard and importing images.

. A color palette is displayed in the left part of the window, allowing the user to choose the pen color.

## Main screen

. A canvas (Canvas) is created in the center of the main window, where the user can draw.

. Mouse events (click and drag) are linked to drawing functions.

## Slider

. A horizontal slider is added to the window to adjust the thickness of the drawing line.

. A label displays the current value selected in the slider.

## Main Loop

The main loop (`root.mainloop()`) is started to run the GUI and wait for user interaction.

In summary, this script creates a simple whiteboard application with basic drawing features, image import, and control of drawing line color and thickness. It's a great base for building a more complex painting or note-taking application.
</br>

## Contributions

<p>
Contributions are welcome! If you want to improve facial detection, add new features, or fix issues, feel free to submit a pull request. </br>If you encounter any problems or have any suggestions for improvement, you can contact me through my profile on <a href="https://github.com/SidneyTeodoroJr" target="_blank">GitHub</a> or through my social networks listed below.
</p>

<hr>
</br>

<div align="center">
<a href="https://www.facebook.com/profile.php?id=100091086461235" target="_blank"><img src="https://img.shields.io/badge/-Facebook-%230077B5?style=for-the-badge&logo=facebook&logoColor=white" style="border-radius: 30px" target="_blank"></a>
<a href="https://www.instagram.com/sidneyteodoroaraujo" target="_blank"><img src="https://img.shields.io/badge/-Instagram-%23E4405F?style=for-the-badge&logo=instagram&logoColor=white"</a>
<a href="https://www.linkedin.com/in/sidney-teodoro-4a4a8119b?lipi=urn%3Ali%3Apage%3Ad_flagship3_profile_view_base_contact_details%3B%2FevuTOiSSJS2hWGCZgtZiQ%3D%3D" target="_blank"><img src="https://img.shields.io/badge/-LinkedIn-%230077B5?style=for-the-badge&logo=linkedin&logoColor=white" style="border-radius: 30px" target="_blank"></a>
</div>
