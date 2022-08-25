# -*- coding: utf-8 -*-

import datetime
from pydantic import BaseModel


class Evenement(BaseModel):
    """
    Un evenement
    """
    nom: str
    description: str
    mots_clef: list[str]
    debut: datetime.datetime
    duree: datetime.timedelta
    zone: str


class Planning(BaseModel):
    """
    Le planning
    """
    # Dictionaire [ identifiant -> Evenement ]
    #   cf. https://stackoverflow.com/questions/60089947/creating-pydantic-model-schema-with-dynamic-key
    __root__: dict[str, Evenement]
