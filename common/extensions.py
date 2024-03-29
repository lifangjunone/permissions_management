#!/usr/bin/env python
# coding=utf-8

from celery import Celery
from flask_sqlalchemy import SQLAlchemy
from conf.default import BaseConfig
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from flask_migrate import Migrate

MYSQL_URI = BaseConfig.MYSQL_URI

main_app_create_engine = create_engine(MYSQL_URI, pool_size=30, max_overflow=10, pool_recycle=60 * 3)
Session = scoped_session(sessionmaker(bind=main_app_create_engine))
session_obj = Session()
db = SQLAlchemy()
celery = Celery()
migrate = Migrate()
