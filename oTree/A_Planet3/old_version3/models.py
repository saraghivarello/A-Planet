from otree.api import (
	models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer, BaseLink,
	Currency as c, currency_range
)

import random


class Link(BaseLink):
	pass


class Constants(BaseConstants):
	name_in_url = 'AAplanetSN'
	players_per_group = None
	num_rounds = 1
	language = "ES"

	if language == "EN":

		question_EE = "What share (in %) of other participants in the survey do you think have chosen one of the transport modes in A for their daily trip?"
		question_PNB= "In your opinion, what should the ideal percentage of people using transport modes in A for their daily trip be?"
		question_NE = "What share (in %) of other participants in the survey do you think have mostly chosen option A (answered more than 50%) in the previous question?"

		question_private = "Considering the last year, how often (in %) did you use your chosen transport mode for your daily trip?"

		question_HH = "Imagine that most of the people answering this survey say that they use option A for their daily trip and that most of them think that other people should also use option A. How often (in %) would you use option A in this scenario?"
		question_HL = "Imagine that most of the people answering this survey say that they use option A for their daily trip and that most of them think that other people should use option B. How often (in %) would you use option A in this scenario?"
		question_LH = "Imagine that most of the people answering this survey say that they use option B for their daily trip and that most of them think that other people should use option A. How often (in %) would you use option A in this scenario?"
		question_LL = "Imagine that most of the people answering this survey say that they use option B for their daily trip and that most of them also think that other people should use option B. How often (in %) would you use option A in this scenario?"

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
						[10,"otro partido"],
						[11,"prefiero no responder"]]

		answers_trust = [[1,"1"],
						 [2,"2"],
						 [3,"3"],
						 [4,"4"],
						 [5,"5"],
						 [6,"6"],
						 [7,"7"],
						 [8,"I prefer to not answer"],
						 [9,"I do not know"]]

		question_air_pollution = "Air pollution derived by cars is one of the major causes of premature death in Europe:"
		question_road_pricing = "The introduction of policies such as road pricing will alleviate congestion problems:"
		question_revenues = "Revenues collected through taxes are used to create a well-functioning welfare state and society:"
		question_tax = "Tax revenues should be used to help those who are more in need:"

	elif language == "ES":

		question_EE = "1) ¿Qué proporción (en %) de los demás participantes en la encuesta cree que han elegido uno de los modos de transporte del tipo A para su viaje diario?"
		question_PNB= "2) En su opinión, ¿cuál debería ser el porcentaje ideal de personas que utilizan los modos de transporte del tipo A para sus desplazamientos diarios?"
		question_NE = "3) ¿Qué proporción (en %) de los demás participantes en la encuesta cree que han contestado con un porcentaje superior al 50 en la pregunta anterior (pregunta 2)?"

		question_private = "Teniendo en cuenta el último año, ¿con qué frecuencia (en %) utilizó el modo de transporte que nos ha dicho para su viaje diario?"

		question_HH = "Imagine que la mayoría de las personas que responden a esta encuesta dicen que utilizan la opción A para sus desplazamientos diarios y que la mayoría de ellas piensan que otras personas también deberían utilizar la opción A. ¿Con qué frecuencia (en %) utilizaría la opción A en esta situación?"
		question_HL = "Imagine que la mayoría de las personas que responden a esta encuesta dicen que utilizan la opción A para sus desplazamientos diarios y que la mayoría de ellas piensan que los demás deberían utilizar la opción B. ¿Con qué frecuencia (en %) utilizaría la opción A en esta situación?"
		question_LH = "Imagine que la mayoría de las personas que responden a esta encuesta dicen que utilizan la opción B para sus desplazamientos diarios y que la mayoría de ellas piensan que los demás deberían utilizar la opción A. ¿Con qué frecuencia (en %) utilizaría la opción A en esta situación?"
		question_LL = "Imagine que la mayoría de las personas que responden a esta encuesta dicen que utilizan la opción B para sus desplazamientos diarios y que la mayoría de ellas también piensan que otras personas deberían utilizar la opción B. ¿Con qué frecuencia (en %) utilizaría la opción A en esta situación?"

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

class Subsession(BaseSubsession):
	pass


class Group(BaseGroup):
	pass

class Player(BasePlayer):

	SN_car_A = models.BooleanField(default=None)

	EE = models.IntegerField(default=None, verbose_name=Constants.question_EE,min=0,max=100)
	PNB= models.IntegerField(default=None, verbose_name=Constants.question_PNB,min=0,max=100)
	NE = models.IntegerField(default=None, verbose_name=Constants.question_NE,min=0,max=100)

	my_trip = models.IntegerField(default=None, verbose_name=Constants.question_private,min=0,max=100)

	HH = models.IntegerField(default=None, verbose_name=Constants.question_HH,min=0,max=100)
	HL = models.IntegerField(default=None, verbose_name=Constants.question_HL,min=0,max=100)
	LH = models.IntegerField(default=None, verbose_name=Constants.question_LH,min=0,max=100)
	LL = models.IntegerField(default=None, verbose_name=Constants.question_LL,min=0,max=100)

	year_born = models.IntegerField(default=None, verbose_name=Constants.question_year_born, choices = range(1920,2004))
	gender = models.IntegerField(default=None, verbose_name=Constants.question_gender, choices = Constants.answers_gender,widget=widgets.RadioSelectHorizontal())
	education = models.IntegerField(default=None, verbose_name=Constants.question_education, choices = Constants.answers_education,widget=widgets.RadioSelect())
	income = models.IntegerField(default=None, verbose_name=Constants.question_income, choices = Constants.answers_income,widget=widgets.RadioSelect())
	family = models.IntegerField(default=None, verbose_name=Constants.question_family, choices = range(1,9),widget=widgets.RadioSelectHorizontal())
	children = models.IntegerField(default=None, verbose_name=Constants.question_children, choices = range(0,5),widget=widgets.RadioSelectHorizontal())

	trust_parlament = models.IntegerField(default=None, verbose_name=Constants.question_trust_parlament,choices = Constants.answers_trust,widget=widgets.RadioSelectHorizontal())
	trust_county = models.IntegerField(default=None, verbose_name=Constants.question_trust_county,choices = Constants.answers_trust,widget=widgets.RadioSelectHorizontal())
	trust_municipality = models.IntegerField(default=None, verbose_name=Constants.question_trust_municipality,choices = Constants.answers_trust,widget=widgets.RadioSelectHorizontal())
	trust_government = models.IntegerField(default=None, verbose_name=Constants.question_trust_government,choices = Constants.answers_trust,widget=widgets.RadioSelectHorizontal())
	trust_politicians = models.IntegerField(default=None, verbose_name=Constants.question_trust_politicians,choices = Constants.answers_trust,widget=widgets.RadioSelectHorizontal())
	trust_parties = models.IntegerField(default=None, verbose_name=Constants.question_trust_parties,choices = Constants.answers_trust,widget=widgets.RadioSelectHorizontal())

	vote = models.IntegerField(default=None, verbose_name = Constants.question_vote, choices = Constants.answers_vote,widget=widgets.RadioSelect())

	air_pollution = models.IntegerField(default=None, verbose_name = Constants.question_air_pollution,choices = Constants.answers_trust,widget=widgets.RadioSelectHorizontal())
	road_pricing = models.IntegerField(default=None, verbose_name = Constants.question_road_pricing,choices = Constants.answers_trust,widget=widgets.RadioSelectHorizontal())
	revenues = models.IntegerField(default=None, verbose_name = Constants.question_revenues,choices = Constants.answers_trust,widget=widgets.RadioSelectHorizontal())
	tax = models.IntegerField(default=None, verbose_name = Constants.question_tax,choices = Constants.answers_trust,widget=widgets.RadioSelectHorizontal())

	paypal_account = models.CharField()
	comments = models.TextField()




