import sys

def sum_values(x, y):
    result = x + y
    # print("The sum of", x, "and", y, "is:", result)
    return result

# Check if the correct number of command-line arguments is provided
# if len(sys.argv) != 3:
#     print("Error: Incorrect number of arguments. Expected 2.")
#     sys.exit(1)

x = int(sys.argv[1])
y = int(sys.argv[2])

# sum_values(x, y)  # Calling the function with x and y

# from ansys.mapdl.core import launch_mapdl
# import time 
# print(2+2)
# print("hi")
# start mapdl
# mapdl = launch_mapdl()
# print(mapdl)

# time.sleep(5)

# mapdl.exit()
