# -*- coding: utf-8 -*-

import logging
from fastapi import FastAPI
from fastapi.middleware import Middleware
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.gzip import GZipMiddleware
from fastapi.middleware.trustedhost import TrustedHostMiddleware

from api.routers import carte, jeton, planning

from outils import obtenir_configuration

configuration = obtenir_configuration()

logging.basicConfig(
    filename=configuration.logs.chemin_fichier_sortie,
    level=configuration.logs.niveau,
    format=configuration.logs.format
)

uvicorn_logger = logging.getLogger('uvicorn.error')
uvicorn_logger.propagate = False

logger = logging.getLogger(__name__)

middlewares: list[Middleware] = [
    # allow gzip responses
    Middleware(GZipMiddleware),
    # trusted domains
    Middleware(TrustedHostMiddleware, allowed_hosts=(configuration.domaines_autorises or None)),
]

if configuration.cors.autoriser:
    middlewares.append(
        Middleware(
            CORSMiddleware,
            allow_origins=configuration.cors.origines,
            allow_credentials=configuration.cors.identifiants,
            allow_methods=configuration.cors.methodes,
            allow_headers=configuration.cors.entetes,
            expose_headers=configuration.cors.exposer_entetes,
        )
    )

# "uri" pour le proxy inverse et la liste des "domaines_autorises" non vides sont synonymes d'environement de production
PRODUCTION = configuration.uri and configuration.domaines_autorises

app = FastAPI(
    root_path=configuration.uri,
    title='popcon-organisation',
    version='0.0.1',
    servers=[
        {'url': 'http://localhost:8088/', 'description': 'Local environment'},
    ],
    **({'docs_url': None, 'redoc_url': None, } if PRODUCTION else {}),  # documentation
    middleware=middlewares
)

# ajouter les routeurs
app.include_router(carte.routeur)
app.include_router(jeton.routeur)
app.include_router(planning.routeur)

# desactiver la redirection lorsque le '/' en fin d'URL est present ou non
app.router.redirect_slashes = False
