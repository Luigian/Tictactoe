# Tictactoe

## An AI to play Tic-Tac-Toe.

<img src="resources/tictactoe_output.png" width="600">

Tic-Tac-Toe is a paper-and-pencil game for two players, X and O, who take turns marking the spaces in a 3×3 grid. The player who succeeds in placing three of their marks in a diagonal, horizontal, or vertical row is the winner. It is a solved game with a forced draw assuming best play from both players. Using Minimax algorithm, we can implement an AI to play Tic-Tac-Toe optimally.

**Minimax**

**Propositional Logic**

Knowledge-based agents make decisions by considering their knowledge base, and making inferences based on that knowledge. One way we could represent an AI’s knowledge about a Minesweeper game is by making each cell a propositional variable that is true if the cell contains a mine, and false otherwise.

The AI would know every time a safe cell is clicked on and would get to see the number of neighboring cells that are mines for that cell.

**Knowledge Representation**

We’ll represent each sentence of our AI’s knowledge like the below.

`{A, B, C, D, E, F, G, H} = 1`

Every logical sentence in this representation has two parts: a set of cells on the board that are involved in the sentence, and a number count, representing the count of how many of those cells are mines. The above logical sentence says that out of cells A, B, C, D, E, F, G, and H, exactly 1 of them is a mine.

This is useful because it lends itself well to certain types of inference:

- Any time we have a sentence whose count is 0, we know that all of that sentence’s cells must be safe.
- Any time the number of cells is equal to the count, we know that all of that sentence’s cells must be mines.
- Any time we have two sentences set1 = count1 and set2 = count2 where set1 is a subset of set2, then we can construct the new sentence set2 - set1 = count2 - count1.

In general, we only want our sentences to be about cells that are not yet known to be either safe or mines. This means that, once we know whether a cell is a mine or not, we can update our sentences to simplify them and potentially draw new conclusions.

So using this method of representing knowledge, the AI agent can gather knowledge about the Minesweeper board, and select cells it knows to be safe.

## Implementation

There are two main files in this project: `runner.py`, which contains all of the code to run the graphical interface for the game; and `tictactoe.py`, which contains all of the logic for playing the game, and for making optimal moves.

In `tictactoe.py`, we define three variables: `X`, `O`, and `EMPTY`, to represent possible moves of the board.

The function `initial_state` returns the starting state of the board. For this problem, we represent the board as a list of three lists (representing the three rows of the board), where each internal list contains three values that are either `X`, `O`, or `EMPTY`.

The `player` function takes a `board` state as input, and returns which player’s turn it is (either `X` or `O`). In the initial game state, `X` gets the first move. Subsequently, the player alternates with each additional move.

The `actions` function returns a set of all of the possible actions that can be taken on a given board. Each action is represented as a tuple `(i, j)` where `i` corresponds to the row of the move (0, 1, or 2) and `j` corresponds to which cell in the row corresponds to the move (also 0, 1, or 2). Possible moves are any cells on the board that do not already have an `X` or an `O` in them.

The `result` function takes a `board` and an `action` as input, and returns a new board state, without modifying the original board. If `action` is not a valid action for the board, your program should raise an exception. The returned board state is the board that would result from taking the original input board, and letting the player whose turn it is make their move at the cell indicated by the input action. The original board is left unmodified: since Minimax will ultimately require considering many different board states during its computation.

The `winner` function accepts a board as input, and returns the winner of the board if there is one. One can win the game with three of their moves in a row horizontally, vertically, or diagonally. If there is no winner of the game (either because the game is in progress, or because it ended in a tie), the function returns `None`.

The `terminal` function accepts a board as input, and returns a boolean value indicating whether the game is over. If the game is over, either because someone has won the game or because all cells have been filled without anyone winning, the function returns `True`. Otherwise, the function returns `False` if the game is still in progress. 

The `utility` function accepts a terminal board as input and output the utility of the board. If `X` has won the game, the utility is `1`. If `O` has won the game, the utility is `-1`. If the game has ended in a tie, the utility is `0`.

The `minimax` function takes a board as input, and returns the optimal move for the player to move on that board. The move returned is the optimal action `(i, j)` that is one of the allowable actions on the board. If multiple moves are equally optimal, any of those moves is acceptable. If the board is a terminal board, the `minimax` function returns None.

Since Tic-Tac-Toe is a tie given optimal play by both sides, you should never be able to beat the AI (though if you don’t play optimally as well, it may beat you).

--------------------------

There are two main files in this project,`runner.py`, which contains all of the code to run the graphical interface for the game; and `minesweeper.py`, which contains all of the logic the game itself and for the AI to play the game.

In `minesweeper.py` there are three classes defined, `Minesweeper`, which handles the gameplay; `Sentence`, which represents a logical sentence that contains both a set of cells and a count; and `MinesweeperAI`, which handles inferring which moves to make based on knowledge.

Each cell is a pair `(i, j)` where `i` is the row number (ranging from `0` to `height - 1`) and `j` is the column number (ranging from `0` to `width - 1`).

**The `Sentence` class**

This class is used to represent logical sentences of the form described before. Each sentence has a set of `cells` within it and a `count` of how many of those cells are mines. 

The class also contains functions `known_mines` and `known_safes` for determining if any of the cells in the sentence are known to be mines or known to be safe. 

It also contains functions `mark_mine` and `mark_safe` to update a sentence in response to new information about a cell.

**The `MinesweeperAI` class**

This class will implement an AI that can play Minesweeper. The AI class keeps track of a number of values. `self.moves_made` contains a set of all cells already clicked on, so the AI knows not to pick those again. `self.mines` contains a set of all cells known to be mines. `self.safes` contains a set of all cells known to be safe. And `self.knowledge` contains a list of all of the Sentences that the AI knows to be true.

The `mark_mine` function adds a cell to `self.mines`, so the AI knows that it is a mine. It also loops over all sentences in the AI’s knowledge and informs each sentence that the cell is a mine, so that the sentence can update itself accordingly if it contains information about that mine. The `mark_safe` function does the same thing, but for safe cells instead.

The `add_knowledge` takes as input a `cell` and its corresponding `count`, and updates `self.mines`, `self.safes`, `self.moves_made`, and `self.knowledge` with any new information that the AI can infer, given that `cell` is known to be a safe cell with `count` mines neighboring it. The function adds a new sentence to the AI’s knowledge base, based on the value of `cell` and `count`, including only cells whose state is still undetermined in the sentence. If, based on any of the sentences in `self.knowledge`, new cells can be marked as safe or as mines, or, new sentences can be inferred (using the subset method described before), then the function does so. 

Any time that we make any change to our AI’s knowledge, it may be possible to draw new inferences that weren’t possible before. That's why the function loops over and over until there's no change made, so we can be sure that those new inferences are added to the knowledge base.

The `make_safe_move` function returns a move `(i, j)` that is known to be safe, and not a move already made. If no safe move can be guaranteed, the function returns `None`. The function don't modify `self.moves_made`, `self.mines`, `self.safes`, or `self.knowledge`.

The `make_random_move` function is called if a safe move is not possible and returns a random move `(i, j)`. The move isn't a move that has already been made or a move that is known to be a mine. If no such moves are possible, the function returns `None`.

When we run our AI (as by clicking “AI Move”), note that it will not always win. There will be some cases where the AI must guess, because it lacks sufficient information to make a safe move. This is to be expected. `runner.py` will print whether the AI is making a move it believes to be safe or whether it is making a random move.

## Resources
* [Search - Lecture 0 - CS50's Introduction to Artificial Intelligence with Python 2020][cs50 lecture]

## Usage

**To install pygame:**

* Inside the `tictactoe` directory: `pip3 install -r requirements.txt`

**To play Tic-Tac-Toe against the AI:** 

* Inside the `tictactoe` directory: `python runner.py`

## Credits
[*Luis Sanchez*][linkedin] 2020.

Project and images from the course [CS50's Introduction to Artificial Intelligence with Python 2020][cs50 ai] from HarvardX.

[cs50 lecture]: https://youtu.be/D5aJNFWsWew?t=4324
[linkedin]: https://www.linkedin.com/in/luis-sanchez-13bb3b189/
[cs50 ai]: https://cs50.harvard.edu/ai/2020/
