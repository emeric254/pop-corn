# -*- coding: utf-8 -*-

import os
import logging

from modeles.carte import Carte

from outils import obtenir_configuration

configuration = obtenir_configuration()

logger = logging.getLogger(__name__)

CHEMIN_CARTE = os.path.join(configuration.chemin_dossier_donnees, 'carte.json')


def lire() -> Carte:
    if not os.path.isfile(path=CHEMIN_CARTE):
        # le fichier n'existe pas, retourne une carte vide
        return Carte()

    return Carte.parse_file(CHEMIN_CARTE)


def sauvegarde(carte: Carte) -> None:
    """TODO
    """
    with open(file=CHEMIN_CARTE, mode='w') as fichier:
        fichier.write(carte.json())
