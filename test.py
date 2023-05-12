# import numpy as np
# import matplotlib.pyplot as plt

# # Generate some random binary data
# data = np.random.randint(0, 2, size=(10, 10))

# # Create a copy of the data to avoid modifying the original array
# data_copy = data.copy()

# # Set the color of a point at (5, 7) to red
# x = 5
# y = 7
# data_copy[x, y] = 2

# # Create the plot
# fig, ax = plt.subplots()
# im = ax.imshow(data_copy, cmap="binary")

# # Change the color of the point at (5, 7) to red
# im.set_cmap("RdYlBu")

# # Show the plot
# plt.show()

import numpy as np
import matplotlib.pyplot as plt

# Generate some random data
x = np.random.rand(50)
y = np.random.rand(50)
c = np.random.rand(50)

# Define the colormap
cmap = plt.cm.get_cmap("cool")

# Create the scatter plot
plt.scatter(x, y, c=c, cmap=cmap)

# Add a colorbar
plt.colorbar()

# Show the plot
plt.show()
