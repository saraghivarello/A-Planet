from otree.api import *



doc = """
This application provides a webpage instructing participants how to get paid.
Examples are given for the lab and Amazon Mechanical Turk (AMT).
"""


class C(BaseConstants):
    NAME_IN_URL = 'A_Planet1'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1
    language = "EN"
    start_time = "Asd"
    start_date = "asd"
    contact_email = "@#!@#"
    
    boolean_choices = [[1,"Sí"],[0,"No"]]
    
    municipality = [[0, 'Acebeda (La)'],
                    [1, 'Ajalvir'],
                    [2, 'Alameda del Valle'],
                    [3, 'Alamo (El)'],
                    [4, 'Alcalá de Henares'],
                    [5, 'Alcobendas'],
                    [6, 'Alcorcón'],
                    [7, 'Aldea del Fresno'],
                    [8, 'Algete'],
                    [9, 'Alpedrete'],
                    [10, 'Ambite'],
                    [11, 'Anchuelo'],
                    [12, 'Aranjuez'],
                    [13, 'Arganda del Rey'],
                    [14, 'Arroyomolinos'],
                    [15, 'Atazar (El)'],
                    [16, 'Batres'],
                    [17, 'Becerril de la Sierra'],
                    [18, 'Belmonte de Tajo'],
                    [19, 'Berzosa del Lozoya'],
                    [20, 'Berrueco (El)'],
                    [21, 'Boadilla del Monte'],
                    [22, 'Boalo (El)'],
                    [23, 'Braojos'],
                    [24, 'Brea de Tajo'],
                    [25, 'Brunete'],
                    [26, 'Buitrago del Lozoya'],
                    [27, 'Bustarviejo'],
                    [28, 'Cabanillas de la Sierra'],
                    [29, 'Cabrera (La)'],
                    [30, 'Cadalso de los Vidrios'],
                    [31, 'Camarma de Esteruelas'],
                    [32, 'Campo Real'],
                    [33, 'Canencia'],
                    [34, 'Carabaña'],
                    [35, 'Casarrubuelos'],
                    [36, 'Cenicientos'],
                    [37, 'Cercedilla'],
                    [38, 'Cervera de Buitrago'],
                    [39, 'Ciempozuelos'],
                    [40, 'Cobeña'],
                    [41, 'Colmenar del Arroyo'],
                    [42, 'Colmenar de Oreja'],
                    [43, 'Colmenarejo'],
                    [44, 'Colmenar Viejo'],
                    [45, 'Collado Mediano'],
                    [46, 'Collado Villalba'],
                    [47, 'Corpa'],
                    [48, 'Coslada'],
                    [49, 'Cubas de la Sagra'],
                    [50, 'Chapinería'],
                    [51, 'Chinchón'],
                    [52, 'Daganzo de Arriba'],
                    [53, 'Escorial (El)'],
                    [54, 'Estremera'],
                    [55, 'Fresnedillas de la Oliva'],
                    [56, 'Fresno de Torote'],
                    [57, 'Fuenlabrada'],
                    [58, 'Fuente el Saz de Jarama'],
                    [59, 'Fuentidueña de Tajo'],
                    [60, 'Galapagar'],
                    [61, 'Garganta de los Montes'],
                    [62, 'Gargantilla del Lozoya y Pinilla de Buitrago'],
                    [63, 'Gascones'],
                    [64, 'Getafe'],
                    [65, 'Griñón'],
                    [66, 'Guadalix de la Sierra'],
                    [67, 'Guadarrama'],
                    [68, 'Hiruela (La)'],
                    [69, 'Horcajo de la Sierra-Aoslos'],
                    [70, 'Horcajuelo de la Sierra'],
                    [71, 'Hoyo de Manzanares'],
                    [72, 'Humanes de Madrid'],
                    [73, 'Leganés'],
                    [74, 'Loeches'],
                    [75, 'Lozoya'],
                    [76, 'Lozoyuela-Navas-Sieteiglesias'],
                    [77, 'Madarcos'],
                    [78, 'Madrid - Arganzuela'],
                    [79, 'Madrid - Barajas'],
                    [80, 'Madrid - Carabanchel'],
                    [81, 'Madrid - Centro'],
                    [82, 'Madrid - Chamartín'],
                    [83, 'Madrid - Chamberí'],
                    [84, 'Madrid - Ciudad Lineal'],
                    [85, 'Madrid - Fuencarral - El Pardo'],
                    [86, 'Madrid - Hortaleza'],
                    [87, 'Madrid - Latina'],
                    [88, 'Madrid - Moncloa Aravaca'],
                    [89, 'Madrid - Moratalaz'],
                    [90, 'Madrid - Puente de Vallecas'],
                    [91, 'Madrid - Retiro'],
                    [92, 'Madrid - Salamanca'],
                    [93, 'Madrid - San Blas - Canillejas'],
                    [94, 'Madrid - Tetuán'],
                    [95, 'Madrid - Usera'],
                    [96, 'Madrid - Vicálvaro'],
                    [97, 'Madrid - Villa de Vallecas'],
                    [98, 'Madrid - Villaverde'],
                    [99, 'Majadahonda'],
                    [100, 'Manzanares el Real'],
                    [101, 'Meco'],
                    [102, 'Mejorada del Campo'],
                    [103, 'Miraflores de la Sierra'],
                    [104, 'Molar (El)'],
                    [105, 'Molinos (Los)'],
                    [106, 'Montejo de la Sierra'],
                    [107, 'Moraleja de Enmedio'],
                    [108, 'Moralzarzal'],
                    [109, 'Morata de Tajuña'],
                    [110, 'Móstoles'],
                    [111, 'Navacerrada'],
                    [112, 'Navalafuente'],
                    [113, 'Navalagamella'],
                    [114, 'Navalcarnero'],
                    [115, 'Navarredonda y San Mamés'],
                    [116, 'Navas del Rey'],
                    [117, 'Nuevo Baztán'],
                    [118, 'Olmeda de las Fuentes'],
                    [119, 'Orusco de Tajuña'],
                    [120, 'Paracuellos de Jarama'],
                    [121, 'Parla'],
                    [122, 'Patones'],
                    [123, 'Pedrezuela'],
                    [124, 'Pelayos de la Presa'],
                    [125, 'Perales de Tajuña'],
                    [126, 'Pezuela de las Torres'],
                    [127, 'Pinilla del Valle'],
                    [128, 'Pinto'],
                    [129, 'Piñuecar-Gandullas'],
                    [130, 'Pozuelo de Alarcón'],
                    [131, 'Pozuelo del Rey'],
                    [132, 'Prádena del Rincón'],
                    [133, 'Puebla de la Sierra'],
                    [134, 'Puentes Viejas'],
                    [135, 'Quijorna'],
                    [136, 'Rascafría'],
                    [137, 'Redueña'],
                    [138, 'Ribatejada'],
                    [139, 'Rivas-Vaciamadrid'],
                    [140, 'Robledillo de la Jara'],
                    [141, 'Robledo de Chavela'],
                    [142, 'Robregordo'],
                    [143, 'Rozas de Madrid (Las)'],
                    [144, 'Rozas de Puerto Real'],
                    [145, 'San Agustín del Guadalix'],
                    [146, 'San Fernando de Henares'],
                    [147, 'San Lorenzo de El Escorial'],
                    [148, 'San Martín de la Vega'],
                    [149, 'San Martín de Valdeiglesias'],
                    [150, 'San Sebastián de los Reyes'],
                    [151, 'Santa María de la Alameda'],
                    [152, 'Santorcaz'],
                    [153, 'Santos de la Humosa (Los)'],
                    [154, 'Serna del Monte (La)'],
                    [155, 'Serranillos del Valle'],
                    [156, 'Sevilla la Nueva'],
                    [157, 'Somosierra'],
                    [158, 'Soto del Real'],
                    [159, 'Talamanca de Jarama'],
                    [160, 'Tielmes'],
                    [161, 'Titulcia'],
                    [162, 'Torrejón de Ardoz'],
                    [163, 'Torrejón de la Calzada'],
                    [164, 'Torrejón de Velasco'],
                    [165, 'Torrelaguna'],
                    [166, 'Torrelodones'],
                    [167, 'Torremocha de Jarama'],
                    [168, 'Torres de la Alameda'],
                    [169, 'Tres Cantos'],
                    [170, 'Valdaracete'],
                    [171, 'Valdeavero'],
                    [172, 'Valdelaguna'],
                    [173, 'Valdemanco'],
                    [174, 'Valdemaqueda'],
                    [175, 'Valdemorillo'],
                    [176, 'Valdemoro'],
                    [177, 'Valdeolmos-Alalpardo'],
                    [178, 'Valdepiélagos'],
                    [179, 'Valdetorres de Jarama'],
                    [180, 'Valdilecha'],
                    [181, 'Valverde de Alcalá'],
                    [182, 'Velilla de San Antonio'],
                    [183, 'Vellón (El)'],
                    [184, 'Venturada'],
                    [185, 'Villaconejos'],
                    [186, 'Villa del Prado'],
                    [187, 'Villalbilla'],
                    [188, 'Villamanrique de Tajo'],
                    [189, 'Villamanta'],
                    [190, 'Villamantilla'],
                    [191, 'Villanueva de la Cañada'],
                    [192, 'Villanueva del Pardillo'],
                    [193, 'Villanueva de Perales'],
                    [194, 'Villar del Olmo'],
                    [195, 'Villarejo de Salvanés'],
                    [196, 'Villaviciosa de Odón'],
                    [197, 'Villavieja del Lozoya'],
                    [198, 'Zarzalejo']]

    if language == "ES":
        
        q1_question1 = "¿Cuál es la municipalidad de su domicilio?"
        
        q2_question1 = "¿Tiene permiso de conducir?"
        q2_choices1 = boolean_choices

        q2_question2 = "¿Posee o tiene acceso a un coche?"
        q2_choices2 = [[0,"Poseo"],[1,"No poseo, pero tengo acceso a"],[2,"No tengo acceso a"]]

        q2_question3 = "¿A qué tipo de vehículo tiene acceso? Si tiene acceso a varios vehículos, elige el que más utilice."
        q2_choices3 = [[0,"Gasolina"],[1,"Diésel"],[2,"Híbrido o híbrido enchufable"],[3,"Eléctrico"]]

        q2_question4 = "¿Piensa comprar un coche en el próximo año?"
        q2_choices4 = [[0,"Sí, gasolina"],[1,"Sí, diésel"],[2,"Sí, híbrido o híbrido enchufable"],[3,"Sí, eléctrico"],[4,"No"]]

        q3_question1 = "¿Posee o tiene acceso a una bicicleta (eléctrica o normal)?"
        q3_choices1 = [[0,"Poseo"],[1,"No poseo, pero tengo acceso a"],[2,"No tengo acceso a"]]     
        q3b_question1 = "¿Posee o tiene acceso a una motocicleta?"
        q3b_choices1 = [[0,"Poseo"],[1,"No poseo, pero tengo acceso a"],[2,"No tengo acceso a"]]     
        q3c_question1 = "¿Tienes o tienes acceso a un patinete eléctrico?"
        q3c_choices1 = [[0,"Poseo"],[1,"No poseo, pero tengo acceso a"],[2,"No tengo acceso a"]]   

        q4_question1 = "¿Cuál es su situación laboral?"
        q4_choices1 = [[0,"Trabajador/a a tiempo completo"],[1,"Trabajador/a a tiempo parcial"],[2,"Estudiante"],[3,"Jubilado/a"],[4, "Desempleado/a"], [5, "Otra"]]

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
                       [9,"Otro"]]
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
        q7_question6 = "¿Paga peajes en su viaje?"
        q7_choices6 = [[0,"Sí"], [1,"No"]]
        q7_question7 = "Si tuviera que realizar este viaje utilizando un modo de transporte diferente al habitual, ¿cuál sería la mejor alternativa?"
        q7_choices7 = [[0,"Coche privado (conductor)"], 
                       [1,"Coche privado (pasajero)"],
                       [2,"Autobús"],
                       [3,"Metro, metro ligero o tranvía"],
                       [4,"Tren (Cercanías o larga distancia)"],
                       [5,"Caminando"],
                       [6,"Bicicleta (normal o eléctrica)"],
                       [7,"Patinete"],
                       [8,"Motocicleta"],
                       [9,"Otro"],
                       [10,"No tengo alternativas disponibles"]]
        q7_question8 = "¿Cómo calificaría su alternativa?"
        q7_choices8 = [[0,"Casi tan buena como mi elección actual"], 
                       [1,"Algo peor que mi elección actual"],
                       [2,"Mucho peor que mi elección actual"],
                       [3,"No lo sé"]]

        q7d_question1 = "Por favor, especifique las razones por las que no tiene una alternativa."

        q8_inequality = "¿Qué tipo de sociedad cree que es España hoy en día, qué diagrama se acerca más?"
        inequality_choices = [[1,"A"],[2,"B"],[3,"C"],[4,"D"],[5,"E"],[6,"No lo sé"]]

        q8a_inequality = "¿Cómo cree que debería ser España? ¿Qué diagrama prefiere?"

        q8b_inequality = "¿Cómo de justa cree que es la distribución de la riqueza en su país?"
        q8b_inequality_choices = [[1,"Muy justa"],[2,"Justa"],[3,"Injusta"],[4,"Muy injusta"],[5,"No lo sé"]]  

        revenue_alternatives = [[1,"Presupuesto general"],
                                [2,"Transferencia igualitaria"],
                                [3,"Transferencia para los ciudadanos con bajos ingresos"],
                                [4,"Inversiones en carreteras"],
                                [5,"Inversiones en transporte público, a pie y en bicicleta"]] 

    
    if language == "EN":

        q1_question1 = "What is the municipality of your home address?"
        
        q2_question1 = "Do you have a driver license?"
        q2_choices1 = [[0,"Yes"],[1,"No"]]

        q2_question2 = "Do you own or have access to a car?"
        q2_choices2 = [[0,"I own"],[1,"I don't own, but have access to"],[2,"I do not have access to"]]
    
        q2_question3 = "What kind of vehicle do you have access to? If you have access to multiple vehicles choose the one you use the most."
        q2_choices3 = [[0,"Gasoline"],[1,"Diesel"],[2,"Hybrid or plug-in hybrid"],[3,"Electric"]]
        
        q2_question4 = "Are you planning to buy a car in the next year?"
        q2_choices4 = [[0,"Yes, gasoline"],[1,"Yes, diesel"],[2,"Yes, hybrid or plug-in hybrid"],[3,"Yes, electric"],[4,"No"]]

        q3_question1 = "Do you own or have access to a bike (electric or regular)?"
        q3_choices1 = [[0,"I own"],[1,"I don't own, but have access to"],[2,"I do not have access to"]]
        q3b_question1 = "Do you own or have access to a motorbyke?"
        q3b_choices1 = [[0,"I own"],[1,"I don't own, but have access to"],[2,"I do not have access to"]]
        q3c_question1 = "Do you own or have access to a e-scooter?"
        q3c_choices1 = [[0,"I own"],[1,"I don't own, but have access to"],[2,"I do not have access to"]]
        
        q4_question1 = "What is your employment status?"
        q4_choices1 = [[0,"Full-time worker"],[1,"Part-time worker"],[2,"Student"],[3,"Retired"],[4, "Unemployed"], [5, "Not working for other reasons"]]

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
                       [9,"Other"]]
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
        q7_choices5 = [[0,"less than 1 EUR"], 
                       [1,"1-2.50 EUR"],
                       [2,"2.50-4.99 EUR"],
                       [3,"5-9.99 EUR"],
                       [4,"10-19.99 EUR"],
                       [5,"20 EUR or more"]]
        q7_question6 = "Do you pay road tolls on your trip?"
        q7_choices6 = [[0,"Yes"], [1,"No"]]
        q7_question7 = "If you were to make this trip using a different mode of travel than your usual mode, which would be the best alternative?"
        q7_choices7 = [[0,"Private car (driver)"], 
                       [1,"Private car (passenger)"],
                       [2,"Bus"],
                       [3,"Metro, tram or light rail"],
                       [4,"Train"],
                       [5,"Walk"],
                       [6,"Bike (regular or electric)"],
                       [7,"E-scooter"],
                       [8,"Motorcycle"],
                       [9,"Other"],
                       [10,"I have no available alternatives"]]
        q7_question8 = "How would you rate your alternative?"
        q7_choices8 = [[0,"Almost as good as my current choice"], 
                       [1,"Somewhat worse than my current choice"],
                       [2,"Much worse than my current choice"],
                       [3,"I do not know"]]

        q7d_question1 = "Please specify the reasons of why you do not have an alternative."
        
        q8_inequality = "What type of society do you think is Spain today – which diagram comes the closest?"
        inequality_choices = [[1,"A"],[2,"B"],[3,"C"],[4,"D"],[5,"E"],[6,"I do not know"]]

        q8a_inequality = "What do you think Spain ought to be like – which would you prefer?"
        
        q8b_inequality = "How fair do you think the wealth distribution is in your country?"
        q8b_inequality_choices = [[1,"Very fair"],[2,"Fair"],[3,"Unfair"],[4,"Very unfair"],[5,"I do not know"]]

        control_question = "How many NOK would you spend for this trip?"
        control_question_choices = [[0,"1,5 NOK"],[1,"15 NOK"],[2,"20 NOK"],[3,"30 NOK"]]

        revenue_alternatives = [[1,"General budget"],
                                [2,"Equal cash transfer"],
                                [3,"Cash transfer for low-income citizens"],
                                [4,"Investments in roads"],
                                [5,"Investments in public transport, walking and cycling"]]

      


      ##########################################################################################################################################
    
    
class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):

    language = models.CharField(default="EN")
    
    
      ##########################################################################################################################################
    
    #   QUESTIONS 1

    municipality_home = models.IntegerField(verbose_name=C.q1_question1, choices=C.municipality)
    
 ##########################################################################################################################################
    
     #   QUESTIONS 2 & 2b & 2c

    driving_license = models.BooleanField(default=None, choices=C.q2_choices1, verbose_name = C.q2_question1, widget=widgets.RadioSelectHorizontal())
    access_to_car = models.IntegerField(default=None, choices=C.q2_choices2, verbose_name = C.q2_question2, widget=widgets.RadioSelect())
    car_type = models.IntegerField(default=None, choices=C.q2_choices3, verbose_name = C.q2_question3, widget=widgets.RadioSelect())
    buy_car_type = models.IntegerField(default=None, choices=C.q2_choices4, verbose_name = C.q2_question4, widget=widgets.RadioSelect())
    ##########################################################################################################################################    
    #   QUESTIONS 3 & 3b & 3c
    
    access_to_bike = models.IntegerField(default=None, choices=C.q3_choices1, verbose_name = C.q3_question1, widget=widgets.RadioSelect())
    access_to_motorbyke = models.IntegerField(default=None, choices=C.q3b_choices1, verbose_name = C.q3b_question1, widget=widgets.RadioSelect())
    access_to_scooter = models.IntegerField(default=None, choices=C.q3c_choices1, verbose_name = C.q3c_question1, widget=widgets.RadioSelect())
  ##########################################################################################################################################
    
    #   QUESTIONS 4
    
    employ_status = models.IntegerField(default=None, choices=C.q4_choices1, verbose_name = C.q4_question1, widget=widgets.RadioSelect())
  ##########################################################################################################################################
    
    #   QUESTIONS 5 
    
    #travel_behavior = models.BooleanField(default=None, choices=C.q5_choices1, verbose_name =C.q5_question1, widget=widgets.RadioSelectHorizontal())
  ##########################################################################################################################################
    
    #   QUESTIONS 6 & 6b
    
    municipality_destination = models.IntegerField(default=None, verbose_name=C.q6_question1, choices=C.municipality)
    trip_purpose = models.IntegerField(default=None, choices=C.q6_choices2,verbose_name=C.q6_question2,widget=widgets.RadioSelect())

    trip_other = models.CharField(default=None, verbose_name =C.q6b_question1)
    ##########################################################################################################################################
    
    #   QUESTIONS 7
    
    trip_moment = models.IntegerField(default=None, choices=C.q7_choices1, verbose_name = C.q7_question1,widget=widgets.RadioSelect())
    trip_mode = models.IntegerField(default=None, choices=C.q7_choices2,verbose_name=C.q7_question2,widget=widgets.RadioSelect())
    mode_other = models.CharField(default=None, verbose_name = C.q7_question1_other)
    trip_traffic = models.IntegerField(default=None, choices=C.q7_choices3, verbose_name = C.q7_question3,widget=widgets.RadioSelect())
    trip_time = models.IntegerField(default=None, choices=C.q7_choices4, verbose_name = C.q7_question4,widget=widgets.RadioSelect())
    trip_cost = models.IntegerField(default=None, choices=C.q7_choices5, verbose_name = C.q7_question5,widget=widgets.RadioSelect())
    trip_tolls = models.IntegerField(default=None, choices=C.q7_choices6, verbose_name = C.q7_question6 ,widget=widgets.RadioSelect())   
    trip_alternative_mode = models.IntegerField(default=None, choices=C.q7_choices7, verbose_name = C.q7_question7,widget=widgets.RadioSelect())
    trip_alternative_rate = models.IntegerField(default=None, choices=C.q7_choices8, verbose_name = C.q7_question8,widget=widgets.RadioSelect())
    trip_alternative_justification = models.CharField(default=None, verbose_name = C.q7d_question1)
    
      ##########################################################################################################################################
    
     #   QUESTIONS 8 - INEQUALITY 
     
    inequality_perception = models.IntegerField(default=None, verbose_name=C.q8_inequality,choices=C.inequality_choices,widget=widgets.RadioSelectHorizontal())
    inequality_wish = models.IntegerField(default=None, verbose_name=C.q8a_inequality,choices=C.inequality_choices,widget=widgets.RadioSelectHorizontal())
    income_distribution= models.IntegerField(default=None, verbose_name=C.q8b_inequality,choices=C.q8b_inequality_choices,widget=widgets.RadioSelect())
    
    ##########################################################################################################################################
    

    paypal_account = models.CharField()
    comments = models.TextField(blank=True)
 
    
    def set_language(self, language):

        self.language = language
    

# FUNCTIONS



# PAGES
class A1(Page):
    def before_next_page(self, timeout_happened):
        self.set_language(C.language)
    def vars_for_template(self):
        language = C.language
        return {'language': language}
    def is_displayed(self):
        return self.subsession.round_number == 1

class A2(Page):
    def vars_for_template(self):
        language = C.language
        return {'language': language}
    def is_displayed(self):
        return self.subsession.round_number == 1    
    
class B1(Page):
    form_model = Player
    form_fields = ['municipality_home','employ_status']

    def vars_for_template(self):
        language = C.language
        return {'language': language}

    def is_displayed(self):
        return self.subsession.round_number == 1
    
    
class B2(Page):
    form_model = Player
    form_fields = ['driving_license','access_to_car']

    def vars_for_template(self):
        language = C.language
        return {'language': language}

    def is_displayed(self):
        return self.subsession.round_number == 1       

    def before_next_page(self, timeout_happened):
        self.participant.vars['access_to_car'] = self.access_to_car
    
    
class B2b(Page):
    form_model = Player
    form_fields = ['car_type']

    def vars_for_template(self):
        language = C.language
        return {'language': language}

    def is_displayed(self):
        return self.subsession.round_number == 1 and self.access_to_car != 2
    
    
class B2c(Page):
    form_model = Player
    form_fields = ['buy_car_type']

    def vars_for_template(self):
        language = C.language
        return {'language': language}

    def is_displayed(self):
        return self.subsession.round_number == 1 and self.access_to_car != 0
    
    
class B3(Page):
    form_model = Player
    form_fields = ['access_to_bike','access_to_motorbyke','access_to_scooter']

    def vars_for_template(self):
        language = C.language
        return {'language': language}

    def is_displayed(self):
        return self.subsession.round_number == 1            
             

class B6(Page):
    form_model = Player
    form_fields = ['municipality_destination','trip_purpose']

    def vars_for_template(self):
        language = C.language
        return {'language': language}

    def is_displayed(self):
        return self.subsession.round_number == 1     

    def before_next_page(self, timeout_happened):
        if C.language == "EN":
            choices = ["Workplace",
                       "Education place",
                       "Trip within my job/for job purposes",
                       "Bring/pick up children or adult",
                       "Errands or shopping",
                       "Visit family or friend",
                       "Leisure activity (cultural, sport, etc)",
                       "Other"]
        elif C.language == "ES":
            choices = ["Lugar de trabajo", 
                       "Lugar de educación",
                       "Viaje dentro de mi trabajo/por motivos laborales",
                       "Traer/recoger niños o adultos",
                       "Recados o compras",
                       "Visitar a la familia o a un amigo",
                       "Actividad de ocio (cultural, deportiva, etc.)",
                       "Otro"]
        self.participant.vars['trip_purpose'] = choices[self.trip_purpose]
        

class B6b(Page):
    form_model = Player
    form_fields = ['trip_other']

    def vars_for_template(self):
        language = C.language
        return {'language': language}

    def before_next_page(self, timeout_happened):
        self.participant.vars['trip_purpose'] = self.trip_other

    def is_displayed(self):
        return self.subsession.round_number == 1 and self.trip_purpose == 7   
    
    
class B7(Page):
    form_model = Player
    form_fields = ['trip_moment','trip_mode']

    def vars_for_template(self):
        from_home = (self.id_in_group % 2) == 0
        language = C.language
        trip_purpose = self.participant.vars['trip_purpose']
        return {'language': language, 'from_home': from_home, 'trip_purpose': trip_purpose}

    def before_next_page(self, timeout_happened):
        if C.language == "EN":
            choices = ["Private car (driver)", 
                       "Private car (passenger)",
                       "Bus",
                       "Metro or tram",
                       "Train",
                       "Walk",
                       "Bike (regular or electric)",
                       "E-scooter",
                       "Motorcycle",
                       "Other"]
        elif C.language == "ES":
            choices = ["Coche privado (conductor)", 
                       "Coche privado (pasajero)",
                       "Autobús",
                       "Metro, metro ligero o tranvía",
                       "Tren (Cercanías o larga distancia)",
                       "Caminando",
                       "Bicicleta (normal o eléctrica)",
                       "Patinete",
                       "Motocicleta",
                       "Otro"]
        self.participant.vars['trip_mode'] = choices[self.trip_mode]

    def is_displayed(self):
        return self.subsession.round_number == 1     

    
class B7a(Page):
    form_model = Player
    form_fields = ['mode_other']

    def vars_for_template(self):
        from_home = (self.id_in_group % 2) == 0
        language = C.language
        return {'language': language, 'from_home': from_home}

    def before_next_page(self, timeout_happened):
        self.participant.vars['trip_mode'] = self.mode_other

    def is_displayed(self):
        return self.subsession.round_number == 1 and self.trip_mode == 9 

    
class B7b1(Page):
    form_model = Player
    form_fields = ['trip_traffic','trip_time','trip_cost']

    def vars_for_template(self):
        from_home = (self.id_in_group % 2) == 0
        language = C.language
        return {'language': language, 'from_home': from_home}

    def is_displayed(self):
        return self.subsession.round_number == 1 and (self.trip_mode != 0 and self.trip_mode != 1 and self.trip_mode != 8)    
    
class B7b2(Page):
    form_model = Player
    form_fields = ['trip_traffic','trip_time','trip_cost','trip_tolls']

    def vars_for_template(self):
        from_home = (self.id_in_group % 2) == 0
        language = C.language
        return {'language': language, 'from_home': from_home}

    def is_displayed(self):
        return self.subsession.round_number == 1 and (self.trip_mode == 0 or self.trip_mode == 1 or self.trip_mode == 8)       

    
class B7c(Page):
    form_model = Player
    form_fields = ['trip_alternative_mode']

    def vars_for_template(self):
        from_home = (self.id_in_group % 2) == 0
        language = C.language
        return {'language': language, 'from_home': from_home}

    def is_displayed(self):
        return self.subsession.round_number == 1          

class B7d(Page):
    form_model = Player
    form_fields = ['trip_alternative_rate']

    def vars_for_template(self):
        from_home = (self.id_in_group % 2) == 0
        language = C.language
        return {'language': language, 'from_home': from_home}

    def is_displayed(self):
        return self.subsession.round_number == 1 and self.trip_alternative_mode != 10 #[1] metti 'Otro'

    
class B7e(Page):
    form_model = Player
    form_fields = ['trip_alternative_justification']

    def vars_for_template(self):
        from_home = (self.id_in_group % 2) == 0
        language = C.language
        return {'language': language, 'from_home': from_home}

    def is_displayed(self):
        return self.subsession.round_number == 1 and self.trip_alternative_mode == 10

    
class B8(Page):
    form_model = Player
    form_fields = ['inequality_perception','inequality_wish','income_distribution']
    def vars_for_template(self):
        language = C.language
        return {'language': language}
    def is_displayed(self):
        return self.subsession.round_number == 1   
        


page_sequence = [A1,
                 A2,
                 B1,
                 B2,
                 B2b,
                 B2c,
                 B3,
                 B6,
                 B6b,
                 B7,
                 B7a,
                 B7b1,
                 B7b2,
                 B7c,
                 B7d,
                 B7e,
                 B8
]



