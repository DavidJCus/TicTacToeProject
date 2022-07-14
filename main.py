"""
The following is a python program for a Tic Toe game using python with an interactive user interface. Made for the
CSI Intern Presentation.

Built in Python 3.9 using Pycharm Community Edition
"""
import tkinter as tk # this is the package that allows us to have a user interface

root = tk.Tk()

root.resizable(False, False)
root.configure(bg='#27187e')
root.title("Tic Tac Toe")

tk.Label(root, text="Tic Tac Toe", font=('Tahoma', 25), bg='#27187e', fg='#f1f2f6').pack()
status_label = tk.Label(root, text="X's Turn", font=('Tahoma', 15), bg='#758bfd', fg='#f1f2f6')
status_label.pack(fill=tk.X)

"""
The following is a function that defines what the play again button will do
"""


def play_again():
    global current_chr  # define a global variable, meaning it can be accessed anywhere in the program
    current_chr = 'X'  # set that variable to x
    for point in XO_points:  # for every button pressed
        point.button.configure(state=tk.NORMAL)  # reset the button
        point.reset()  # reset that point
    status_label.configure(text="X's Turn")  # set the label back to "X's Turn"
    play_again_button.pack_forget()  # make the play again button disappear


"""
Here is where we define the actual button that the user will see
"""
play_again_button = tk.Button(root, text='Play again', font=('Ariel', 15), command=play_again)

current_chr = "X"

play_area = tk.Frame(root, width=300, height=300, bg='white')
XO_points = []
X_points = []
O_points = []


class XOPoint:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.value = None
        self.button = tk.Button(play_area, text="", width=10, height=5, command=self.set)
        self.button.grid(row=x, column=y)

    def set(self):  # triggers when a playable tile is clicked
        global current_chr
        if not self.value:  # if a playable tile was clicked then...
            self.value = current_chr  # set the value to the current player
            if current_chr == "X":  # if it was X's turn
                self.button.configure(text=current_chr, bg='#ff8600', fg='#f1f2f6')  # set the tile to orange
                X_points.append(self)  # add that tile position to to X's points
                current_chr = "O"  # set it to O's turn
                status_label.configure(text="O's Turn")  # make the label say that it's O's turn
            elif current_chr == "O":
                self.button.configure(text=current_chr, bg='#aeb8fe', fg='#f1f2f6')
                O_points.append(self)
                current_chr = "X"
                status_label.configure(text="X's Turn")
        check_win()  # after each turn, check if there's a winner

    def reset(self):
        self.button.configure(text="", bg='lightgray')
        if self.value == "X":
            X_points.remove(self)
        elif self.value == "O":
            O_points.remove(self)
        self.value = None


"""
This populates the play area with the buttons we will use
"""
for x in range(1, 4):
    for y in range(1, 4):
        XO_points.append(XOPoint(x, y))


class WinningPossibility:
    def __init__(self, x1, y1, x2, y2, x3, y3):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.x3 = x3
        self.y3 = y3

    def check(self, for_chr):
        p1_satisfied = False  # one in a row
        p2_satisfied = False  # two in a row
        p3_satisfied = False  # three in a row
        if for_chr == 'X':
            for point in X_points:  # for every position that X has accumulated, check if it is in a winning possibility
                if point.x == self.x1 and point.y == self.y1:  # if what player chose and a winning possibility matches
                    p1_satisfied = True  # one in a row is true
                elif point.x == self.x2 and point.y == self.y2:
                    p2_satisfied = True  # two in a row is true
                elif point.x == self.x3 and point.y == self.y3:
                    p3_satisfied = True  # three in a row is true
        elif for_chr == 'O':
            for point in O_points:
                if point.x == self.x1 and point.y == self.y1:
                    p1_satisfied = True
                elif point.x == self.x2 and point.y == self.y2:
                    p2_satisfied = True
                elif point.x == self.x3 and point.y == self.y3:
                    p3_satisfied = True
        return all([p1_satisfied, p2_satisfied, p3_satisfied])


# array (list) of winning possibilities
winning_possibilities = [
    WinningPossibility(1, 1, 1, 2, 1, 3),  # if a player has their letter in (1,1) (1,2) and (1,3) they win!
    WinningPossibility(2, 1, 2, 2, 2, 3),  # if a player has their letter in (2,1) (2,2) and (2,3) they win!
    WinningPossibility(3, 1, 3, 2, 3, 3),  # if a player has their letter in (3,1) (3,2) and (3,3) they win!
    WinningPossibility(1, 1, 2, 1, 3, 1),
    WinningPossibility(1, 2, 2, 2, 3, 2),
    WinningPossibility(1, 3, 2, 3, 3, 3),
    WinningPossibility(1, 1, 2, 2, 3, 3),
    WinningPossibility(3, 1, 2, 2, 1, 3)
]


def disable_game():
    for point in XO_points:
        point.button.configure(state=tk.DISABLED)
    play_again_button.pack()


def check_win():
    for possibility in winning_possibilities:  # for every possibility in the winning possibilities, check if player's match
        if possibility.check('X'):  # if this is true, X wins (calls the check function from line 92)
            status_label.configure(text="X Won!")
            disable_game()
            return
        elif possibility.check('O'):
            status_label.configure(text="O Won!")
            disable_game()
            return
    if len(X_points) + len(
            O_points) == 9:  # if everything has been clicked but nothing matches the winning combos, draw!
        status_label.configure(text="Draw!")
        disable_game()


play_area.pack(pady=10, padx=10)

root.mainloop()
