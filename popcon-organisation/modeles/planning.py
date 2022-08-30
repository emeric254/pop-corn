# -*- coding: utf-8 -*-

import datetime
from pydantic import BaseModel


class Activite(BaseModel):
    """
    Un evenement
    """
    nom: str
    description: str = ''
    mots_clef: list[str] = []
    debut: datetime.datetime
    duree: datetime.timedelta
    zone: str = ''


class Planning(BaseModel):
    """
    Le planning
    """
    activites: dict[str, Activite] = {}
