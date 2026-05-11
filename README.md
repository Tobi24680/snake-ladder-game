# Snake and Ladder Game 🎮

A Python implementation of the classic Snake and Ladder board game.

## Features

- Support for multiple players (2 or more)
- Classic 100-square board
- Random dice rolls
- Snake and ladder positions following traditional rules
- Interactive turn-based gameplay
- Visual feedback with emojis

## How to Play

1. Run the game:
   ```bash
   python snake_ladder.py
   ```

2. Enter the number of players when prompted

3. Players take turns rolling the dice by pressing Enter

4. Move according to the dice value:
   - Land on a ladder: Climb up to a higher square
   - Land on a snake: Slide down to a lower square
   - Exceed position 100: Stay in current position

5. First player to reach position 100 wins!

## Game Rules

- Players start at position 0
- On each turn, a player rolls a dice (1-6)
- Players move forward by the number shown on the dice
- Ladders allow players to jump ahead
- Snakes force players to slide backward
- If a move would take you beyond square 100, you stay at your current position
- First to reach exactly square 100 wins

## Board Positions

### Snakes (move down from):
- 16 → 6
- 47 → 26
- 49 → 11
- 56 → 53
- 62 → 19
- 87 → 24
- 93 → 73
- 95 → 75
- 98 → 79

### Ladders (move up from):
- 1 → 38
- 4 → 14
- 9 → 31
- 21 → 42
- 28 → 84
- 51 → 67
- 72 → 91
- 80 → 99

## Requirements

- Python 3.6+
- No external dependencies

## License

MIT License
