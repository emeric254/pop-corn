# -*- coding: utf-8 -*-

import os
import logging

from modeles.planning import Planning

from outils import obtenir_configuration

configuration = obtenir_configuration()

logger = logging.getLogger(__name__)

CHEMIN_PLANNING = os.path.join(configuration.chemin_dossier_donnees, 'planning.json')


def lire() -> Planning:
    """TODO
    """
    if not os.path.isfile(path=CHEMIN_PLANNING):
        # le fichier n'existe pas, retourne un planning vide
        return Planning()

    return Planning.parse_file(CHEMIN_PLANNING)


def sauvegarde(planning: Planning) -> None:
    """TODO
    """
    with open(file=CHEMIN_PLANNING, mode='w') as fichier:
        fichier.write(planning.json())
