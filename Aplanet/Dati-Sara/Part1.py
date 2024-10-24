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

    name_in_url = 'AAplanet'
    # if = 24, just one group
    players_per_group = None
    # total rounds of the experiment
    num_rounds = 1
    # what I give every individual
    endowment = c(1)
    # "b" in my model
    # multiplier = players_per_group // 2
    # "c" in my model
    cost_cooperating = 1

    payment_coefficient = 10
    payment_show_up_fee = 2

    timeout_pgg = 30
    timeout_fight = 45
    start_time = "12:00"
    start_date = "19/07/2022"
    start_time_1 = "17:15"
    # initial_score = players_per_group // 2
    language = "ES" # "NO", "EN", "ES"

    boolean_choices = [[1,"Yes"],[0,"No"]]

    if language == "EN":

        boolean_choices = [[1,"Yes"],[0,"No"]]

        q1_question1 = "What is the postal code of your home address?"
        q1_max = 99999

        q4_question1 = "What is your employment status?"
        q4_choices1 = [[0,"Full-time worker"],[1,"Part-time worker"],[2,"Student"],[3,"Retired"],[4, "Unemployed"], [5, "Not working for other reasons"]]

        q1_inequality = "What type of society do you think is Spain today – which diagram comes the closest?"
        inequality_choices = [[1,"A"],[2,"B"],[3,"C"],[4,"D"],[5,"E"],[6,"I do not know"]]

        q2_inequality = "What do you think Spain ought to be like – which would you prefer?"
        
        q3_inequality = "How fair do you think the wealth distribution is in your country?"
        q3_inequality_choices = [[1,"Very fair"],[2,"Fair"],[3,"Unfair"],[4,"Very unfair"],[5,"I do not know"]]

        q2_question1 = "Do you have a driver license?"
        q2_choices1 = boolean_choices

        q2_question2 = "Do you own or have access to a car?"
        q2_choices2 = [[0,"I own"],[1,"I don't own, but have access to"],[2,"I do not have access to"]]
    
        q2_question3 = "What kind of vehicle do you have access to? If you have access to multiple vehicles choose the one you use the most."
        q2_choices3 = [[0,"Gasoline"],[1,"Diesel"],[2,"Hybrid or plug-in hybrid"],[3,"Electric"]]

        q3_question1 = "Do you own or have access to a bike (electric or regular)?"
        q3_choices1 = [[0,"I own"],[1,"I don't own, but have access to"],[2,"I do not have access to"]]

        q3b_question1 = "Do you own or have access to a motorbyke?"
        q3b_choices1 = [[0,"I own"],[1,"I don't own, but have access to"],[2,"I do not have access to"]]
        q3c_question1 = "Do you own or have access to a e-scooter?"
        q3c_choices1 = [[0,"I own"],[1,"I don't own, but have access to"],[2,"I do not have access to"]]

        q6_question1 = "Where is the destination of this trip? (municipality)"
        
        q6_question2 = "What is the purpose/destination of this trip?"
        q6_choices2 = [[0,"Workplace"], 
                       [1,"Education place"],
                       [2,"Trip within my job/for job purposes"],
                       [3,"Bring/pick up children or adult"],
                       [4,"Errands or shopping"],
                       [5,"Visit family or friend"],
                       [6,"Leisure activity (cultural, sport, etc)"],
                       [7,"Other"]]
        q6b_question1 = "Please specify the purpose/destination of your trip."

        q7_question1 = "At what time of the day do you typically travel?"
        q7_choices1 = [[0,"morning"], [1,"afternoon"], [2,"evening"],[3,"night"]]
        q7_question2 = "By which mode do you travel with during this trip? If you travel with multiple modes choose the mode that takes you the longest time."
        q7_choices2 = [[0,"Private car (driver)"], 
                       [1,"Private car (passenger)"],
                       [2,"Bus"],
                       [3,"Metro, tram or light rail"],
                       [4,"Train"],
                       [5,"Walk"],
                       [6,"Bike (regular or electric)"],
                       [7,"E-scooter"],
                       [8,"Motorcycle"],
                       [9,"Ferry"],
                       [10,"Other"]]
        q7_question1_other = "Please specify the mode of your trip."
        q7_question3 = "How are the traffic conditions normally on the trip?"
        q7_choices3 = [[0,"Heavily congested"], 
                       [1,"Somewhat congested"],
                       [2,"Little or no congested"]]
        q7_question4 = "What is the approximate travel time of this trip (one way)?"
        q7_choices4 = [[0,"10-19 minutes"],
                       [1,"20-39 minutes"],
                       [2,"40-59 minutes"],
                       [3,"1-2 hours"],
                       [4,"more than 2 hours"]]
        q7_question5 = "What is the approximate cost of this trip (fuel, road tolls, parking, ticket price etc.), one way? If you are traveling by public transport and have a period ticket, please consider the average price per trip."
        q7_choices5 = [[0,"less than 10 NOK"], 
                       [1,"10-24 NOK"],
                       [2,"25-49 NOK"],
                       [3,"50-99 NOK"],
                       [4,"100-199 NOK"],
                       [5,"200 NOK or more"]]
        q7_question6 = "If you were to make this trip using a different mode of travel than your usual mode, which would be the best alternative?"
        q7_choices6 = [[0,"Private car (driver)"], 
                       [1,"Private car (passenger)"],
                       [2,"Bus"],
                       [3,"Metro, tram or light rail"],
                       [4,"Train"],
                       [5,"Walk"],
                       [6,"Bike (regular or electric)"],
                       [7,"E-scooter"],
                       [8,"Motorcycle"],
                       [9,"Ferry"],
                       [10,"I have no available alternatives"]]
        q7_question7 = "How would you rate your alternative?"
        q7_choices7 = [[0,"Almost as good as my current choice"], 
                       [1,"Somewhat worse than my current choice"],
                       [2,"Much worse than my current choice"],
                       [3,"I do not know"]]

        q7d_question1 = "Please specify the reasons of why you do not have an alternative."

        control_question = "How many NOK would you spend for this trip?"
        control_question_choices = [[0,"1,5 NOK"],[1,"15 NOK"],[2,"20 NOK"],[3,"30 NOK"]]

        revenue_alternatives = [[1,"General budget"],
                            [2,"Equal cash transfer"],
                            [3,"Cash transfer for low-income citizens"],
                            [4,"Investments in roads"],
                            [5,"Investments in public transport, walking and cycling"]]

    elif language == "ES":

        boolean_choices = [[1,"Sí"],[0,"No"]]

        q1_question1 = "¿Cuál es el código postal de su domicilio?"
        q1_max = 99999

        q4_question1 = "¿Cuál es su situación laboral?"
        q4_choices1 = [[0,"Trabajador/a a tiempo completo"],[1,"Trabajador/a a tiempo parcial"],[2,"Estudiante"],[3,"Jubilado/a"],[4, "Desempleado/a"], [5, "Otra"]]

        q1_inequality = "¿Qué tipo de sociedad cree que es España hoy en día, qué diagrama se acerca más?"
        inequality_choices = [[1,"A"],[2,"B"],[3,"C"],[4,"D"],[5,"E"],[6,"No lo sé"]]

        q2_inequality = "¿Cómo cree que debería ser España? ¿Qué diagrama prefiere?"
        
        q3_inequality = "¿Cómo de justa cree que es la distribución de la riqueza en su país?"
        q3_inequality_choices = [[1,"Muy justa"],[2,"Justa"],[3,"Injusta"],[4,"Muy injusta"],[5,"No lo sé"]]        

        q2_question1 = "¿Tiene permiso de conducir?"
        q2_choices1 = boolean_choices

        q2_question2 = "¿Posee o tiene acceso a un coche?"
        q2_choices2 = [[0,"Poseo"],[1,"No poseo, pero tengo acceso a"],[2,"No tengo acceso a"]]

        q2_question3 = "¿A qué tipo de vehículo tiene acceso? Si tiene acceso a varios vehículos, elige el que más utilice."
        q2_choices3 = [[0,"Gasolina"],[1,"Diésel"],[2,"Híbrido o híbrido enchufable"],[3,"Eléctrico"]]

        q3_question1 = "¿Posee o tiene acceso a una bicicleta (eléctrica o normal)?"
        q3_choices1 = [[0,"Poseo"],[1,"No poseo, pero tengo acceso a"],[2,"No tengo acceso a"]]     
        q3b_question1 = "¿Posee o tiene acceso a una motocicleta?"
        q3b_choices1 = [[0,"Poseo"],[1,"No poseo, pero tengo acceso a"],[2,"No tengo acceso a"]]     
        q3c_question1 = "¿Tienes o tienes acceso a un patinete eléctrico?"
        q3c_choices1 = [[0,"Poseo"],[1,"No poseo, pero tengo acceso a"],[2,"No tengo acceso a"]]     
    
        q6_question1 = "¿Cuál es el destino de este viaje? (municipio)"
        
        q6_question2 = "¿Cuál es el objetivo/destino de este viaje?"
        q6_choices2 = [[0,"Lugar de trabajo"], 
                       [1,"Lugar de educación"],
                       [2,"Viaje dentro de mi trabajo/por motivos laborales"],
                       [3,"Traer/recoger niños o adultos"],
                       [4,"Recados o compras"],
                       [5,"Visitar a la familia o a un amigo"],
                       [6,"Actividad de ocio (cultural, deportiva, etc.)"],
                       [7,"Otro"]]
        q6b_question1 = "Especifique el propósito/destino de su viaje."

        q7_question1 = "¿A qué hora del día suele viajar?"
        q7_choices1 = [[0,"por la mañana"], [1,"a media tarde"], [2,"por la tarde"],[3,"por la noche"]]
        q7_question2 = "¿Con qué modo de transporte viaja durante este viaje? Si viaja con varios modos, elija el modo que le lleve más tiempo."
        q7_choices2 = [[0,"Coche privado (conductor)"], 
                       [1,"Coche privado (pasajero)"],
                       [2,"Autobús"],
                       [3,"Metro, metro ligero o tranvía"],
                       [4,"Tren (Cercanías o larga distancia)"],
                       [5,"Caminando"],
                       [6,"Bicicleta (normal o eléctrica)"],
                       [7,"Patinete"],
                       [8,"Motocicleta"],
                       [9,"Ferry"],
                       [10,"Otro"]]
        q7_question1_other = "Por favor, especifique el modo de su viaje."
        q7_question3 = "¿Cómo son normalmente las condiciones de su viaje?"
        q7_choices3 = [[0,"Muy congestionado"], 
                       [1,"Algo congestionado"],
                       [2,"Poca o ninguna congestión"]]
        q7_question4 = "¿Cuál es la duración aproximada de este viaje (solo ida)?"
        q7_choices4 = [[0,"10-19 minutos"],
                       [1,"20-39 minutos"],
                       [2,"40-59 minutos"],
                       [3,"1-2 horas"],
                       [4,"más de 2 horas"]]
        q7_question5 = "¿Cuál es el coste aproximado de este viaje (combustible, peajes, aparcamiento, precio del billete, etc.), por trayecto? Si viaja en transporte público y tiene un abono, tenga en cuenta el precio medio por trayecto."
        q7_choices5 = [[0,"menos de 1 EUR"], 
                       [1,"1-2.50 EUR"],
                       [2,"2.50-4.99 EUR"],
                       [3,"5-9.99 EUR"],
                       [4,"10-19.99 EUR"],
                       [5,"20 EUR o más"]]
        q7_question6 = "Si tuviera que realizar este viaje utilizando un modo de transporte diferente al habitual, ¿cuál sería la mejor alternativa?"
        q7_choices6 = [[0,"Coche privado (conductor)"], 
                       [1,"Coche privado (pasajero)"],
                       [2,"Autobús"],
                       [3,"Metro, metro ligero o tranvía"],
                       [4,"Tren (Cercanías o larga distancia)"],
                       [5,"Caminando"],
                       [6,"Bicicleta (normal o eléctrica)"],
                       [7,"Patinete"],
                       [8,"Motocicleta"],
                       [9,"Ferry"],
                       [10,"Otro"],
                       [11,"No tengo alternativas disponibles"]]
        q7_question7 = "¿Cómo calificaría su alternativa?"
        q7_choices7 = [[0,"Casi tan buena como mi elección actual"], 
                       [1,"Algo peor que mi elección actual"],
                       [2,"Mucho peor que mi elección actual"],
                       [3,"No lo sé"]]

        q7d_question1 = "Por favor, especifique las razones por las que no tiene una alternativa."

        control_question = "¿Cuántos euros gastaría en este viaje?"
        control_question_choices = [[0,"0.20 EUR"],[1,"1.50 EUR"],[2,"2 EUR"],[3,"3 EUR"]]

        revenue_alternatives = [[1,"Presupuesto general"],
                            [2,"Transferencia igualitaria"],
                            [3,"Transferencia para los ciudadanos con bajos ingresos"],
                            [4,"Inversiones en carreteras"],
                            [5,"Inversiones en transporte público, a pie y en bicicleta"]]        

    ##### EXTRA QUESTIONS (NOT USED ANYMORE)

    q5_question1 = "Did you change your travel behaviour before/after covid?"
    q5_choices1 = boolean_choices

    contact_email = "ibsen.gisc@gmail.com"

    max_auto_decisions = 4

class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass

class Player(BasePlayer):

    language = models.CharField(default="ES")

    ############################################################################################################################################################
    #   INEQUALITY QUESTIONS
    ############################################################################################################################################################

    inequality_perception = models.IntegerField(default=None, verbose_name=Constants.q1_inequality,choices=Constants.inequality_choices,widget=widgets.RadioSelectHorizontal())
    inequality_wish = models.IntegerField(default=None, verbose_name=Constants.q2_inequality,choices=Constants.inequality_choices,widget=widgets.RadioSelectHorizontal())
    income_distribution= models.IntegerField(default=None, verbose_name=Constants.q3_inequality,choices=Constants.q3_inequality_choices,widget=widgets.RadioSelect())

    ############################################################################################################################################################
    #   QUESTIONS 1
    ############################################################################################################################################################

    postal_code = models.IntegerField(default=None, verbose_name=Constants.q1_question1,min=1,max=Constants.q1_max)
    # city = models.CharField(default=None, verbose_name=Constants.q1_question2)

    ############################################################################################################################################################
    #   QUESTIONS 2 & 2b
    ############################################################################################################################################################

    driving_license = models.BooleanField(default=None, choices=Constants.q2_choices1, verbose_name = Constants.q2_question1, widget=widgets.RadioSelectHorizontal())
    access_to_car = models.IntegerField(default=None, choices=Constants.q2_choices2, verbose_name = Constants.q2_question2, widget=widgets.RadioSelect())
    car_type = models.IntegerField(default=None, choices=Constants.q2_choices3, verbose_name = Constants.q2_question3, widget=widgets.RadioSelect())

    ############################################################################################################################################################
    #   QUESTIONS 3 & 3b & 3c
    ############################################################################################################################################################

    access_to_bike = models.IntegerField(default=None, choices=Constants.q3_choices1, verbose_name = Constants.q3_question1, widget=widgets.RadioSelect())
    access_to_motorbyke = models.IntegerField(default=None, choices=Constants.q3b_choices1, verbose_name = Constants.q3b_question1, widget=widgets.RadioSelect())
    access_to_scooter = models.IntegerField(default=None, choices=Constants.q3c_choices1, verbose_name = Constants.q3c_question1, widget=widgets.RadioSelect())

    ############################################################################################################################################################
    #   QUESTIONS 4
    ############################################################################################################################################################

    employ_status = models.IntegerField(default=None, choices=Constants.q4_choices1, verbose_name = Constants.q4_question1, widget=widgets.RadioSelect())

    ############################################################################################################################################################
    #   QUESTIONS 5
    ############################################################################################################################################################

    travel_behavior = models.BooleanField(default=None, choices=Constants.q5_choices1, verbose_name = Constants.q5_question1, widget=widgets.RadioSelectHorizontal())

    ############################################################################################################################################################
    #   QUESTIONS 6 & 6b
    ############################################################################################################################################################

    trip_destination = models.CharField(default=None, verbose_name = Constants.q6_question1)
    trip_purpose = models.IntegerField(default=None, choices=Constants.q6_choices2,verbose_name=Constants.q6_question2,widget=widgets.RadioSelect())

    trip_other = models.CharField(default=None, verbose_name = Constants.q6b_question1)

    ############################################################################################################################################################
    #   QUESTIONS 7
    ############################################################################################################################################################

    trip_moment = models.IntegerField(default=None, choices=Constants.q7_choices1, verbose_name = Constants.q7_question1,widget=widgets.RadioSelect())
    trip_mode = models.IntegerField(default=None, choices=Constants.q7_choices2,verbose_name=Constants.q7_question2,widget=widgets.RadioSelect())
    mode_other = models.CharField(default=None, verbose_name = Constants.q7_question1_other)
    trip_traffic = models.IntegerField(default=None, choices=Constants.q7_choices3, verbose_name = Constants.q7_question3,widget=widgets.RadioSelect())
    trip_time = models.IntegerField(default=None, choices=Constants.q7_choices4, verbose_name = Constants.q7_question4,widget=widgets.RadioSelect())
    trip_cost = models.IntegerField(default=None, choices=Constants.q7_choices5, verbose_name = Constants.q7_question5,widget=widgets.RadioSelect())
    trip_alternative_mode = models.IntegerField(default=None, choices=Constants.q7_choices6, verbose_name = Constants.q7_question6,widget=widgets.RadioSelect())
    trip_alternative_rate = models.IntegerField(default=None, choices=Constants.q7_choices7, verbose_name = Constants.q7_question7,widget=widgets.RadioSelect())
    trip_alternative_justification = models.CharField(default=None, verbose_name = Constants.q7d_question1)

    control_question = models.IntegerField(default=None, choices=Constants.control_question_choices, verbose_name = Constants.control_question,widget=widgets.RadioSelect())

    alternative1 = models.IntegerField(default=None, choices=Constants.revenue_alternatives, verbose_name = "")
    alternative2 = models.IntegerField(default=None, choices=Constants.revenue_alternatives, verbose_name = "")
    alternative3 = models.IntegerField(default=None, choices=Constants.revenue_alternatives, verbose_name = "")
    alternative4 = models.IntegerField(default=None, choices=Constants.revenue_alternatives, verbose_name = "")
    alternative5 = models.IntegerField(default=None, choices=Constants.revenue_alternatives, verbose_name = "")

    fighting = models.BooleanField(default=None, widget=widgets.RadioSelectHorizontal(), verbose_name="Escoja su decisión y pulse Siguiente", choices=((True, "Pelear"), (False, "No pelear")))

    #   rank = models.PositiveIntegerField(default=int(Constants.players_per_group/2))

    automatic_decision = models.BooleanField(default=0)
    num_automatic_decisions = models.IntegerField(default=0)

    total_payoff = models.FloatField(default=0)
    pgg_payoff = models.FloatField(default=0)
    fight_payoff = models.FloatField(default=0)
    last_payoff = models.FloatField(default=0)

    timeout_commit = models.IntegerField(default=0)
    timeout_pgg = models.IntegerField(default=0)
    timeout_choose = models.IntegerField(default=0)
    timeout_fight = models.IntegerField(default=0)

    opponent_id = models.IntegerField(default=0)
    was_a_fight = models.BooleanField(default=False)
    fights_won = models.IntegerField(default=0)
    last_fight_result = models.BooleanField(default=False)

    paypal_account = models.CharField()
    comments = models.TextField(blank=True)

    def set_language(self, language):

        self.language = language


class Link(BaseLink):
    pass
