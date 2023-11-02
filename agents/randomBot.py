from agents.basePlayer import Player

class RandomBot(Player):
    def make_move(self, game):
        """Make a random move."""
        if sum(game.player_deterministic_knowledge[self.name].sum(axis=0) == -game.n_players) == 3:
            card_indices = np.where(game.player_deterministic_knowledge[self.name].sum(axis=0) == -game.n_players)[0]
            return ['accuse', {game.all_cards[card_index] for card_index in card_indices}]
        return ['ask', random.choice(game.suspects), random.choice(game.weapons), random.choice(game.rooms)]