# -*- coding: utf-8 -*-

import jwt
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer

from modeles.base import Id

from outils import jwt


oauth2_scheme = OAuth2PasswordBearer(tokenUrl='token')


CREDENTIAL_EXCEPTION: HTTPException = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail='Could not validate credentials',
    headers={'WWW-Authenticate': 'Bearer'},
)


async def utilisateur_courant(jeton: str = Depends(oauth2_scheme)) -> Id:
    """
    Validate that the request of the user is authenticated.

    :param jeton: JWT token given as Bearer inside the request
    :return: user id
    """
    try:
        payload: dict = jwt.verification(jeton=jeton)
    except jwt.PyJWTError:
        raise CREDENTIAL_EXCEPTION

    user: str = (payload.get('sub') or '').replace('user:', '')
    if not user:
        raise CREDENTIAL_EXCEPTION

    try:
        user_id: Id = int(user)
    except ValueError:
        raise CREDENTIAL_EXCEPTION

    return user_id
