#!/usr/bin/env python
# coding=utf-8

import datetime
import logging

from flask import make_response
from flask import request
from flask_restful import Resource

import PermissionMangement.models as models

_logger = logging.getLogger(__name__)


# region API Examples

class Authors(Resource):
    """ Route: /authors """

    def get(self):
        authors = models.Author.query.all()
        result = authors_schema.dump(authors)
        return {'authors': result.data}


class Author(Resource):
    """ Route: /author/<int:pk> """

    def get(self, pk):
        author = models.Author.query.get(pk)
        if author is None:
            _logger.error("ID:%s Author could not be found.", pk)
            return {"message": "Author could not be found."}, 400
        author_result = author_schema.dump(author)
        quotes_result = quotes_schema.dump(author.quotes.all())
        return {'author': author_result.data, 'quotes': quotes_result.data}


class Quotes(Resource):
    """ Route: /quotes """

    def get(self):
        quotes = models.Quote.query.all()
        result = quotes_schema.dump(quotes)
        return {"quotes": result.data}

    def post(self):
        json_data = request.get_json()
        if json_data is None:
            _logger.error("No input data provided")
            return {'message': 'No input data provided'}, 400

        data, errors = quote_schema.load(json_data)
        if errors:
            return make_response(errors, 422)
        first, last = data['author']['first'], data['author']['last']
        author = models.Author.query.filter_by(first=first, last=last).first()
        if author is None:
            models.Author.create(first=first, last=last)
        quote = models.Quote.create(
            content=data['content'],
            author=author,
            posted_at=datetime.datetime.utcnow()
        )
        result = quote_schema.dump(models.Quote.query.get(quote.id))
        return {"message": "Created new quote.",
                "quote": result.data}


class Quote(Resource):
    """ Route: /quote/<int:pk> """

    def get(self, pk):
        quote = models.Quote.query.get(pk)
        if quote is None:
            return {"message": "Quote could not be found."}, 400
        result = quote_schema.dump(quote)
        return {"quote": result.data}

# endregion
