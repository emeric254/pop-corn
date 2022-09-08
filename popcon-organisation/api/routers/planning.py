# -*- coding: utf-8 -*-

import logging
from fastapi import APIRouter, Depends, HTTPException

from api.dependances import utilisateur_courant

from logique import planning

from modeles.base import Id
from modeles.planning import Planning, Activite


loguer = logging.getLogger(__name__)

routeur = APIRouter(
    prefix='/planning',
    tags=['planning'],
    dependencies=[Depends(utilisateur_courant)],
)


@routeur.get(
    '/activites',
    response_model=Planning,
)
async def obtenir_planning(*, _: Id = Depends(utilisateur_courant)):
    return planning.lire()


@routeur.post(
    '/activites',
    response_model=Planning,
    responses={
        422: {'description': 'Activite invalide'}
    },
)
async def nouvelle_activite(*, _: Id = Depends(utilisateur_courant), activite: Activite):
    return planning.ajouter_activite(activite=activite)


@routeur.put(
    '/activites',
    responses={
        422: {'description': 'Planning invalide'}
    },
)
async def ecraser_planning(*, _: Id = Depends(utilisateur_courant), nouveau_planning: Planning):
    planning.sauvegarde(nouveau_planning)


@routeur.get(
    '/activites/{nom_activite}',
    response_model=Activite,
    responses={
        404: {'description': 'Activite inexistante'}
    },
)
async def obtenir_activite(*, _: Id = Depends(utilisateur_courant), nom_activite: str):
    activite = planning.details_activite(nom_activite=nom_activite)

    if not activite:
        raise HTTPException(status_code=404, detail='Cette activite n\'exsite pas')

    return activite


@routeur.put(
    '/activites/{nom_activite}',
    response_model=Activite,
    responses={
        404: {'description': 'Activite inexistante'},
        422: {'description': 'Activite invalide'}
    },
)
async def modifier_activite(*, _: Id = Depends(utilisateur_courant), nom_activite: str, activite: Activite):
    # on verifie si l'activite existe pour emuler le comportement d'une vraie REST API
    existe = planning.details_activite(nom_activite=nom_activite)

    if not existe:
        raise HTTPException(status_code=404, detail='Cette activite n\'exsite pas')

    planning.supprimer_activite(nom_activite=nom_activite)

    planning.ajouter_activite(activite=activite)

    return activite


@routeur.delete('/activites/{nom_activite}')
async def supprimer_activite(*, _: Id = Depends(utilisateur_courant), nom_activite: str):
    planning.supprimer_activite(nom_activite=nom_activite)


# @routeur.post(
#     '/importer',
#     response_model=Planning,
#     responses={
#         401: {'description': 'Jeton invalide'}
#     },
# )
# async def importer_planning(*, _: Id = Depends(utilisateur_courant), fichier):  # TODO importer un fichier
#
#     # TODO analyser le fichier
#
#     # TODO supprimer ancien planning
#
#     # TODO creer nouveau planning
#
#     # TODO recuperer nouveau planning
#
#     return Planning()
#
#
# @routeur.post(
#     '/exporter',
#     response_model=fichier,  # TODO exporter un fichier
#     responses={
#         401: {'description': 'Jeton invalide'}
#     },
# )
# async def exporter_planning(*, _: Id = Depends(utilisateur_courant)):
#     # TODO recuperer planning
#
#     # TODO creer fichier
#
#     return fichier  # TODO retourner le fichier

