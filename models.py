#!/usr/bin/env python
# -*- coding: utf-8 -*-
from sqlalchemy import Column, Integer, String, DateTime

from db import Base


class Material(Base):
    __tablename__ = 't_materials'
    id = Column(Integer, primary_key=True, autoincrement=True)
    account_id = Column(String(255), nullable=True)
    category = Column(String(255), nullable=True)
    name = Column(String(255), nullable=True)
    url = Column(String(255), unique=True)
    created_at = Column(DateTime)
    updated_at = Column(DateTime, onupdate=True)

    def __init__(self, account_id=None, category=None, name=None, url=None):
        self.account_id = account_id
        self.category = category
        self.name = name
        self.url = url
