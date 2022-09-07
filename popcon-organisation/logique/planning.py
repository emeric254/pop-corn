# -*- coding: utf-8 -*-

import os
import logging
import pyexcel
import datetime

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


def importer(contenu: bytes) -> Planning:
    """TODO
    """
    r = pyexcel.get_dict(contenu, name_columns_by_row=0)

    planning = Planning()

    clefs = list(r.keys())

    premiere_colonne = clefs[0]
    date = datetime.datetime.fromisoformat(premiere_colonne)

    horaires = r[premiere_colonne][1:]
    print(f'{horaires=}')

    jours = clefs[1:]
    print(f'{jours=}')

    zones = [r[jour][0] for jour in jours]
    print(f'{zones=}')

    nb_lignes = len(r[jours[0]])

    activites = {}

    for i in range(nb_lignes):
        valeur_horaire = horaires[i]

        if not valeur_horaire:
            # fin du contenu "utile" du fichier
            break

        heure, minute = valeur_horaire.split('h', 1)

        for j in range(len(jours)):
            jour = jours[j]
            zone = zones[j]

            if not jour or not zone:
                # inutile
                continue

            horaire = date.replace(hour=int(heure), minute=int(minute))
            if jour.startswith('DIMANCHE'):
                horaire += datetime.timedelta(days=1)
            elif not jour.startswith('SAMEDI'):
                # inutile
                continue

            valeur = r[jour][i]

            if not valeur:
                # inutile
                continue

            valeur = valeur.replace('\n', ' - ')

            clef_activite = valeur + ' - ' + horaire
            print(f'{clef_activite=}')

            print(f'{valeur=}')

            activites[clef_activite] = {
                'nom': valeur,
                'debut': horaire,
                'duree': 15,
                'zone': zone,
            }

    print(activites)

    clefs = sorted(list(activites.keys()))

    i = 0
    while i < len(clefs):
        clef = clefs[i]
        nom, horaire = clef.split(' - ')

        i += 1

        if i == len(clefs):
            # eviter de sortir de la liste
            break

        suivante = clefs[i + 1]
        nom_suivante, horaire_suivante = suivante.split(' - ')

        if nom != nom_suivante:
            # activite differente
            continue

        if datetime.datetime.fromisoformat(horaire) + datetime.timedelta(minutes=15) \
                == datetime.datetime.fromisoformat(suivante):
            # la meme activite
            # ajouter 15 min a sa duree
            activites[clef]['duree'] += 15
            # supprimer le duplicat
            activites.pop(suivante)

    for clef in activites.keys():
        activite = activites[clef]
        planning.activites[clef] = Activite.parse_obj(activite)

    return planning


def exporter(planning: Planning) -> bytes:
    """TODO
    """
    # TODO
    raise NotImplementedError
