class Player:
    def __init__(self, name):
        self.name = name
        self.id = -1

    def reveal_card(self, cards):
        """Reveal one of the available cards."""
        return random.choice(list(cards))

    def make_move(self, game):
        """To be overridden by subclasses to make a move."""
        pass
