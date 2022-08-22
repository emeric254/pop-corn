# -*- coding: utf-8 -*-

import jwt
import datetime

from modeles.base import Id

from outils import obtenir_configuration

configuration = obtenir_configuration()


with open(configuration.jwt.chemin_clef_privee, mode='r') as fichier:
    CLEF_PRIVEE = fichier.read()
with open(configuration.jwt.chemin_clef_publique, mode='r') as fichier:
    CLEF_PUBLIQUE = fichier.read()


def nouveau_jeton(user_id: Id) -> str:
    """
    Creer un nouveau jeton d'authentification pour un utilisateur.

    :param user_id: numero de l'utilisateur
    :return: un nouveau jeton d'authentification pour cet utilisateur
    """
    now: datetime.datetime = datetime.datetime.now().astimezone()
    expiration: datetime.datetime = now + datetime.timedelta(seconds=configuration.jwt.expiration)

    token: str = jwt.encode(
        payload={
            'iat': now,  # issued at
            'nbf': now,  # not before time
            'exp': expiration,  # expiration time
            'sub': f'user:{user_id}',  # subject
            'iss': 'popcon-organisation',  # issuer
            'aud': ['popcon-organisation', ],  # audience
        },
        key=CLEF_PRIVEE,
        algorithm=configuration.jwt.algorithme
    )
    return token


def verification(jeton: str) -> dict:
    """
    Verifie un jeton d'authentification.

    :param jeton: JWT token to verify and read
    :return: details et donnees contenus par le jeton
    :raise DecodeError: le jeton n'est pas valide
    """
    return jwt.decode(
        jwt=jeton,
        key=CLEF_PUBLIQUE,
        algorithms=[configuration.jwt.algorithme],
        # claims validation
        leeway=datetime.timedelta(seconds=configuration.jwt.marge_expiration),
        issuer='popcon-organisation',
        audience='popcon-organisation',
        options={
            'require': ['iat', 'nbf', 'exp', 'sub', 'iss', 'aud', ],
            'verify_iat': True,
            'verify_nbf': True,
            'verify_exp': True,
            'verify_iss': True,
            'verify_aud': True,
        }
    )
