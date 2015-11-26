# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import os
from pyramid.config import Configurator
from pyramid.view import view_config
from waitress import serve
import sqlalchemy as sa
from sqlalchemy import create_engine
from sqlalchemy import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import datetime
from sqlalchemy.orm import scoped_session, sessionmaker
from zope.sqlalchemy import ZopeTransactionExtension

DBSession = scoped_session(sessionmaker(extension=ZopeTransactionExtension()))

Base = declarative_base()

DATABASE_URL = os.environ.get (
    'DATABASE_URL',
    'postgresql://jens_mac:W1ck3ed1!@localhost:5432/learning-journal'
)

class Entry(Base):
    __tablename__ = 'entries'
    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    title = sa.Column(sa.Unicode(127), nullable=False)
    text = sa.Column(sa.UnicodeText, nullable=False)
    created = sa.Column(
        sa.DateTime, nullable=False, default=datetime.datetime.utcnow
    )

def init_db():
    engine = sa.create_engine(DATABASE_URL)
    Base.metadata.create_all(engine)

@view_config(route_name='home', renderer='string')
def home(request):
    return "Hello World"


def main():
    """Create a configured wsgi app"""
    settings = {}
    debug = os.environ.get('DEBUG', True)
    settings['reload_all'] = debug
    settings['debug_all'] = debug
    if not os.environ.get('TESTING', False):
<<<<<<< HEAD
	# only bind the session if we are not testing
	engine = sa.create_engine(DATABASE_URL)
 	DBSession.configure(bind=engine)
=======
        # only bind the session if we are not testing
        engine = sa.create_engine(DATABASE_URL)
        DBSession.configure(bind=engine)
>>>>>>> 6166a9364650673c84d7b540f28eabf36491b387
    # configuration setup
    config = Configurator(
        settings=settings
    )
    config.include('pyramid_tm')
    config.add_route('home', '/')
    config.scan()
    app = config.make_wsgi_app()
    return app


if __name__ == '__main__':
    app = main()
    
    port = os.environ.get('PORT', 5000)
    serve(app, host='0.0.0.0', port=port)
