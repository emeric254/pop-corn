# -*- coding: utf-8 -*-

from jwt import PyJWTError
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer

from modeles.base import Id

from outils import jwt


oauth2_scheme = OAuth2PasswordBearer(tokenUrl='jeton')


EXCEPTION_IDENTIFIANTS: HTTPException = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail='Identifiants impossibles a verifier',
    headers={'WWW-Authenticate': 'Bearer'},
)


async def utilisateur_courant(jeton: str = Depends(oauth2_scheme)) -> Id:
    """
    Validate that the request of the user is authenticated.

    :param jeton: JWT token given as Bearer inside the request
    :return: user id
    """
    try:
        print('ok')
        payload: dict = jwt.verification(jeton=jeton)
        print('ok')
    except PyJWTError as e:
        print(e)
        raise EXCEPTION_IDENTIFIANTS

    user: str = (payload.get('sub') or '').replace('user:', '')
    if not user:
        print('prout')
        raise EXCEPTION_IDENTIFIANTS

    try:
        user_id: Id = int(user)
        print('caca')
    except ValueError:
        raise EXCEPTION_IDENTIFIANTS

    return user_id
