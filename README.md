## What:
The [Game of Life](https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life), also
known simply as Life, is a cellular automaton devised by the British
mathematician John Horton Conway in 1970.[1] It is a zero-player game, meaning
that its evolution is determined by its initial state, requiring no further
input. One interacts with the Game of Life by creating an initial configuration
and observing how it evolves. It is Turing complete and can simulate a
universal constructor or any other Turing machine.

## How:
Ingredients:
* Raspberry Pi 4 (or probably any Pi > -1)
* Single color SSD1306 OLED display

![Hook up](http://static.mknote.us/SSD1306-ConwaysLife.png)

## Go:
Get ready to run:

```
virtualenv --system-site-packages venv
. venv/bin/activate
pip install -Ur requirements.txt
```

Run:

```
python colony.py
```
