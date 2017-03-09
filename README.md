# Dots-and-Boxes-AI

This is a artificial inteligence using competitive search and pruning for the game Dots and Boxes.

The competitive search chosen was alphabeta pruning with depth limit.

## Usage

#### DotsAndBoxes.py

DotsAndBoxes.py is the representation of the board. It comes with a method that converts the board to string. This will be userful for testing

```python
import DotsAndBoxes as dab

game = dab.DotsAndBoxes(3, 3) # creating a board 3 by 3.

game.to_string()

>>> '._._.|_*_*_|._._.|_*_*_|._._.'
```

There is also a method that receives the string of the board as input to fill the board.

```python
import DotsAndBoxes as dab

game = dab.DotsAndBoxes(3, 3)

game.input_board('._._.|_*_*_|._._.|_*_*_|._._.')

game.to_string()

>>> '._._.|_*_*_|._._.|_*_*_|._._.'
```

You can make a move as any player and print the board to try it visually on the UI.

```python
import DotsAndBoxes as dab

game = dab.DotsAndBoxes(3, 3)

game.to_string()

>>> '._._.|_*_*_|._._.|_*_*_|._._.'

game.move(0, 1, True)

game.to_string()

>>> '.X._.|_*_*_|._._.|_*_*_|._._.'
```

Additionally you can check if the game has finished using the `is_finished` method.

```python
import DotsAndBoxes as dab

game = dab.DotsAndBoxes(3, 3)

print game.is_finished()

>>> False

game.input_board('.x.x.|xWxWx|.x.x.|xWxWx|.x.x.')

print game.is_finished()

>>> True
```

#### DotsAndBoxesAI.py

DotsAndBoxesAI.py is the AI. The depth is the limit of how far it will search on the tree. Use player = True to play as white, or player = False to play as Black.

```python
import DotsAndBoxes as dab
import DotsAndBoxes as ai

game = dab.DotsAndBoxes(3, 3)

print ai.alphabeta(game, depth = 8, player = True)
>>> 0 1
```

#### DotsAndBoxesUI.py

DotsAndBoxesUI.py is a simple UI made to test board. It recevies the parameter of the board as a string.

```{r, engine=&#39;bash&#39;, code_block_name}
$ python DotsAndBoxesUI.py "._.x.|_*xWx|.x.x.|xBx*_|.x._."
```

<img src='https://cloud.githubusercontent.com/assets/4142065/23759059/6670bf20-04ca-11e7-9af1-cff390063568.png' alt='Dots and Boxes board' width='300'>

Or it can  receive the height and the width of the board.

```{r, engine=&#39;bash&#39;, code_block_name}
$ python DotsAndBoxesUI.py 3 4
```
<img src='https://cloud.githubusercontent.com/assets/4142065/23759066/6b119c3e-04ca-11e7-8ee1-61ca244ec7a7.png' alt='Dots and Boxes board' width='300'>

#### main.py

The main.py was made to test the AI. It receives as parameter the player and the board as a string. 

```{r, engine=&#39;bash&#39;, code_block_name}
$ python main.py W "._.x.|_*x*_|.x._.|xBx*_|.x._."
1 4
```
If no parameter is passed, the default will be used (a board 4x4 with the player white)

```{r, engine=&#39;bash&#39;, code_block_name}
$ python main.py
0 1
```



## License

Dots and Boxes AI is released under the [MIT License](LICENSE).