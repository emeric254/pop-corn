# -*- coding: utf-8 -*-

import os
import logging

from modeles.carte import Carte, Zone

from outils import obtenir_configuration

configuration = obtenir_configuration()

logger = logging.getLogger(__name__)

CHEMIN_CARTE = os.path.join(configuration.chemin_dossier_donnees, 'carte.json')


def lire() -> Carte:
    """TODO
    """
    if not os.path.isfile(path=CHEMIN_CARTE):
        # le fichier n'existe pas, retourne un carte vide
        return Carte()

    try:
        return Carte.parse_file(path=CHEMIN_CARTE)
    except Exception:
        return Carte()


def sauvegarde(carte: Carte) -> None:
    """TODO
    """
    with open(file=CHEMIN_CARTE, mode='w') as fichier:
        fichier.write(carte.json())


def ajouter_zone(zone: Zone) -> Carte:
    """TODO
    """
    carte = lire()
    carte.zones[zone.id] = zone
    sauvegarde(carte=carte)
    return carte


def details_zone(id_zone: str) -> Zone:
    carte = lire()
    return carte.zones.get(id_zone)


def supprimer_zone(id_zone: str) -> None:
    """TODO
    """
    carte = lire()
    carte.zones.pop(id_zone)
    sauvegarde(carte=carte)
