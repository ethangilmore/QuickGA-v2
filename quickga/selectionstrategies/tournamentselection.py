import random

from .selectionstrategy import SelectionStrategy

class TournamentSelection():

    def __init__(self, tournament_size, p=.9):
        self.tournament_size = tournament_size
        self.p = p

    def select(self, population):
        tournament = random.sample(population.organisms, self.tournament_size)
        return random.choices(tournament, weights=[self.p * (1-self.p)**i for i in range(self.tournament_size)])[0]
