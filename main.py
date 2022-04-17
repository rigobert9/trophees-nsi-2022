from src.screen import Screen
from src.gestion import Gestion
from src.utils.texts import T_PROLOGUE
from pygameSettings import *
from src.utils.constante import CITOYEN
from bouton import *
g = Gestion()
ouvert = True
ecran = PROLOGUE
screen = Screen()

interragibles = [
    Bouton((50, 50), (100, 100), "image/temp_debut.jpg", "image/imagepygame.jpg"),
    Bouton((240, 580), (120, 60), "image/oui.png", "image/oui_c.png"),
    Bouton((890, 580), (120, 60), "image/non.png", "image/non_c.png")
]

while ouvert:
    screen.set_fond()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            ouvert = False
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
                if ecran == PROLOGUE:
                    ecran = CITOYEN
                    g.lancement(screen)
                for bouton in interragibles:
                    # Du fait que le bouton est laché, il ne peut pas y avoir de bouton clické
                    bouton.set_clicked(False)

    if ecran == MAIN:
        for i in interragibles:
            i.actualiser(screen)
    elif ecran == PROLOGUE:
        afficher_text(T_PROLOGUE, screen, screen.font, (0.5, 0.5), True, BLANC)
    elif ecran == CITOYEN:
        afficher_text(CITOYEN.capitalize(), screen, screen.font50, (0.12, 0.055), True, BLANC)

    pygame.display.flip()
    screen.clock.tick(60)


pygame.quit()
#g.set_nom(input('Bonjour, quel est ton nom? '))
# g.lancement()
