# -*- coding: utf-8 -*-

import os
import logging

from modeles.planning import Planning, Activite

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

    try:
        return Planning.parse_file(path=CHEMIN_PLANNING)
    except Exception:
        return Planning()


def sauvegarde(planning: Planning) -> None:
    """TODO
    """
    with open(file=CHEMIN_PLANNING, mode='w') as fichier:
        fichier.write(planning.json())


def ajouter_activite(activite: Activite) -> Planning:
    """TODO
    """
    planning = lire()
    planning.activites[activite.nom] = activite
    sauvegarde(planning=planning)
    return planning


def details_activite(nom_activite: str) -> Activite:
    planning = lire()
    return planning.activites.get(nom_activite)


def supprimer_activite(nom_activite: str) -> None:
    """TODO
    """
    planning = lire()
    planning.activites.pop(nom_activite)
    sauvegarde(planning=planning)
