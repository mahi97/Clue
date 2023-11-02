from agents.basePlayer import Player

class HumanPlayer(Player):
    def make_move(self, game):
        """Get input from the human player for their move."""
        move_type = input(f'{self.name}, your move (ask/accuse): ').strip()
        if move_type == 'ask':
            suspect = input('Ask about suspect: ')
            weapon = input('Ask about weapon: ')
            room = input('Ask about room: ')
            return ['ask', suspect, weapon, room]
        elif move_type == 'accuse':
            suspect = input('Accuse suspect: ')
            weapon = input('Accuse weapon: ')
            room = input('Accuse room: ')
            return ['accuse', {suspect, weapon, room}]

