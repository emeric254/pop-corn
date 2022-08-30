# -*- coding: utf-8 -*-

from pydantic import BaseModel


class Zone(BaseModel):
    """
    Une zone de la carte
    """
    id: str
    nom: str
    description: str = ''


class Carte(BaseModel):
    """
    La carte
    """
    zones: dict[str, Zone] = {}
