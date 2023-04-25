import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# --- Read color data from a CSV file into a Pandas DataFrame object ---
# DataFrame is a data structure in Pandas that is designed for with data arranged in rows and columns
# The variable color_data stores a Pandas DataFrame


color_data = pd.read_csv(
    "colors.csv",              # CSV file to read
    skipinitialspace=True,     # Remove leading spaces from values
    comment='#',               # Ignore lines starting with '#'
    header=0,                  # First row contains column names
    sep=','                    # Values are separated by commas
)


# --- Create a new figure object in matplotlib for the scatter plot ---
scatter_plot_figure = plt.figure()

# --- Add a 3D scatter plot to the figure ---
# the variable "scatter_plot_axes" is a variable that stores an instance of the Axes3D class from the Matplotlib library
# "add_subplot()" is a method in the Matplotlib library
scatter_plot_axes = scatter_plot_figure.add_subplot(111, projection="3d")
# add_subplot() takes three integer arguments that specify the number of rows, the number of columns, and the index of the subplot to create.
    # you can use the shorthand "111" argument to create a single 3D scatter plot with a 1 x 1 grid.
        # projection="3d"is a "keyword argument" that is recognized by Matplotlib
    # the projection="3d" argument specifies that the plot should have a 3D projection.
    # The x-axis represents red, the y-axis represents green, and the z-axis represents blue.


# --- Scale down the RGB color values to the range 0-1 ---
color_data[['R', 'G', 'B']] /= 255.0
# This scales the RGB values of each data point from the range 0-255 to the range 0-1, allowing us to represent the colors using a continuous gradient, from black (0, 0, 0) to white (1, 1, 1).
# Before the RGB color values have been passed to the scatter() function
# the scatter() function in Matplotlib requires that the color values be represented as floating-point numbers between 0 and 1.


# --- Create the scatter plot ---

scatter_plot_axes.scatter(
    color_data['R'], color_data['G'], color_data['B'], # X, Y, and Z values of the plot
    c=color_data[['R', 'G', 'B']] # Colors of each point in the plot
)
    # "scatter_plot_axes.scatter()" is a method from the Matplotlib library used to create a scatter plot from the data in the Pandas DataFrame variable "color_data"
        # ARGS: scatter_plot_axes.scatter(<x-axis values>, <y-axis values>, <z-axis values>, c=<color values>).
            # From the "color_data"  DataFrame:
                # each row represents a different shade of thread
                # each column represents a different "feature" of that shade of thread
                # In this case, R,G,B values are the most important and relevant columns.
                # "DMC Name" and "Floss Number" are not relevant for creating a scatter plot of the colors
# the variable "scatter_plot_axes" stores a Axes3D object that represents the 3D scatter plot.
# allows access and manipulate the various graphical elements of the plot

# The "c" parameter in scatter() method determines the color of each data point in the scatter plot.
# set "c" equal to color_data[['R', 'G', 'B']]

# Each data point in the scatter plot is assigned a color based on its RGB values, where the red component corresponds to the x-axis, the green component corresponds to the y-axis, and the blue component corresponds to the z-axis.


# --- Add labels and title to the 3D scatter plot using the "set" methods from the Matplotlib library ---

scatter_plot_axes.set_xlabel("Red")   # Set the label for the x-axis (Red)
scatter_plot_axes.set_ylabel("Green")  # Set the label for the y-axis (Green)
scatter_plot_axes.set_zlabel("Blue")  # Set the label for the z-axis (Blue)
# Set the title for the 3D scatter plot
scatter_plot_axes.set_title("DMC Thread Colors")

# --- Display the 3D scatter plot ---

# Show the 3D scatter plot
plt.show()
