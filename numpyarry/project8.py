import numpy as np

#Speed Tracker
#Measure average speed from distance & time arrays.

distance = np.array([100,150,120])
time = np.array([2,3,2.5])
speed = distance / time
print("Speeds (km/h)",speed)

# Multiplication Table Generator
#Generate table of 2 to 10 using NumPy broadcasting.

nums = np.arange(1,11)
tables = np.arange(2,11).reshape(-1,1)* nums
print("Multiplication Tables:\n",tables)

#Shopping Cart Total
#Prices × Quantities → Grand total

prices = np.array([199,349,150])
qty = np.array([2,1,3])
total = np.sum(prices * qty)
print("Cart Total: $",total)

# Image to Grayscale Converter (Matrix Simulation)
#Simulate a grayscale image as a 2D NumPy array.
#Normalize pixel values (0–255 to 0–1).

image = np.random.randint(0,256,(5,5))
grayscale = image / 255.0
print("Normalied Image:\n",grayscale)