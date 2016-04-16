#!/usr/bin/env python
# -*- coding: utf-8 -*-
# http://yuizho.hatenablog.com/entry/2013/06/26/012044
# http://d.hatena.ne.jp/heavenshell/20151011/1444546659
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker
import yaml


# debug用の__repr__を各モデルに書かなくてよくなる設定
class RepresentableBase(object):
    def __repr__(self):
        """Dump all columns and value automagically.

        This code is copied a lot from followings.
        See also:
           - https://gist.github.com/exhuma/5935162#file-representable_base-py
           - http://stackoverflow.com/a/15929677
        """

        #: Columns.
        columns = ', '.join(
            ['{0}={1}'.format(k, repr(self.__dict__[k])) for k in self.__dict__.keys() if k[0] != '_']
        )

        return '<{0}({1})>'.format(
            self.__class__.__name__, columns
        )


with open('./settings.yml') as fin:
    text = fin.read()
conf = yaml.load(text)

engine = create_engine(conf['database'], encoding='utf-8', echo=True)
db_session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))

Base = declarative_base(cls=RepresentableBase)
Base.query = db_session.query_property()


def init_db():
    Base.metadata.create_all(bind=engine)
