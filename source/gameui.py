import tkinter as tk
from tkinter import *
import tensorflow as tf
import numpy as np
import collectdata


class GameUi:
    global window, buttons_list, game_no_lbl, status_label, restart_btn, saved_model, game_no, computers_previous_move, computers_moves

    def button_click(self, button):
        button['text'] = 'X'

        values_list = []
        blank_positions = []
        global computers_previous_move

        for index, button in enumerate(buttons_list):
            if button['text'] == '0':
                values_list.append(2)
            elif button['text'] == 'X':
                values_list.append(1)
            else:
                blank_positions.append(index)
                values_list.append(0)

        print(values_list)

        result = self.check_the_winner(values_list)
        if result is not None:
            # game has over computer lost
            print("computer wrong move : ", computers_previous_move)
            print("this guy has won : ", str(result))
            self.update_the_computers_moves_list(computers_previous_move, False)
            self.game_over(result)
            return

        # add the previous move
        if computers_previous_move is not None:
            self.update_the_computers_moves_list(computers_previous_move, True)

        if not blank_positions:
            # no spaces left, game has  drawn
            print("computer s correct move : ", computers_previous_move)
            self.update_the_computers_moves_list(computers_previous_move, True)
            self.draw_game()
            return

        output = self.find_the_next_move(values_list, blank_positions)
        print("next move : ", output)
        self.update_the_board(output)

        result = self.check_the_winner(output)
        if result is not None:
            # game has over
            print("computer s winning move : ", output)
            print("this guy has won : " + str(result))
            self.update_the_computers_moves_list(output, True)
            self.game_over(result)
            return

        computers_previous_move = output

    def update_the_computers_moves_list(self, move, status):
        move.append(status)
        global computers_moves
        computers_moves.append(move)
        print("updated moves list : ", computers_moves)

    def game_over(self, winner):
        print("game over started.")
        for button in buttons_list:
            button['state'] = 'disabled'

        winner_msg = ''
        if winner == 1:
            winner_msg = 'You Won!'
        else:
            winner_msg = 'Computer Won!'

        status_label['text'] = winner_msg
        restart_btn['state'] = 'normal'

    def draw_game(self):
        status_label['text'] = 'Game Drawn'
        restart_btn['state'] = 'normal'

    def check_the_winner(self, current_values_list):
        # check the horizontal winner
        winning_positions = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
        for position in winning_positions:
            if 0 != current_values_list[position[0]] == current_values_list[position[1]] == current_values_list[position[2]]:
                print("All the three values are equal")
                return current_values_list[position[0]]
            else:
                print("All the three values are not equal")

    def update_the_board(self, values_list):
        for index, value in enumerate(values_list):
            if value == 2:
                buttons_list[index]['text'] = "0"
                buttons_list[index]['state'] = "disabled"
            elif value == 1:
                buttons_list[index]['text'] = "X"
                buttons_list[index]['state'] = "disabled"
            else:
                buttons_list[index]['text'] = ""

    def find_the_next_move(self, values_list, blank_positions):
        for index, pos in enumerate(blank_positions):
            values_list[pos] = 2
            result = self.predict_output(saved_model, values_list)

            if result == 1:
                print("true")
                print("ee : ", values_list)
                return values_list
            else:
                print("false")
                if index == len(blank_positions)-1:
                    return values_list
                values_list[pos] = 0

    def __intialize_the_model(self):
        print("model initialized.")
        return tf.keras.models.load_model('saved_model')

    def predict_output(self, model, board_values_list):
        print("predict output started. ", board_values_list)
        input_list_to_model = [board_values_list]
        # received a numpy array
        predictions = model.predict(input_list_to_model)
        print(predictions)
        val_no = np.argmax(predictions[0])
        print(val_no)
        return val_no

    def __crate_the_window(self):
        global window
        window = tk.Tk()

        # window attributes
        window.geometry("300x300")
        window.title("Tic Tac Toe")
        # window attributes

        global game_no_lbl
        game_no_lbl = Label(window)
        game_no_lbl['text'] = "Game Number : "+str(game_no)
        game_no_lbl.grid(row=0, column=0, columnspan=4, pady=10, padx=(10, 2))

        # top layer
        tl_btn = Button(window, text='', height=2, width=4)
        tl_btn.configure(command=lambda: self.button_click(tl_btn))
        tl_btn.grid(row=1, column=0, sticky=W, pady=2, padx=(10, 2))

        tm_btn = Button(window, text='', height=2, width=4)
        tm_btn.configure(command=lambda: self.button_click(tm_btn))
        tm_btn.grid(row=1, column=1, sticky=W, pady=2, padx=2)

        tr_btn = Button(window, text='', height=2, width=4)
        tr_btn.configure(command=lambda: self.button_click(tr_btn))
        tr_btn.grid(row=1, column=2, sticky=W, pady=2, padx=2)
        # top layer

        # middle layer
        ml_btn = Button(window, text='', height=2, width=4)
        ml_btn.configure(command=lambda: self.button_click(ml_btn))
        ml_btn.grid(row=2, column=0, sticky=W, pady=2, padx=(10, 2))

        mm_btn = Button(window, text='', height=2, width=4)
        mm_btn.configure(command=lambda: self.button_click(mm_btn))
        mm_btn.grid(row=2, column=1, sticky=W, pady=2, padx=2)

        mr_btn = Button(window, text='', height=2, width=4)
        mr_btn.configure(command=lambda: self.button_click(mr_btn))
        mr_btn.grid(row=2, column=2, sticky=W, pady=2, padx=2)
        # middle layer

        # top layer
        bl_btn = Button(window, text='', height=2, width=4)
        bl_btn.configure(command=lambda: self.button_click(bl_btn))
        bl_btn.grid(row=3, column=0, sticky=W, pady=2, padx=(10, 2))

        bm_btn = Button(window, text='', height=2, width=4)
        bm_btn.configure(command=lambda: self.button_click(bm_btn))
        bm_btn.grid(row=3, column=1, sticky=W, pady=2, padx=2)

        br_btn = Button(window, text='', height=2, width=4)
        br_btn.configure(command=lambda: self.button_click(br_btn))
        br_btn.grid(row=3, column=2, sticky=W, pady=2, padx=2)
        # top player

        global status_label
        status_label = Label(window, text="Good Luck !", font=("Helvetica", 12), fg="blue")
        status_label.grid(row=4, column=0, columnspan=4, pady=10, padx=(10, 2))

        global restart_btn
        restart_btn = Button(window, text='Start a new game', bg="yellow", state="disabled")
        restart_btn.configure(command=self.start_a_new_game)
        restart_btn.grid(row=5, column=0, columnspan=4, pady=10, padx=(8, 2))

        global buttons_list
        buttons_list = [tl_btn, tm_btn, tr_btn, ml_btn, mm_btn, mr_btn, bl_btn, bm_btn, br_btn]

        window.mainloop()

    def start_a_new_game(self):
        print("new game started.")
        global game_no, computers_moves, computers_previous_move

        # save the moves for training
        collectdata.CollectData(computers_moves)

        # remove all items from the list
        computers_moves.clear()
        game_no = game_no + 1
        computers_previous_move = None

        game_no_lbl['text'] = "Game Number : "+str(game_no)
        status_label['text'] = "Good Luck!"
        restart_btn['state'] = 'disabled'

        for button in buttons_list:
            button['state'] = 'normal'
            button['text'] = ''

    def start_the_game(self):
        global saved_model, game_no, computers_moves, computers_previous_move
        saved_model = self.__intialize_the_model()
        game_no = 1
        computers_previous_move = None
        computers_moves = []
        self.__crate_the_window()


GameUi().start_the_game()
