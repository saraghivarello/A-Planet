from otree.api import *
import random
#import numpy as np
import ast
from itertools import zip_longest


doc = """
This application provides a webpage instructing participants how to get paid.
Examples are given for the lab and Amazon Mechanical Turk (AMT).
"""


class C(BaseConstants):
    NAME_IN_URL = 'A_Planet2'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 8
    language = "EN"
    start_time = "Asd"
    start_date = "asd"
    contact_email = "@#!@#"
   
      
    CE_BLOCKS = [[2,4,2,1,2,1,1,4,3,2],
                 [4,3,2,4,1,3,3,1,2,4],
                 [3,4,2,3,1,4,1,2,5,3],
                 [2,3,2,1,4,1,1,3,4,3],
                 [3,1,4,1,3,4,4,1,4,5],
                 [3,4,3,4,2,4,4,2,1,5],
                 [3,2,1,2,2,1,4,2,4,3],
                 [1,3,1,1,3,1,2,3,5,4],
                 [1,2,1,1,2,3,4,2,3,1],
                 [2,4,2,1,3,4,4,2,1,5],
                 [4,1,4,1,1,2,1,2,2,3],
                 [4,1,1,1,4,1,3,2,2,4],
                 [2,4,1,2,2,4,4,2,4,5],
                 [4,3,2,3,4,1,4,3,4,5],
                 [3,4,4,3,1,2,2,1,1,5],
                 [4,3,4,2,3,1,1,2,2,1],
                 [2,4,1,2,1,3,2,3,4,1],
                 [1,3,1,4,3,4,2,4,4,3],
                 [4,3,3,4,1,3,3,1,4,3],
                 [1,3,1,2,1,4,2,1,3,1],
                 [3,2,2,1,3,2,2,1,5,3],
                 [4,1,2,1,2,4,2,3,3,5],
                 [4,3,4,3,1,3,1,4,3,2],
                 [3,4,1,3,4,2,4,3,4,2],
                 [3,4,4,3,3,2,2,4,1,5],
                 [4,3,4,2,4,3,2,1,1,2],
                 [2,4,2,1,3,2,3,1,3,4],
                 [3,2,3,2,4,1,2,3,3,5],
                 [4,3,3,2,1,2,4,3,1,2],
                 [2,3,1,2,4,2,4,1,2,1],
                 [4,3,1,3,2,4,4,3,5,4],
                 [3,1,3,1,1,2,1,4,5,1],
                 [2,4,2,1,1,3,3,4,4,1],
                 [2,3,1,4,3,4,2,4,4,1],
                 [4,2,2,1,2,4,2,3,4,1],
                 [4,2,2,1,4,1,3,2,4,2],
                 [4,3,2,3,4,3,1,4,1,3],
                 [4,3,1,4,1,2,4,2,3,2],
                 [1,3,1,3,4,2,1,3,2,5],
                 [2,4,1,4,4,3,4,1,5,1],
                 [2,4,2,3,3,2,3,2,3,1],
                 [3,4,1,4,3,1,2,3,2,4],
                 [2,1,2,1,1,3,1,3,5,2],
                 [3,2,2,1,1,4,4,3,2,1],
                 [3,4,3,1,2,3,3,1,1,3],
                 [3,4,4,3,2,3,4,2,2,1],
                 [4,3,1,3,2,4,3,4,4,5],
                 [3,4,1,3,2,3,2,1,5,2],
                 [2,3,2,1,2,3,2,1,2,5],
                 [1,2,1,2,4,1,3,2,4,2],
                 [4,3,4,1,2,3,1,3,2,4],
                 [4,3,4,3,3,2,3,1,4,3],
                 [4,3,2,4,1,2,4,3,1,5],
                 [4,1,4,1,3,4,4,1,5,2],
                 [2,3,2,1,2,1,4,1,5,2],
                 [4,3,4,1,3,4,4,1,5,3],
                 [1,2,1,1,1,2,4,3,4,1],
                 [1,3,1,4,3,4,1,2,5,2],
                 [3,4,3,1,4,2,1,3,4,3],
                 [4,1,3,1,3,1,2,4,4,1],
                 [1,2,1,2,1,4,3,4,2,3],
                 [2,3,1,2,2,4,1,3,1,3],
                 [4,3,3,1,1,2,3,2,3,5],
                 [2,3,2,4,4,1,4,1,2,3]]
    

    if language=="ES":
        
        control_question = "¿Cuántos euros gastaría en este viaje?"
        control_question_choices = [[0,"0.20 EUR"],[1,"1.50 EUR"],[2,"2 EUR"],[3,"3 EUR"]]

        alternative_1 = "¿Cuál es la mejor alternativa para ti?"
        revenue_alternatives = [[1,"Presupuesto general"],
                                [2,"Transferencia igualitaria"],
                                [3,"Transferencia para los ciudadanos con bajos ingresos"],
                                [4,"Inversiones en carreteras"],
                                [5,"Inversiones en transporte público, a pie y en bicicleta"]]

        attributes_binary1 = "Precio por kilómetro en zonas urbanas, hora punta:"
        attributes_binary2 = "Precio por kilómetro en zonas urbanas, fuera de la hora punta:"
        attributes_binary3 = "Precio por kilómetro fuera de las zonas urbanas:"
        attributes_binary4 = "Precio de los vehículos eléctricos:"
        attributes_binary5 = "Uso de los ingresos:"
        binary_choice = [[0,"Sí"],[1,"No"]]
        
        question = "¿Qué tipo de politica prefiere?"
        other_policy = "Ninguna de ellas, prefiero mantener el sistema actual"
        policy_type = ["Presupuesto general",
                      "Transferencia igualitaria",
                      "Transferencia para los ciudadanos de bajos ingresos",
                      "Inversiones en carreteras",
                      "Inversiones en transporte público, a pie y en bicicleta"]
        Price_UR = ["0.10 EUR","0.20 EUR","0.40 EUR", "0.50 EUR"]
        Price_UN = ["0.10 EUR","0.20 EUR","0.30 EUR", "0.40 EUR"]
        Price_O = ["0.01 EUR","0.02 EUR","0.03 EUR", "0.05 EUR"]
        EV = ["lo mismo que los vehículos normales",
                "25 por ciento de descuento",
                "50 por ciento de descuento",
                "100 por ciento de descuento"]
        
        
    elif language=="EN":
            
        control_question = "How many euros would you spend on this trip?"
        control_question_choices = [[0,"0.20 EUR"],[1,"1.50 EUR"],[2,"2 EUR"],[3,"3 EUR"]]

        alternative_1 = "What is the best alternative for you?"
        revenue_alternatives = [[1,"General budget"],
                                [2,"Equal cash transfer"],
                                [3,"Cash transfer for low-income citizens"],
                                [4,"Investments in roads"],
                                [5,"Investments in public transport, walking and cycling"]]
        
        attributes_binary1 = "Price per km in urban areas, rush hour:"
        attributes_binary2 = "Price per km in urban areas, outside rush hour:"
        attributes_binary3 = "Price per km outside urban areas:"
        attributes_binary4 = "Price for electric vehicles:"
        attributes_binary5 = "Use of revenues:"
        binary_choice = [[0,"Yes"],[1,"No"]]

        question = "What is your preferred policy type?"
        other_policy = "None of them, keep the current system"
        policy_type = ["General budget",
                      "Equal cash transfer",
                      "Cash transfer for low-income citizens",
                      "Investments in roads",
                      "Investments in public transport, walking and cycling"]
        Price_UR = ["0.10 EUR","0.20 EUR","0.40 EUR", "0.50 EUR"]
        Price_UN = ["0.10 EUR","0.20 EUR","0.30 EUR", "0.40 EUR"]
        Price_O = ["0.01 EUR","0.02 EUR","0.03 EUR", "0.05 EUR"]
        EV = ["the same as regular vehicles",
              "25 percent discount of regular vehicles",
              "50 percent discount of regular vehicles",
              "100 percent discount of regular vehicles"]



class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    
    language = models.CharField(default="EN")
    random_block = models.IntegerField(default=None)
    random_order = models.CharField(default=None)
    
    control_question = models.IntegerField(default=None, choices=C.control_question_choices, verbose_name = C.control_question,widget=widgets.RadioSelect())

    alternative1 = models.IntegerField(default=None, choices=C.revenue_alternatives, verbose_name = C.alternative_1)
    
    policy_choice = models.IntegerField(default=None, choices=[[1,"A"],[2,"B"],[3,C.other_policy]], verbose_name = C.question, widget=widgets.RadioSelectHorizontal())

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
    
    attributes_binary_1 = models.IntegerField(default=None, choices= C.binary_choice, verbose_name = C.attributes_binary1, widget=widgets.RadioSelectHorizontal())
    attributes_binary_2 = models.IntegerField(default=None, choices= C.binary_choice, verbose_name = C.attributes_binary2, widget=widgets.RadioSelectHorizontal())
    attributes_binary_3 = models.IntegerField(default=None, choices= C.binary_choice, verbose_name = C.attributes_binary3, widget=widgets.RadioSelectHorizontal())
    attributes_binary_4 = models.IntegerField(default=None, choices= C.binary_choice, verbose_name = C.attributes_binary4, widget=widgets.RadioSelectHorizontal())
    attributes_binary_5 = models.IntegerField(default=None, choices= C.binary_choice, verbose_name = C.attributes_binary5, widget=widgets.RadioSelectHorizontal())
    

    def set_language(self, language):

        self.language = language


# FUNCTIONS


# PAGES
   
class C1(Page):
    def vars_for_template(self):
        language = C.language
        return {'language': language}

    def is_displayed(self):
        return self.subsession.round_number == 1  

class C2(Page):
    def vars_for_template(self):
        language = C.language
        return {'language': language}

    def is_displayed(self):
        return self.subsession.round_number == 1  

class C2b(Page):

    form_model = Player
    form_fields = ['control_question']

    def vars_for_template(self):
        language = C.language
        return {'language': language}

    def is_displayed(self):
        return self.subsession.round_number == 1  
    
class C2b2(Page):

    form_model = Player
    form_fields = ['control_question']

    def vars_for_template(self):
        language = C.language
        return {'language': language}

    def is_displayed(self):
        return self.subsession.round_number == 1 and (self.control_question!=3)

class C2c(Page):

    def vars_for_template(self):
        language = C.language
        return {'language': language}

    def is_displayed(self):
        return self.subsession.round_number == 1 and (self.control_question==3)
    
class C2c2(Page):

    def vars_for_template(self):
        language = C.language
        return {'language': language}

    def is_displayed(self):
        return self.subsession.round_number == 1 and (self.control_question!=3)

class C3(Page):
    form_model = Player
    form_fields = ['alternative1']

    def vars_for_template(self):
        language = C.language
        return {'language': language}

    def is_displayed(self):
        return self.subsession.round_number == 1          


class C4(Page): # Pollution treatment
    def vars_for_template(self):
        language = C.language
        return {'language': language}

    def is_displayed(self):
        return self.subsession.round_number == 1 and ((self.id_in_group+1)%5==0)

class C5(Page): # Public service treatment
    def vars_for_template(self):
        language = C.language
        return {'language': language}

    def is_displayed(self):
        return self.subsession.round_number == 1 and ((self.id_in_group+2)%5==0) 

class C6(Page): # Road pricing treatment
    def vars_for_template(self):
        language = C.language
        return {'language': language}

    def is_displayed(self):
        return self.subsession.round_number == 1 and ((self.id_in_group+3)%5==0) 
    
class C7(Page): # new treatment
    def vars_for_template(self):
        language = C.language
        return {'language': language}

    def is_displayed(self):
        return self.subsession.round_number == 1 and ((self.id_in_group)%5==0) 

    
class Choice(Page):
    form_model = Player
    form_fields = ['policy_choice']

    def vars_for_template(self):

        language = C.language

        ID = self.id_in_group
        choice_number = self.round_number
        treatment = ((ID-1)%4)

        if self.round_number == 1:

            random_order = ""
            num_blocks = len(C.CE_BLOCKS)/C.NUM_ROUNDS
            random_block = random.randint(0,num_blocks-1) 
            random_order += str(random_block)
            choice_order = [item for item in range(int(num_blocks))]
            random.shuffle(choice_order)

            for i in range(C.NUM_ROUNDS):
                random_order += str(choice_order[i])

            self.participant.vars['random_order'] = random_order
            
        random_order = self.participant.vars['random_order']
        random_block = int(random_order[0])

        first = random_block*C.NUM_ROUNDS                     # (int((ID-1)/4)%4)*8
        last = random_block*C.NUM_ROUNDS+C.NUM_ROUNDS         # (int((ID-1)/4)%4)*8 + 8

        player_choices = C.CE_BLOCKS[first:last][int(random_order[self.round_number])]

        AB = random.choice([True, False]) # ((int((ID-1)/16)%2)==0)

        if (AB):
            A = 0
            B = 1
        else:
            A = 1
            B = 0

        Price_UR = C.Price_UR
        Price_UN = C.Price_UN
        Price_O = C.Price_O
        EV = C.EV
        Revenue = C.policy_type

        Price_UR_A = player_choices[0+A]
        self.Price_UR_A = Price_UR_A

        Price_UN_A = player_choices[2+A]
        self.Price_UN_A = Price_UN_A

        Price_O_A = player_choices[4+A]
        self.Price_O_A = Price_O_A     

        EV_A = player_choices[6+A]
        self.EV_A = EV_A  

        Revenue_A = player_choices[8+A]
        self.Revenue_A = Revenue_A

        Price_UR_B = player_choices[0+B]
        self.Price_UR_B = Price_UR_B

        Price_UN_B = player_choices[2+B]
        self.Price_UN_B = Price_UN_B

        Price_O_B = player_choices[4+B]
        self.Price_O_B = Price_O_B    

        EV_B = player_choices[6+B]
        self.EV_B = EV_B  

        Revenue_B = player_choices[8+B]
        self.Revenue_B = Revenue_B
        
        self.random_order = random_order
        self.random_block = random_block
        
        show_revenue1 = ((Revenue_A == 1) or (Revenue_B == 1))
        show_revenue2 = ((Revenue_A == 2) or (Revenue_B == 2))
        show_revenue3 = ((Revenue_A == 3) or (Revenue_B == 3))
        show_revenue4 = ((Revenue_A == 4) or (Revenue_B == 4))
        show_revenue5 = ((Revenue_A == 5) or (Revenue_B == 5))

        return {'language': language, 
                'Price_UR_A': Price_UR[Price_UR_A-1], 
                'Price_UN_A': Price_UN[Price_UN_A-1],
                'Price_O_A': Price_O[Price_O_A-1],
                'EV_A': EV[EV_A-1],
                'Revenue_A': Revenue[Revenue_A-1],
                'Price_UR_B': Price_UR[Price_UR_B-1], 
                'Price_UN_B': Price_UN[Price_UN_B-1],
                'Price_O_B': Price_O[Price_O_B-1],
                'EV_B': EV[EV_B-1],
                'Revenue_B': Revenue[Revenue_B-1],
                'show_revenue1':show_revenue1,
                'show_revenue2':show_revenue2,
                'show_revenue3':show_revenue3,
                'show_revenue4':show_revenue4,
                'show_revenue5':show_revenue5,
                'treatment':treatment,
                'random_order':random_order,
                'random_block':random_block}

class C8(Page):
    form_model = Player
    form_fields = ['attributes_binary_1','attributes_binary_2','attributes_binary_3','attributes_binary_4','attributes_binary_5']
    
    def vars_for_template(self):
        language = C.language
        return {'language': language}

    def is_displayed(self):
        return self.subsession.round_number == 8

    
    

page_sequence = [C1,
                 C2,
                 C2b,
                 C2b2,
                 C2c,
                 C2c2,
                 C3,
                 C4,
                 C5,
                 C6,
                 C7,
                 Choice,
                 C8]
