from otree.api import *


doc = """
Your app description
"""


class C(BaseConstants):
    NAME_IN_URL = 'spasibo'
    PLAYERS_PER_GROUP = 8
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):

    get = models.StringField(label='Как Вы хотите распорядиться своим выигрышем?',
                             choices=['Забрать выигрыш',
                                      'Сделать пожертвование в благотворительный фонд "Защити жизнь"'],
                             widget=widgets.RadioSelect)
    contact = models.StringField(
        label='Если вы хотите получить выигрыш, оставьте свой контакт тут, с вами свяжутся для уточнения деталей')


# PAGES
class WinnerPage(Page):
    def is_displayed(self):
        return self.id_in_group == 1 or self.id_in_group == 8
    form_model = 'player'
    form_fields = ['get', 'contact']

class NoWinPage(Page):
    def is_displayed(self):
        return self.id_in_group != 1 and self.id_in_group != 8
    form_model = 'player'



page_sequence = [WinnerPage, NoWinPage]
