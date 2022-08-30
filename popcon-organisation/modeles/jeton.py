# -*- coding: utf-8 -*-

from pydantic import BaseModel


class Jeton(BaseModel):
    """
    Jeton tel qu'il est retourne par l'api
    """
    access_token: str
    token_type: str = 'Bearer'
