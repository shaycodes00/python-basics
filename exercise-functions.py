# Step 1: Define the light functions

def red_light():
    print("Stop! The light is red.")

def yellow_light():
    print("Caution! The light is yellow.")

def green_light():
    print("Go! The light is green.")

# Step 2: Controller function

def traffic_light(state):
    if state == "red":
        red_light()
    elif state == "yellow":
        yellow_light()
    elif state == "green":
        green_light()
    else:
        print("Error: Invalid traffic light state!")

# Calling the function

traffic_light("red")
traffic_light("yellow")
traffic_light("green")
traffic_light("blinking")

# Pedestrian Countdown

def countdown(start):
    print(f"Countdown from {start}:")
    for x in range(start, 0, -1):
        print(x)
    print("You may walk")

countdown(10)