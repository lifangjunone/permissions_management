#!/usr/bin/env python
# coding=utf-8

import os

from flask_migrate import Migrate
from flask.cli import FlaskGroup
from common.extensions import celery
from PermissionMangement import create_app, db, init_celery
from conf.default import BaseConfig

app = create_app(os.getenv('ENVIRONMENT', BaseConfig.ENV))
init_celery(app, celery)
migrate = Migrate(app, db)

cli = FlaskGroup(app)


@cli.command("db")
def db_command():
    """Perform database migrations."""


@cli.command("runserver")
def runserver_command():
    """Start the Flask development server."""
    host = app.config['SERVER_HOST']
    port = app.config['SERVER_PORT']
    use_debugger = app.config['DEBUG']
    use_reloader = app.config['USE_RELOADER']
    app.run(host=host, port=port, debug=use_debugger, use_reloader=use_reloader)


@cli.command("create_db")
def create_db():
    db.create_all()


if __name__ == '__main__':
    cli()
