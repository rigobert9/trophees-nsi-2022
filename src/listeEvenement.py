from json import load
from random import choice
from bouton import *
from pygameSettings import afficher_text

from src.utils.constante import CITOYEN, FIN_DICT_VIDE, MAIRE, DEPUTE, DEPUTE_REGIONAL, MINISTRE, PRESIDENT, PRESIDENT_DES_NATIONS
from src.utils.affichage import Affichage

class ListeEvenement:

    grade = CITOYEN
    dict_citoyen         = {}
    dict_maire           = {}
    dict_depute          = {}
    dict_depregion       = {}
    dict_ministre        = {}
    dict_president       = {}
    dict_presidentnation = {}
    
    def __init__(self, grade):
        with open('src/utils/events/citoyen.json')         as f: self.dict_citoyen         = load(f)
        with open('src/utils/events/maire.json')           as f: self.dict_maire           = load(f)
        with open('src/utils/events/depute.json')          as f: self.dict_depute          = load(f)
        with open('src/utils/events/depRegion.json')       as f: self.dict_depregion       = load(f)
        with open('src/utils/events/ministre.json')        as f: self.dict_ministre        = load(f)
        with open('src/utils/events/president.json')       as f: self.dict_president       = load(f)
        with open('src/utils/events/presidentNation.json') as f: self.dict_presidentnation = load(f)
        self.grade = grade

    def get_grade(self) -> str:
        return self.grade

    def set_grade(self, grade):
        self.grade = grade

    def citoyen(self):
        if len(self.dict_citoyen) == 0:
            Affichage.fin_jeu(FIN_DICT_VIDE)
            return False
        event = choice(list(self.dict_citoyen.items()))
        del self.dict_citoyen[event[0]]
        return event

    def maire(self):
        if len(self.dict_maire) == 0:
            Affichage.fin_jeu(FIN_DICT_VIDE)
            return False
        event = choice(list(self.dict_maire.items()))
        del self.dict_maire[event[0]]
        return event
        
    def depute(self):
        if len(self.dict_depute) == 0:
            Affichage.fin_jeu(FIN_DICT_VIDE)
            return False
        event = choice(list(self.dict_depute.items()))
        del self.dict_depute[event[0]]
        return event

    def depregion(self):
        if len(self.dict_depregion) == 0:
            Affichage.fin_jeu(FIN_DICT_VIDE)
            return False
        event = choice(list(self.dict_depregion.items()))
        del self.depregion[event[0]]
        return event

    def ministre(self):
        if len(self.dict_ministre) == 0:
            Affichage.fin_jeu(FIN_DICT_VIDE)
            return False
        event = choice(list(self.dict_ministre.items()))
        del self.dict_ministre[event[0]]
        return event
        
    def president(self):
        if len(self.dict_president) == 0:
            Affichage.fin_jeu(FIN_DICT_VIDE)
            return False
        event = choice(list(self.dict_president.items()))
        del self.dict_president[event[0]]
        return event
        
    def presidentnation(self):
        if len(self.dict_presidentnation) == 0:
            Affichage.fin_jeu(FIN_DICT_VIDE)
            return False
        event = choice(list(self.dict_presidentnation.items()))
        del self.dict_presidentnation[event[0]]
        return event

    def faire_choix(self, screen):
        print(self.grade)
        if self.grade == CITOYEN:
            event = self.citoyen()
        elif self.grade == MAIRE:
            event = self.maire()
        elif self.grade == DEPUTE:
            event = self.depute()
        elif self.grade == DEPUTE_REGIONAL:
            event = self.depregion()
        elif self.grade == MINISTRE:
            event = self.ministre()
        elif self.grade == PRESIDENT:
            event = self.president()
        elif self.grade == PRESIDENT_DES_NATIONS:
            event = self.presidentnation()
        else:
            Affichage.erreur('Grade inconnu')
        return self.afficher(event, screen)

    def afficher(self, event, screen):
        print(event)
        interragibles = [
            Bouton((50, 50), (100, 100), "image/temp_debut.jpg", "image/imagepygame.jpg"),
            Bouton((240, 580), (120, 60), "image/oui.png", "image/oui_c.png", self.retour_true),
            Bouton((890, 580), (120, 60), "image/non.png", "image/non_c.png", self.retour_false)
        ]
        afficher_text(event[1]['titre'], screen, screen.font)
        wait = True
        while wait:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    choix = 'stop'
                if event.type == pygame.VIDEORESIZE:
                    screen.set_screen(pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE))

                # click de souris
                if event.type == pygame.MOUSEBUTTONDOWN:
                    # click gauche :
                    if event.button == 1:
                        for bouton in interragibles:
                            # Si le bouton est clické, alors sont état est clické
                            bouton.set_clicked(bouton.is_clicked())
                            r = bouton.click()

                # lacher le clic
                if event.type == pygame.MOUSEBUTTONUP:
                    # clic gauche :
                    if event.button == 1:
                        for bouton in interragibles:
                            # Du fait que le bouton est laché, il ne peut pas y avoir de bouton clické
                            bouton.set_clicked(False)
                            choix = bouton.click()
        print(choix)
        return {'accepter':choix, 'event':event[1]}
    
    def retour_true(self):
        return True
    def retour_false(self):
        return False
