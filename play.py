from clue import *
from agents import *

def play_game(n_players=6, bot_type=RandomBot):
    players = []
    for i in range(n_players):
        player = bot_type(f"Bot_{i}")
        player.id = i
        players.append(player)
    game = Clue(players=players)
    
    game.deal_cards()
    
    while not game.game_over():
        current_player = game.players[game.current_player]
        move = current_player.make_move(game)
        game.update_game_state(current_player, move)
        game.current_player = (game.current_player + 1) % game.n_players
        game.turn += 1
        # game.heatmap()
    if game.solution is None:
        print(f"The winner is {game.winner.name}! at Turn {game.turn}")
    else:
        print("No one could solve the mystery!")

if __name__ == "__main__":
    play_game(n_players=6, bot_type=RandomBot) 