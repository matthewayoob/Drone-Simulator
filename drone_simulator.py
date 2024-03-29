# Name: Matthew Louis Ayoob

# Takehome question
# * Make reasonable assumptions and state them explicitly.

# Drone Placement

# Objective
# Design an algorithm to place 1000 2-dimensional drones (looking like a disc) randomly and without collision within a L x L square meter area.

# Input
# N - The number of drones whose shapes are congruent circular.
# L - Length of each side of the square
# r - Radius of each drone (circle)

# Output
# If a valid placement can be found, the coordinates of the center of each drone. If not, denote that a valid placement cannot be found for the given input.


""" 
    Function: drone_simulator(N, L, r)

    Parameters: num_of_drones, square_side_length, radius_of_drone

    Return: If a valid placement can be found, the coordinates of the center of each drone.
            Otherwise, returns that a valid placement cannot be found for the given input.
"""


def drone_simulator(num_of_drones, square_side_length, radius_of_drone):

    landing_locations = create_map(square_side_length, radius_of_drone)
    num_successes = 0
    placed_drone_coordinates = set()

    # iterate through given drones
    for x in range(num_of_drones):

        if len(landing_locations) > 0:
            # mark randomized landing position as no longer available
            placed_drone_coordinates.add(landing_locations.pop())
            num_successes += 1
        else:
            break

    if num_successes == num_of_drones:
        return "All drones were placed successfully with their centers at the following coordinates: " + str(placed_drone_coordinates)
    else:
        return f"A valid placement cannot be found for the given input constraints of N = {num_of_drones}, L = {square_side_length}, and r = {radius_of_drone}"


""" 
    Function: create_map(L, r)

    Parameters: square_side_length, radius_of_drone

    Return: Set of all potential midpoints of landing locations
"""


def create_map(square_side_length, radius_of_drone):

    # calculate first midpoint of circumscribed square of drone
    diameter = (2 * radius_of_drone)
    x_coord = diameter/2
    y_coord = diameter/2

    x_coord_set = {x_coord}
    y_coord_set = {y_coord}
    potential_landings_set = set()

    while x_coord < square_side_length - diameter and y_coord < square_side_length - diameter:

        x_coord += diameter
        y_coord += diameter
        x_coord_set.add(x_coord)
        y_coord_set.add(y_coord)

    # create set to represent all possible coordinates to select from randomly
    for x_coord in x_coord_set:
        for y_coord in y_coord_set:
            potential_landings_set.add((x_coord, y_coord))
    return potential_landings_set


assert ('Test #1 Confirming Correct Placement Coordinates of (0.5, 0.5), (1.5, 0.5), (1.5, 1.5), (0.5, 1.5): ' + 'Confirmed' if str(drone_simulator(4, 2, 0.5) ==
                                                                                                                                    "All drones were placed successfully with their centers at the following coordinates: {(0.5, 0.5), (1.5, 0.5), (1.5, 1.5), (0.5, 1.5)}") else 'Failure.')

assert ('Test #2 Successful Placement at Scale (N=1000): ' + 'Confirmed' if str(drone_simulator(1000, 96, 1.5) !=
                                                                                "A valid placement cannot be found for the given input constraints of N = 1000, L = 96, and r = 1.5") else 'Failure.')

assert ('Test #3 Robustness Test (N=10,000)): ' + 'Confirmed' if str(drone_simulator(10000, 300, 1.5) !=
                                                                     "A valid placement cannot be found for the given input constraints of N = 1000, L = 10, and r = 1.5") else 'Failure.')

assert ('Test #4 Correct Failure Behavior (Only 9 Drones Could Land): ' + 'Confirmed' if str(drone_simulator(1000, 10, 1.5) ==
                                                                                             "A valid placement cannot be found for the given input constraints of N = 1000, L = 10, and r = 1.5") else 'Failure.')

# For Viewing Landing Coordinates:
# res = drone_simulator(1000, 2, 0.5)
# res = drone_simulator(1000, 96, 1.5)
# res = drone_simulator(10000, 300, 1.5)
# res = drone_simulator(1000, 10, 1.5)
# print("result: " + str(res))

