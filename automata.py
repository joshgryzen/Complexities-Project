import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from rules import rules


# Set up the initial state of the automaton
num_steps = 50
# width = 200
state = np.zeros((num_steps, 100), dtype=int)
state[0, 50] = 1

supported_rules = ""

for key in rules.keys():
    supported_rules += str(key) + ", "

print(f"Currently supported rules: {supported_rules}")

rule_num = input("Select a rule: ")
rule_name = "Rule " + rule_num

while rule_name not in rules:
    print("Please select a supported rule and input the number only.")
    rule_num = input("Select a rule: ")
    rule_name = "Rule " + rule_num

# Define the rule
rule = rules[rule_name]
# print(f"keys: {list(rules.keys())}, index: [{list(rules.values()).index(rule)}]")
# rule_name = list(rules.keys())[list(rules.values()).index(rule)]
# rule_name = "Rule 150"


fig = plt.figure(num="Automata " + rule_name)
plt.title(rule_name)
im = plt.imshow(state, cmap="binary")


def apply_rule(state, rule):
    # Apply the rule to the current state
    new_state = np.zeros_like(state)
    for i in range(1, len(state) - 1):
        left = state[i - 1]
        center = state[i]
        right = state[i + 1]
        new_state[i] = rule[left, center, right]
    return new_state


def visualize_state(state):
    # Visualize the current state of the automaton
    # plt.clf()
    plt.imshow(state, cmap="binary", interpolation="nearest")
    plt.axis("off")
    plt.show()
    # plt.pause(1)  # Pause for 0.1 seconds
    # plt.close("all")


def animate(frame):
    if frame == num_steps - 1:
        ani.event_source.stop()
        return
    state[frame + 1] = apply_rule(state[frame], rule)
    im.set_array(state)
    return [im]


ani = animation.FuncAnimation(fig, animate, frames=num_steps, interval=0.5)


def get_state():
    view_state()
    return state


def view_state():
    plt.show()


# view_state()
full_state = get_state()
# print(full_state)
# visualize_state(full_state)
# view_state()
# fig = plt.figure()
# im = plt.imshow(state, cmap="binary")
# ani = animation.FuncAnimation(fig, animate, frames=num_steps, interval=1)
# plt.show()
# print(state)
