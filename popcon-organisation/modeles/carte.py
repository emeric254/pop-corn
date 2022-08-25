# -*- coding: utf-8 -*-

from pydantic import BaseModel


class Zone(BaseModel):
    """
    Une zone de la carte
    """
    nom: str
    description: str


class Carte(BaseModel):
    """
    La carte
    """
    # Dictionaire [ identifiant -> Zone ]
    #   cf. https://stackoverflow.com/questions/60089947/creating-pydantic-model-schema-with-dynamic-key
    __root__: dict[str, Zone]
