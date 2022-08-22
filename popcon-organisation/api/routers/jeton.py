# -*- coding: utf-8 -*-

import logging
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm

from api.dependances import utilisateur_courant

from logic import compte

from modeles.base import Id
from modeles.jeton import Jeton

from outils import jwt

loguer = logging.getLogger(__name__)

routeur = APIRouter(
    prefix='/jeton',
    tags=['jeton'],
)


@routeur.post(
    '',
    response_model=Jeton,
    responses={
        401: {'description': 'Identifiants invalides'}
    },
)
async def login(*, formulaire: OAuth2PasswordRequestForm = Depends()):
    connexion = compte.connexion(email=formulaire.username, password=formulaire.password)

    if not connexion:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='Email et/ou mot de passe invalide',
            headers={'WWW-Authenticate': 'Bearer'},
        )

    return Jeton(jeton=jwt.nouveau_jeton(user_id=0))


@routeur.get(
    '',
    response_model=Jeton,
    responses={
        401: {'description': 'Jeton invalide'}
    },
)
async def rafraichir_jeton(*, user_id: Id = Depends(utilisateur_courant)):
    # TODO limiter les rafraichissements ?

    return Jeton(jeton=jwt.nouveau_jeton(user_id=user_id))
