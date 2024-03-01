#!/usr/bin/env python
# coding=utf-8
import json

import pytest

from Ipid import models, db
from tests.configtest import app


@pytest.mark.usefixtures('live_server')
class TestLiveServerQuote:
    @pytest.mark.usefixtures('app')
    @pytest.fixture
    def setup_quotes(self, client):
        d = json.dumps({'author': 'Tim Peters', 'content': 'Beautiful is better than ugly.'})
        res = client.post('/api/v2/quotes', data=d,
                          content_type='application/json')
        print(res.json)
        assert res.status_code == 200

        d = json.dumps({'author': 'Peter Hintjens', 'content': 'Simplicity is always better than functionality.'})
        res = client.post('/api/v2/quotes', data=d,
                          content_type='application/json')
        print(res.json)
        assert res.status_code == 200

        one_author = models.Author.query.filter_by(first='Tim').first()
        one_author.update(commit=True, first='jizhen')
        assert models.Author.query.filter_by(first='jizhen').first().first == 'jizhen'

    @pytest.mark.usefixtures('setup_quotes')
    def test_quotes(self, client):
        target_res = {"quotes": [{"content": "Beautiful is better than ugly.", "id": 1},
                                 {"content": "Simplicity is always better than functionality.", "id": 2}
                                 ]}
        res = client.get('/api/v2/quotes')

        assert res.json == target_res
