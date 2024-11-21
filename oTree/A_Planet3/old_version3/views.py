from . import models
from ._builtin import Page, WaitPage
from .functions import slider, tdm9
from otree.api import Currency as c, currency_range
from .models import Constants

class A_info(Page):

    form_model = models.Player
    form_fields = ['EE','PNB','NE']

    def vars_for_template(self):
        trip_purpose = self.participant.vars['trip_purpose']
        trip_mode = self.participant.vars['trip_mode']
        language = Constants.language
        SN_car_A = ((int((self.player.id_in_group-1)/32)%2)==0)
        self.player.SN_car_A = SN_car_A

        return {'trip_purpose': trip_purpose,
                'trip_mode': trip_mode,
                'language': language,
                'SN_car_A': SN_car_A}

class A_info2(Page):

    form_model = models.Player
    form_fields = ['my_trip']

    def vars_for_template(self):
        trip_purpose = self.participant.vars['trip_purpose']
        trip_mode = self.participant.vars['trip_mode']
        language = Constants.language
        SN_car_A = ((int((self.player.id_in_group-1)/32)%2)==0)

        return {'trip_purpose': trip_purpose,
                'trip_mode': trip_mode,
                'language': language,
                'SN_car_A': SN_car_A}

class A_info3(Page):

    form_model = models.Player
    form_fields = ['HH','HL','LH','LL']

    def vars_for_template(self):
        trip_purpose = self.participant.vars['trip_purpose']
        trip_mode = self.participant.vars['trip_mode']
        language = Constants.language
        SN_car_A = ((int((self.player.id_in_group-1)/32)%2)==0)
        access_to_car = (self.participant.vars['access_to_car']!=2)
        
        return {'trip_purpose': trip_purpose,
                'trip_mode': trip_mode,
                'language': language,
                'SN_car_A': SN_car_A,
                'access_to_car': access_to_car}


class A_info4(Page):

    form_model = models.Player
    form_fields = ['year_born','gender','education','income','family','children']

    def vars_for_template(self):
        language = Constants.language
        return {'language': language}

class A_info5(Page):

    form_model = models.Player
    form_fields = ['trust_parlament','trust_county','trust_municipality','trust_government','trust_politicians','trust_parties','vote']

    def vars_for_template(self):
        language = Constants.language
        return {'language': language}

class A_info6(Page):

    form_model = models.Player
    form_fields = ['air_pollution','road_pricing','revenues','tax']

    def vars_for_template(self):
        language = Constants.language
        return {'language': language}

class Comments(Page):

    form_model = models.Player
    form_fields = ['paypal_account', 'comments']

    def vars_for_template(self):
        language = Constants.language
        return {'language': language}

page_sequence = [
    A_info,
    A_info2,
    A_info3,
    A_info4,
    A_info5,
    A_info6,
    Comments,
]
