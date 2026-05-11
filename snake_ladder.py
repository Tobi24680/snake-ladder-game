import random
from typing import Dict, List, Tuple

class SnakeLadderGame:
    """A Snake and Ladder board game implementation."""
    
    def __init__(self, num_players: int = 2, board_size: int = 100):
        """
        Initialize the game.
        
        Args:
            num_players: Number of players in the game (default: 2)
            board_size: Size of the board (default: 100)
        """
        self.board_size = board_size
        self.num_players = num_players
        self.players = {f"Player {i+1}": 0 for i in range(num_players)}
        self.current_player = 0
        self.player_names = list(self.players.keys())
        
        # Define snakes and ladders
        self.snakes = {
            16: 6, 47: 26, 49: 11, 56: 53, 62: 19,
            87: 24, 93: 73, 95: 75, 98: 79
        }
        self.ladders = {
            1: 38, 4: 14, 9: 31, 21: 42, 28: 84,
            51: 67, 72: 91, 80: 99
        }
    
    def roll_dice(self) -> int:
        """Roll a six-sided dice."""
        return random.randint(1, 6)
    
    def get_new_position(self, current_pos: int, dice_value: int) -> int:
        """
        Calculate new position after rolling dice, considering snakes and ladders.
        
        Args:
            current_pos: Current position on the board
            dice_value: Value rolled on the dice
            
        Returns:
            New position after applying snakes/ladders rules
        """
        new_pos = current_pos + dice_value
        
        # Check if position exceeds board size
        if new_pos > self.board_size:
            return current_pos
        
        # Check for snakes
        if new_pos in self.snakes:
            print(f"  🐍 Snake! Sliding down from {new_pos} to {self.snakes[new_pos]}")
            new_pos = self.snakes[new_pos]
        
        # Check for ladders
        elif new_pos in self.ladders:
            print(f"  🪜 Ladder! Climbing up from {new_pos} to {self.ladders[new_pos]}")
            new_pos = self.ladders[new_pos]
        
        return new_pos
    
    def play_turn(self) -> bool:
        """
        Execute one player's turn.
        
        Returns:
            True if the player wins, False otherwise
        """
        player_name = self.player_names[self.current_player]
        current_pos = self.players[player_name]
        
        print(f"\n{'='*50}")
        print(f"{player_name}'s turn (Currently at position {current_pos})")
        print(f"{'='*50}")
        
        input("Press Enter to roll the dice...")
        dice_value = self.roll_dice()
        print(f"🎲 Rolled: {dice_value}")
        
        new_pos = self.get_new_position(current_pos, dice_value)
        self.players[player_name] = new_pos
        
        print(f"➡️  Moved to position {new_pos}")
        
        # Check if player wins
        if new_pos == self.board_size:
            print(f"\n🎉 {player_name} reached position {self.board_size} and won! 🎉")
            return True
        
        # Move to next player
        self.current_player = (self.current_player + 1) % self.num_players
        return False
    
    def display_board(self):
        """Display current game status."""
        print(f"\n{'='*50}")
        print("Current Positions:")
        print(f"{'='*50}")
        for player, position in self.players.items():
            print(f"{player}: Position {position}")
    
    def start_game(self):
        """Start and run the game."""
        print(f"\n{'*'*50}")
        print("🎮 Welcome to Snake and Ladder Game! 🎮")
        print(f"{'*'*50}")
        print(f"Board size: {self.board_size}")
        print(f"Number of players: {self.num_players}")
        print(f"Players: {', '.join(self.player_names)}")
        print(f"{'*'*50}\n")
        
        game_won = False
        turn_count = 0
        
        while not game_won:
            self.display_board()
            game_won = self.play_turn()
            turn_count += 1
        
        print(f"\n{'='*50}")
        print(f"Game Over! Total turns: {turn_count}")
        print(f"{'='*50}\n")


def main():
    """Main function to run the game."""
    try:
        num_players = int(input("Enter number of players (default 2): ") or "2")
        if num_players < 1:
            num_players = 2
    except ValueError:
        num_players = 2
    
    game = SnakeLadderGame(num_players=num_players)
    game.start_game()


if __name__ == "__main__":
    main()
