# -*- coding: utf-8 -*-

import logging

from modeles.base import Id

from outils import obtenir_configuration

configuration = obtenir_configuration()

logger = logging.getLogger(__name__)


def connexion(email: str, password: str) -> Id:
    """
    Tentative de connexion d'un utilisateur.

    :param email: email de l'utilisateur
    :param password: mot de passe de l'utilisateur
    :return: True si la connexion est reussie, sinon False
    """

    if not all([configuration.identifiants.email, configuration.identifiants.mot_de_passe]):
        logger.error('Identifiants invalides dans la configuration')
        return False

    if not configuration.identifiants.email == email:
        return False

    return configuration.identifiants.mot_de_passe.get_secret_value() == password
