# -*- coding: utf-8 -*-

import logging
from fastapi import APIRouter, Depends, HTTPException

from api.dependances import utilisateur_courant

from logique import carte

from modeles.base import Id
from modeles.carte import Carte, Zone


loguer = logging.getLogger(__name__)

routeur = APIRouter(
    prefix='/carte',
    tags=['carte'],
    dependencies=[Depends(utilisateur_courant)],
)


@routeur.get(
    '/zones',
    response_model=Carte,
)
async def obtenir_carte(*, _: Id = Depends(utilisateur_courant)):
    return carte.lire()


@routeur.post(
    '/zones',
    response_model=Carte,
    responses={
        422: {'description': 'Zone invalide'}
    },
)
async def nouvelle_zone(*, _: Id = Depends(utilisateur_courant), zone: Zone):
    return carte.ajouter_zone(zone=zone)


@routeur.get(
    '/zones/{id_zone}',
    response_model=Zone,
    responses={
        404: {'description': 'Zone inexistante'}
    },
)
async def obtenir_zone(*, _: Id = Depends(utilisateur_courant), id_zone: str):
    zone = carte.details_zone(id_zone=id_zone)

    if not zone:
        raise HTTPException(status_code=404, detail='Cette zone n\'exsite pas')

    return zone


@routeur.put(
    '/zones/{id_zone}',
    response_model=Zone,
    responses={
        404: {'description': 'Zone inexistante'},
        422: {'description': 'Zone invalide'}
    },
)
async def modifier_zone(*, _: Id = Depends(utilisateur_courant), id_zone: str, zone: Zone):
    # on verifie si la zone existe pour emuler le comportement d'une vraie REST API
    existe = carte.details_zone(id_zone=id_zone)

    if not existe:
        raise HTTPException(status_code=404, detail='Cette zone n\'exsite pas')

    carte.ajouter_zone(zone=zone)

    return zone


@routeur.delete('/zones/{id_zone}')
async def supprimer_zone(*, _: Id = Depends(utilisateur_courant), id_zone: str):
    carte.supprimer_zone(id_zone=id_zone)


# @routeur.post(
#     '/importer',
#     response_model=Planning,
#     responses={
#         401: {'description': 'Jeton invalide'}
#     },
# )
# async def importer_carte(*, _: Id = Depends(utilisateur_courant), fichier):  # TODO importer un fichier
#
#     # TODO analyser le fichier
#
#     # TODO supprimer ancien carte
#
#     # TODO creer nouvelle carte
#
#     # TODO recuperer nouvelle carte
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
# async def exporter_carte(*, _: Id = Depends(utilisateur_courant)):
#     # TODO recuperer carte
#
#     # TODO creer fichier
#
#     return fichier  # TODO retourner le fichier
