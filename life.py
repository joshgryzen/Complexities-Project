import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from automata import get_state
import math

# Set up the board with a cellular automata rule
board = get_state()

# 20 for small, 40 for medium, 60 for large
board = np.pad(board, 20)
x_1 = len(board)
x_2 = len(board[0])

temp_entropies = []
average_entropies = []
highest_entropies = []
sub_boards = []


# Get num of zeros
# Get num of 1s
# Formula -> -(P(0))*(logP(0) + P(1)*logP(1))
def calc_entropy(sub):
    entropy = 0
    ones = 0
    zeroes = 0
    if sub.size > 0:
        ones = np.sum(sub)
        zeroes = (len(sub) * len(sub[0])) - ones
        if ones + zeroes != 0:
            p_ones = (ones) / (ones + zeroes)
            p_zeroes = (zeroes) / (ones + zeroes)
            log_ones = math.log2(p_ones) if p_ones != 0 else 0
            log_zeroes = math.log2(p_zeroes) if p_zeroes != 0 else 0
            entropy = -(p_ones * log_ones + p_zeroes * log_zeroes)

    return entropy


# Define the rules for updating the board
def update_board(board):
    new_board = np.zeros((x_1, x_2))
    temp_entropies.clear()
    for i in range(x_1):
        for j in range(x_2):
            # Count the number of live neighbors
            sub_board = board[i - 1 : i + 2, j - 1 : j + 2]
            sub_board_medium = board[i - 2 : i + 3, j - 2 : j + 3]
            sub_board_large = board[i - 3 : i + 4, j - 3 : j + 4]
            num_neighbors = np.sum(sub_board) - board[i, j]
            temp_entropies.append(calc_entropy(sub_board_large))
            # Apply the rules of the game
            if board[i, j] == 1 and (num_neighbors == 2 or num_neighbors == 3):
                new_board[i, j] = 1
            elif board[i, j] == 0 and num_neighbors == 3:
                new_board[i, j] = 1
    # Add the average entropy of the board
    average_entropies.append(sum(temp_entropies) / len(temp_entropies))
    highest_entropies.append(max(temp_entropies))
    return new_board


# Set up the animation
fig = plt.figure(num="Game of Life")
im = plt.imshow(board, cmap="binary")


def animate(frame):
    global board
    board = update_board(board)
    im.set_array(board)
    return [im]


# Start the animation
ani = animation.FuncAnimation(fig, animate, frames=100, interval=1)
plt.show()

x_lab = range(0, len(average_entropies))
y_lab = average_entropies
plt.plot(x_lab, y_lab)
plt.xlabel("Board State by frame")
plt.ylabel("Average Entropy")
plt.title("Entropy over Time")
plt.show()

x_lab = range(0, len(highest_entropies))
y_lab = highest_entropies
plt.plot(x_lab, y_lab)
plt.xlabel("Board State by frame")
plt.ylabel("Highest Entropies")
plt.title("Entropy over Time")
plt.show()
