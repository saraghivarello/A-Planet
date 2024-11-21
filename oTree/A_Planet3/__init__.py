from otree.api import *



doc = """
This application provides a webpage instructing participants how to get paid.
Examples are given for the lab and Amazon Mechanical Turk (AMT).
"""


class C(BaseConstants):
    NAME_IN_URL = 'A_Planet3'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 4
    players_per_group = None
    language = "EN"
    
    vec = [[1, 2, 3, 4],
           [1, 2, 4, 3],
           [1, 3, 2, 4],
           [1, 3, 4, 2],
           [1, 4, 2, 3],
           [1, 4, 3, 2],
           [2, 1, 3, 4],
           [2, 1, 4, 3],
           [2, 3, 1, 4],
           [2, 3, 4, 1],
           [2, 4, 1, 3],
           [2, 4, 3, 1],
           [3, 1, 2, 4],
           [3, 1, 4, 2],
           [3, 2, 1, 4],
           [3, 2, 4, 1],
           [3, 4, 1, 2],
           [3, 4, 2, 1],
           [4, 1, 2, 3],
           [4, 1, 3, 2],
           [4, 2, 1, 3],
           [4, 2, 3, 1],
           [4, 3, 1, 2],
           [4, 3, 2, 1]]
    
    answers_percentage = [[1,"0%"],
                          [2,"10%"],
                          [3,"20%"],
                          [4,"30%"],
                          [5,"40%"],
                          [6,"50%"],
                          [7,"60%"],
                          [8,"70%"],
                          [9,"80%"],
                          [10,"90%"],
                          [11,"100%"]]

    if language == "EN":

        question_EE = "What share (in %) of other participants in the survey do you think have chosen one of the transport modes in A for their daily trip?"
        question_PNB= "In your opinion, what should the ideal percentage of people using transport modes in A for their daily trip be?"
        question_NE = "What percentage do you think other participants typically answered in the previous question?"

        question_private = "Considering the last year, how often (in %) did you use your chosen transport mode for your daily trip?"

        question_HH = "Suppose that 80% of the other participants use the car on their daily trip and typically  participants think that 80% should use the car. How often (in %) would you use the car in this scenario?"
        question_HL = "Suppose that 80% of the other participants use the car on their daily trip but typically participants think that 20% should use the car. How often (in %) would you use the car in this scenario?"
        question_LH = "Suppose that 20% of the other participants use the car on their daily trip but typically participants think that 80% should use the car. How often (in %) would you use the car in this scenario?"
        question_LL = "Suppose that 20% of the other participants use the car on their daily trip and typically  participants think that 20% should use the car. How often (in %) would you use the car in this scenario?"

        question_year_born = "Which year were you born?"
        question_gender = "How do you identify as?"
        answers_gender = [[0,"woman"],[1,"man"],[2,"other"],[3,"prefer not to say"]]

        question_education = "What is your highest level of education?"
        answers_education = [[0,"elementary school"],[1,"high school"],[2,"university (less than 4 years)"],[3,"university (more than 4 years)"]]

        question_income = "What is your income per year?"
        answers_income = [[0,"less than 10k EUR"],[1,"10k-20k EUR"],[2,"20k-30k EUR"],[3,"30k-40k EUR"],[4,"more than 40k EUR"],[5,"prefer not to say"]]

        question_family = "How many people does your household have including you?"
        question_children = "How many children under the age of 15 live with you?"

        question_trust_parlament = "Parlament:"
        question_trust_municipality = "Municipal council:"
        question_trust_county = "County council:"
        question_trust_government = "Government:"
        question_trust_politicians = "National politicians:"
        question_trust_parties = "Political parties:"

        question_vote = "Which political party you voted for in the last election?"
        answers_vote = [[0,"PSOE"],
                        [1,"Partido Popular"],
                        [2,"Vox"],
                        [3,"Unidas Podemos"],
                        [4,"ERC-Cat"],
                        [5,"Ciudadanos"],
                        [6,"JxCat"],
                        [7,"PNV"],
                        [8,"EHB"],
                        [9,"MP-EQUO"],
                        [10,"BNG"],
                        [11,"Compromís"],
                        [12,"Other party"],
                        [13,"I prefer not to answer"]]

        answers_trust = [[1,"1"],
                         [2,"2"],
                         [3,"3"],
                         [4,"4"],
                         [5,"5"],
                         [6,"6"],
                         [7,"7"],
                         [8,"I prefer not to answer"],
                         [9,"I do not know"]]

        question_air_pollution = "Air pollution derived by cars is one of the major causes of premature death in Europe:"
        question_road_pricing = "The introduction of policies such as road pricing will alleviate congestion problems:"
        question_revenues = "Revenues collected through taxes are used to create a well-functioning welfare state and society:"
        question_tax = "Tax revenues should be used to help those who are more in need:"
        question_tax_lev = "I think the overall tax level is too high:"
        
        question_effect_rp = "How do you think road pricing will affect you, from 1 (negative effect) to 7 (positive effect)?"
        question_effect_rp_others = "How do you think the road pricing tax will affect low-income citizens, from 1 (negative effect) to 7 (positive effect)?"

    elif language == "ES":

        question_EE = "1) ¿Qué proporción (en %) de los demás participantes en la encuesta cree que han elegido uno de los modos de transporte del tipo A para su viaje diario?"
        question_PNB= "2) En su opinión, ¿cuál debería ser el porcentaje ideal de personas que utilizan los modos de transporte del tipo A para sus desplazamientos diarios?"
        question_NE = "3) ¿Qué porcentaje cree que suelen responder otros participantes en la pregunta anterior?"

        question_private = "Teniendo en cuenta el último año, ¿con qué frecuencia (en %) utilizó el modo de transporte que nos ha dicho para su viaje diario?"

        question_HH = "Supongamos que el 80% de los demás participantes utilizan el coche en sus desplazamientos diarios y, por lo general, los participantes piensan que el 80% debería utilizar el coche. ¿Con qué frecuencia (en %) utilizaría la opción A en esta situación?"
        question_HL = "Supongamos que el 80% de los demás participantes utilizan el coche en sus desplazamientos diarios, pero por lo general los participantes piensan que el 20% debería utilizar el coche. ¿Con qué frecuencia (en %) utilizaría la opción A en esta situación?"
        question_LH = "Supongamos que el 20% de los demás participantes utilizan el coche en sus desplazamientos diarios, pero por lo general los participantes piensan que el 80% debería utilizar el coche. ¿Con qué frecuencia (en %) utilizaría la opción A en esta situación?"
        question_LL = "Supongamos que el 20% de los demás participantes utilizan el coche en sus desplazamientos diarios y, por lo general, los participantes piensan que el 20% debería utilizar el coche. ¿Con qué frecuencia (en %) utilizaría la opción A en esta situación?"

        question_year_born = "¿En qué año nació?"
        question_gender = "¿Cómo se identifica usted?"
        answers_gender = [[0,"mujer"],[1,"hombre"],[2,"otro"],[3,"prefiero no responder"]]

        question_education = "¿Cuál es su nivel de estudios más alto?"
        answers_education = [[0,"escuela primaria"],[1,"escuela secundaria"],[2,"universidad (menos de 4 años)"],[3,"universidad (más de 4 años)"]]

        question_income = "¿Cuáles son sus ingresos anuales?"
        answers_income = [[0,"menos de 10.000 EUR"],[1,"10.000-20.000 EUR"],[2,"20.000-30.000 EUR"],[3,"30.000-40.000 EUR"],[4,"más de 40.000 EUR"],[5,"prefiero no responder"]]

        question_family = "¿Cuántas personas viven en su casa, incluido usted?"
        question_children = "¿Cuántos hijos menores de 15 años viven con usted?"

        question_trust_parlament = "Parlamento:"
        question_trust_municipality = "Ayuntamiento:"
        question_trust_county = "Gobierno autonómico:"
        question_trust_government = "Gobierno central:"
        question_trust_politicians = "Líderes políticos:"
        question_trust_parties = "Partidos políticos:"

        question_vote = "¿A qué partido político votó en las últimas elecciones?"
        answers_vote = [[0,"PSOE"],
                        [1,"Partido Popular"],
                        [2,"Vox"],
                        [3,"Unidas Podemos"],
                        [4,"ERC-Cat"],
                        [5,"Ciudadanos"],
                        [6,"JxCat"],
                        [7,"PNV"],
                        [8,"EHB"],
                        [9,"MP-EQUO"],
                        [10,"BNG"],
                        [11,"Compromís"],
                        [12,"otro partido"],
                        [13,"prefiero no responder"]]

        answers_trust = [[1,"1"],
                         [2,"2"],
                         [3,"3"],
                         [4,"4"],
                         [5,"5"],
                         [6,"6"],
                         [7,"7"],
                         [8,"prefiero no responder"],
                         [9,"no lo sé"]]
              

        question_air_pollution = "La contaminación atmosférica derivada de los automóviles es una de las principales causas de muerte prematura en Europa:"
        question_road_pricing = "La introducción de políticas como la tarificación de las carreteras aliviará los problemas de congestión:"
        question_revenues = "Los ingresos recaudados a través de los impuestos se utilizan para crear un estado de bienestar y una sociedad que funcionen bien:"
        question_tax = "Los ingresos fiscales deben utilizarse para ayudar a los más necesitados:"
        question_tax_lev = "Creo que el nivel general de impuestos es demasiado alto:"
        question_effect_rp = "¿Cómo cree que le afectará la tarificación de las carreteras, de 1 (efecto negativo) a 7 (efecto positivo)?"
        question_effect_rp_others = "¿Cómo cree que el impuesto sobre la tarificación vial afectará a los ciudadanos con bajos ingresos, de 1 (efecto negativo) a 7 (efecto positivo)?"


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    SN_car_A = models.BooleanField(default=None)

    EE = models.IntegerField(default=None, verbose_name = C.question_EE,choices = C.answers_percentage,widget=widgets.RadioSelectHorizontal())
    PNB= models.IntegerField(default=None, verbose_name = C.question_PNB,choices = C.answers_percentage,widget=widgets.RadioSelectHorizontal())
    NE = models.IntegerField(default=None, verbose_name = C.question_NE,choices = C.answers_percentage,widget=widgets.RadioSelectHorizontal())

    my_trip = models.IntegerField(default=None, verbose_name = C.question_private,choices = C.answers_percentage,widget=widgets.RadioSelectHorizontal())
    
    HH = models.IntegerField(default=None, verbose_name = C.question_HH,choices = C.answers_percentage,widget=widgets.RadioSelectHorizontal())
    HL = models.IntegerField(default=None, verbose_name = C.question_HL,choices = C.answers_percentage,widget=widgets.RadioSelectHorizontal())
    LH = models.IntegerField(default=None, verbose_name = C.question_LH,choices = C.answers_percentage,widget=widgets.RadioSelectHorizontal())
    LL = models.IntegerField(default=None, verbose_name = C.question_LL,choices = C.answers_percentage,widget=widgets.RadioSelectHorizontal())

    year_born = models.IntegerField(default=None, verbose_name=C.question_year_born, choices = range(1920,2004))
    gender = models.IntegerField(default=None, verbose_name=C.question_gender, choices = C.answers_gender,widget=widgets.RadioSelectHorizontal())
    education = models.IntegerField(default=None, verbose_name=C.question_education, choices = C.answers_education,widget=widgets.RadioSelect())
    income = models.IntegerField(default=None, verbose_name=C.question_income, choices = C.answers_income,widget=widgets.RadioSelect())
    family = models.IntegerField(default=None, verbose_name=C.question_family, choices = range(1,9),widget=widgets.RadioSelectHorizontal())
    children = models.IntegerField(default=None, verbose_name=C.question_children, choices = range(0,5),widget=widgets.RadioSelectHorizontal())

    trust_parlament = models.IntegerField(default=None, verbose_name=C.question_trust_parlament,choices = C.answers_trust,widget=widgets.RadioSelectHorizontal())
    trust_county = models.IntegerField(default=None, verbose_name=C.question_trust_county,choices = C.answers_trust,widget=widgets.RadioSelectHorizontal())
    trust_municipality = models.IntegerField(default=None, verbose_name=C.question_trust_municipality,choices = C.answers_trust,widget=widgets.RadioSelectHorizontal())
    trust_government = models.IntegerField(default=None, verbose_name=C.question_trust_government,choices = C.answers_trust,widget=widgets.RadioSelectHorizontal())
    trust_politicians = models.IntegerField(default=None, verbose_name=C.question_trust_politicians,choices = C.answers_trust,widget=widgets.RadioSelectHorizontal())
    trust_parties = models.IntegerField(default=None, verbose_name=C.question_trust_parties,choices = C.answers_trust,widget=widgets.RadioSelectHorizontal())

    vote = models.IntegerField(default=None, verbose_name = C.question_vote, choices = C.answers_vote,widget=widgets.RadioSelect())

    air_pollution = models.IntegerField(default=None, verbose_name = C.question_air_pollution,choices = C.answers_trust,widget=widgets.RadioSelectHorizontal())
    road_pricing = models.IntegerField(default=None, verbose_name = C.question_road_pricing,choices = C.answers_trust,widget=widgets.RadioSelectHorizontal())
    revenues = models.IntegerField(default=None, verbose_name = C.question_revenues,choices = C.answers_trust,widget=widgets.RadioSelectHorizontal())
    tax = models.IntegerField(default=None, verbose_name = C.question_tax,choices = C.answers_trust,widget=widgets.RadioSelectHorizontal())
    tax_level = models.IntegerField(default=None, verbose_name = C.question_tax_lev,choices = C.answers_trust,widget=widgets.RadioSelectHorizontal())
    
    effect_rp = models.IntegerField(default=None, verbose_name = C.question_effect_rp,choices = C.answers_trust,widget=widgets.RadioSelectHorizontal())
    effect_rp_others = models.IntegerField(default=None, verbose_name = C.question_effect_rp_others,choices = C.answers_trust,widget=widgets.RadioSelectHorizontal())

    paypal_account = models.CharField()
    comments = models.TextField()


# FUNCTIONS



# PAGES
class A1(Page):

    form_model = Player
    form_fields = ['EE','PNB','NE']

    def vars_for_template(self):
        trip_purpose = self.participant.vars['trip_purpose']
        trip_mode = self.participant.vars['trip_mode']
        language = C.language
        SN_car_A = ((int((self.id_in_group-1)/32)%2)==0)
        self.SN_car_A = SN_car_A

        return {'trip_purpose': trip_purpose,
                'trip_mode': trip_mode,
                'language': language,
                'SN_car_A': SN_car_A}
    
    def is_displayed(self):
        return self.subsession.round_number == 1
    

class A2(Page):

    form_model = Player
    form_fields = ['my_trip']

    def vars_for_template(self):
        trip_purpose = self.participant.vars['trip_purpose']
        trip_mode = self.participant.vars['trip_mode']
        language = C.language
        SN_car_A = ((int((self.id_in_group-1)/32)%2)==0)

        return {'trip_purpose': trip_purpose,
                'trip_mode': trip_mode,
                'language': language,
                'SN_car_A': SN_car_A}
    
    def is_displayed(self):
        return self.subsession.round_number == 1
    

class A3a(Page):

    form_model = Player
    form_fields = ['HH']

    def vars_for_template(self):
        trip_purpose = self.participant.vars['trip_purpose']
        trip_mode = self.participant.vars['trip_mode']
        language = C.language
        SN_car_A = ((int((self.id_in_group-1)/32)%2)==0)
        access_to_car = (self.participant.vars['access_to_car']!=2)
        
        return {'trip_purpose': trip_purpose,
                'trip_mode': trip_mode,
                'language': language,
                'SN_car_A': SN_car_A,
                'access_to_car': access_to_car}
    
    def is_displayed(self):
        return C.vec[int((self.id_in_group-1)%24)][self.subsession.round_number-1] == 1
    

class A3b(Page):

    form_model = Player
    form_fields = ['HL']

    def vars_for_template(self):
        trip_purpose = self.participant.vars['trip_purpose']
        trip_mode = self.participant.vars['trip_mode']
        language = C.language
        SN_car_A = ((int((self.id_in_group-1)/32)%2)==0)
        access_to_car = (self.participant.vars['access_to_car']!=2)
        
        return {'trip_purpose': trip_purpose,
                'trip_mode': trip_mode,
                'language': language,
                'SN_car_A': SN_car_A,
                'access_to_car': access_to_car}
    
    def is_displayed(self):
        return C.vec[int((self.id_in_group-1)%24)][self.subsession.round_number-1] == 2

    
class A3c(Page):

    form_model = Player
    form_fields = ['LH']

    def vars_for_template(self):
        trip_purpose = self.participant.vars['trip_purpose']
        trip_mode = self.participant.vars['trip_mode']
        language = C.language
        SN_car_A = ((int((self.id_in_group-1)/32)%2)==0)
        access_to_car = (self.participant.vars['access_to_car']!=2)
        
        return {'trip_purpose': trip_purpose,
                'trip_mode': trip_mode,
                'language': language,
                'SN_car_A': SN_car_A,
                'access_to_car': access_to_car}
    
    def is_displayed(self):
        return C.vec[int((self.id_in_group-1)%24)][self.subsession.round_number-1] == 3

    
class A3d(Page):

    form_model = Player
    form_fields = ['LL']

    def vars_for_template(self):
        trip_purpose = self.participant.vars['trip_purpose']
        trip_mode = self.participant.vars['trip_mode']
        language = C.language
        SN_car_A = ((int((self.id_in_group-1)/32)%2)==0)
        access_to_car = (self.participant.vars['access_to_car']!=2)
        
        return {'trip_purpose': trip_purpose,
                'trip_mode': trip_mode,
                'language': language,
                'SN_car_A': SN_car_A,
                'access_to_car': access_to_car}
    
    def is_displayed(self):
        return C.vec[int((self.id_in_group-1)%24)][self.subsession.round_number-1] == 4
    

class A4(Page):

    form_model = Player
    form_fields = ['year_born','gender','education','income','family','children']

    def vars_for_template(self):
        language = C.language
        return {'language': language}
    
    def is_displayed(self):
        return self.subsession.round_number == 4

class A5(Page):

    form_model = Player
    form_fields = ['trust_parlament','trust_county','trust_municipality','trust_government','trust_politicians','trust_parties','vote']

    def vars_for_template(self):
        language = C.language
        return {'language': language}
    
    def is_displayed(self):
        return self.subsession.round_number == 4

class A6(Page):

    form_model = Player
    form_fields = ['air_pollution','road_pricing','revenues','tax','tax_level']

    def vars_for_template(self):
        language = C.language
        return {'language': language}
    
    def is_displayed(self):
        return self.subsession.round_number == 4
    
    
class A7(Page):
    
    form_model = Player
    form_fields = ['effect_rp','effect_rp_others']
    
    def vars_for_template(self):
        language = C.language
        return {'language': language}

    def is_displayed(self):
        return self.subsession.round_number == 4

class Comments(Page):

    form_model = Player
    form_fields = ['paypal_account', 'comments']

    def vars_for_template(self):
        language = C.language
        return {'language': language}
    
    def is_displayed(self):
        return self.subsession.round_number == 4


class End(Page):
    
    form_model = Player
    form_fields = ['paypal_account']

    def vars_for_template(self):
        language = C.language
        return {'language': language}
    
    def is_displayed(self):
        return self.subsession.round_number == 4

    
    
    
page_sequence = [A1,
                 A2,
                 A3a,
                 A3b,
                 A3c,
                 A3d,
                 A4,
                 A5,
                 A6,
                 A7,
                 Comments,
                 End
]

