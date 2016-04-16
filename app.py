#!/usr/bin/env python
# -*- coding: utf-8 -*-

from db import db_session, init_db
from models import Material

if __name__ == '__main__':
    init_db()

    material = Material(category='stage', url='xxx')
    db_session.add(material)
    db_session.flush()  # 同期
    db_session.commit()  # 書き込み
    print(material)

    materials = db_session.query(Material).all()
    print(materials)
