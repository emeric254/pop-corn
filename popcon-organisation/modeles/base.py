# -*- coding: utf-8 -*-

from pydantic import conint

Id = conint(ge=0)
