# -*- coding: utf-8 -*-

from typing import Literal

from pydantic import BaseSettings, BaseModel, Field, EmailStr, SecretStr, Json, FilePath, DirectoryPath, AnyHttpUrl
from functools import lru_cache



NiveauSortie = Literal['CRITICAL', 'ERROR', 'WARNING', 'INFO', 'DEBUG', 'NOTSET']


class Logs(BaseModel):
    chemin_fichier_sortie: FilePath | None = None
    niveau: NiveauSortie = 'INFO'
    format: str = '%(asctime)s - %(name)s [%(levelname)s] %(message)s'


class CORS(BaseModel):
    autoriser: bool = True
    origines: Json[list[AnyHttpUrl | Literal['*']]] = [
        'https://mobile.popcon.show',  # prod
        'http://localhost:8080',  # popcon-compagnon en local
        'http://localhost:8088',  # popcon-organisation en local
    ]
    identifiants: bool = True
    methodes: Json[list[str]] = ['*', ]
    entetes: Json[list[str]] = ['*', ]
    exposer_entetes: Json[list[str]] = ['*', ]


class JWT(BaseModel):
    algorithme: str = 'EdDSA'
    expiration: int = Field(default=60*60, ge=30, le=24*60*60)  # secondes, minimum 30 secondes, maximum 1 jour
    marge_expiration: int = Field(default=30, ge=0, le=60)  # secondes, minimum 0 seconde, maximum 1 minute
    chemin_clef_privee: FilePath = './jwt.key'
    chemin_clef_publique: FilePath = './jwt.key.pub'


class Identifiants(BaseModel):
    email: EmailStr = ''
    mot_de_passe: SecretStr = ''


class Configuration(BaseSettings):
    uri: str = ''
    chemin_dossier_donnees: DirectoryPath = './donnees/'
    logs = Logs()
    cors = CORS()
    jwt = JWT()
    identifiants = Identifiants()
    domaines_autorises: list[str] = ['mobile.popcon.show', ]

    class Config:
        env_file = 'configuration.env'
        anystr_strip_whitespace = True
        env_nested_delimiter = '__'


@lru_cache()
def obtenir_configuration():
    """
    Retourne la configuration.

    Charge la configuration au premier appel de cette methode et garde en cache le resultat pour les prochains appels.
    cf. https://docs.python.org/3/library/functools.html#functools.lru_cache

    :return: configuration
    """
    return Configuration()
