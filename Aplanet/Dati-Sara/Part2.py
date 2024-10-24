from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer, BaseLink,
    Currency as c, currency_range
)
import random
import ast
from itertools import zip_longest

author = 'Alberto Antonioni'

doc = """
A-planet experiment

Email: alberto.antonioni@uc3m.es
"""

class Constants(BaseConstants):
    """ Constants and variables in the model """

    name_in_url = 'CE2'

    players_per_group = None

    # total rounds of the experiment
    num_rounds = 6

    payment_coefficient = 10
    payment_show_up_fee = 2

    # OLD BLOCKS (December 2021)

#    CE_BLOCKS = [[1,1,1,1,1,1,3,4,3,3],
#                [3,3,3,3,3,3,4,3,3,1],
#                [2,4,2,4,2,4,1,3,4,2],
#                [2,3,2,2,2,4,2,2,1,5],
#                [4,3,3,3,3,2,2,4,2,2],
#                [1,4,1,3,2,4,2,2,3,4],
#                [2,2,2,2,2,2,2,2,4,4],
#                [3,3,3,3,3,3,1,2,1,3],
#                [1,3,1,3,1,3,4,3,5,5],
#                [2,4,1,1,1,3,3,4,3,1],
#                [4,3,3,3,2,4,2,3,4,4],
#                [3,2,3,1,3,2,1,3,2,2],
#                [1,1,1,1,1,1,4,1,1,3],
#                [4,4,4,4,4,4,1,4,5,4],
#                [2,3,2,3,2,3,3,3,5,1],
#                [2,3,1,1,4,1,3,4,3,4],
#                [4,3,3,3,1,3,3,2,3,2],
#                [2,4,2,4,4,1,1,4,4,3],
#                [2,2,2,2,2,2,3,2,5,2],
#                [4,4,4,4,4,4,3,3,3,2],
#                [1,4,1,4,1,4,2,3,5,3],
#                [2,4,2,2,3,2,4,4,4,3],
#                [4,3,3,3,4,1,1,1,1,5],
#                [4,2,4,2,1,3,1,2,1,1]]

    CE_BLOCKS = [[1,1,1,1,1,1,3,4,5,3],
                [3,3,3,3,3,3,4,3,5,1],
                [2,4,2,4,2,4,1,3,4,2],
                [2,3,2,2,2,4,2,2,3,5],
                [4,3,3,3,3,2,2,4,4,2],
                [1,4,1,3,2,4,2,2,5,4],
                [2,2,2,2,2,2,2,2,1,4],
                [3,3,3,3,3,3,1,2,2,3],
                [1,3,1,3,1,3,4,3,2,5],
                [2,4,1,1,1,3,3,4,2,1],
                [4,3,3,3,2,4,2,3,5,4],
                [3,2,3,1,3,2,1,3,2,2],
                [1,1,1,1,1,1,4,1,2,3],
                [4,4,4,4,4,4,1,4,2,4],
                [2,3,2,3,2,3,3,3,4,1],
                [2,3,1,1,4,1,3,4,3,4],
                [4,3,3,3,1,3,3,2,4,2],
                [2,4,2,4,4,1,1,4,2,3],
                [2,2,2,2,2,2,3,2,4,2],
                [4,4,4,4,4,4,3,3,5,2],
                [1,4,1,4,1,4,2,3,5,3],
                [2,4,2,2,3,2,4,4,1,3],
                [4,3,3,3,4,1,1,1,1,5],
                [4,2,4,2,1,3,1,2,3,1]]       

    language = "ES" # "NO", "EN", "ES"

    policy_type_EN = ["General budget",
                    "Equal cash transfer",
                    "Cash transfer for low-income citizens",
                    "Investments in roads",
                    "Investments in public transport, walking and cycling"]

    policy_type_ES = ["Presupuesto general",
                    "Transferencia igualitaria",
                    "Transferencia para los ciudadanos de bajos ingresos",
                    "Inversiones en carreteras",
                    "Inversiones en transporte público, a pie y en bicicleta"]                    

    if language=="EN":

        question = "What is your preferred policy type?"
        other_policy = "None of them, keep the current system"
        policy_type = policy_type_EN
        Price_UR = ["1 NOK","2 NOK","4 NOK", "5 NOK"]
        Price_UN = ["1 NOK","2 NOK","3 NOK", "4 NOK"]
        Price_O = ["0.1 NOK","0.2 NOK","0.3 NOK", "0.5 NOK"]
        EV = ["the same as regular vehicles",
                "25 percent discount of regular vehicles",
                "50 percent discount of regular vehicles",
                "100 percent discount of regular vehicles"]

    elif language=="ES":
        question = "¿Qué tipo de politica prefiere?"
        other_policy = "Ninguna de ellas, prefiero mantener el sistema actual"
        policy_type = policy_type_ES
        Price_UR = ["0.10 EUR","0.20 EUR","0.40 EUR", "0.50 EUR"]
        Price_UN = ["0.10 EUR","0.20 EUR","0.30 EUR", "0.40 EUR"]
        Price_O = ["0.01 EUR","0.02 EUR","0.03 EUR", "0.05 EUR"]
        EV = ["lo mismo que los vehículos normales",
                "25 por ciento de descuento",
                "50 por ciento de descuento",
                "100 por ciento de descuento"]

class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass

class Player(BasePlayer):

    language = models.CharField(default="ES") 

    policy_choice = models.IntegerField(default=None, choices=[[1,"A"],[2,"B"],[3,Constants.other_policy]], verbose_name = Constants.question, widget=widgets.RadioSelectHorizontal())

    Price_UR_A = models.IntegerField(default=None)
    Price_UN_A = models.IntegerField(default=None)
    Price_O_A = models.IntegerField(default=None)
    EV_A = models.IntegerField(default=None)
    Revenue_A = models.IntegerField(default=None)

    Price_UR_B = models.IntegerField(default=None)
    Price_UN_B = models.IntegerField(default=None)
    Price_O_B = models.IntegerField(default=None)
    EV_B = models.IntegerField(default=None)
    Revenue_B = models.IntegerField(default=None)

    def set_language(self, language):

        self.language = language


class Link(BaseLink):
    pass
