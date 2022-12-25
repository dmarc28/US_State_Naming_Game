# import turtle
# from turtle import Turtle, Screen
# import pandas
#
# screen = Screen()
# states = pandas.read_csv("50_states.csv")
# pos_x = states.x
# pos_y = states.y
# state_name_list = states.state.to_list()
# state_x_pos = states.x.to_list()
# state_y_pos = states.y.to_list()
#
# player_list = []
#
# class statename(Turtle):
#
#     def __init__(self):
#         super().__init__()
#         self.player_prompt()
#         self.
#
#
#     def player_prompt(self):
#         score = 0
#         prompt_counter = 0
#         if prompt_counter < 60:
#             game_on = True
#             while game_on:
#                 prompt_counter += 1
#                 attempt_left = 60 - prompt_counter
#                 player_prompt = (screen.textinput(f"You got {score}/50 so far",
#                                                   f"Name a State(attempt:{prompt_counter}/60)")).title()
#                 print(player_prompt)
#                 for x in range(len(state_name_list)):
#                     if state_name_list[x] == player_prompt:
#                         t = turtle.Turtle()
#                         t.hideturtle()
#                         t.penup()
#                         t.goto(state_x_pos[x], state_y_pos[x])
#                         print(x)
#                         print(state_x_pos[x])
#                         print(state_y_pos[x])
#                         player_list.append(state_name_list[x])
#                         t.write(player_prompt)
#                         score += 1
#                     elif player_prompt == "Done":
#                         game_on = False
#                         print(screen.textinput(f"You got {score}/50 so far","Thanks"))
#
#                         break
#                     else:
#                         continue
#                 else:
#                     continue
#             else:
#                 print(score)
#
#     def left_out_state(self):
#         left_out_list = []
#         for x in state_name_list:
#             if x not in player_list:
#                 left_out_list.append(x)
#
#