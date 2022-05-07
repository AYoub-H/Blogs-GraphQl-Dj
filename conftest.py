from dataclasses import dataclass
from typing import Any

import pytest
from django.conf import settings
from graphene.test import Client

from blogs.graphql.schema import schema
from tests.blogs.factories import UserFactory


@pytest.fixture
def user() -> settings.AUTH_USER_MODEL:
    return UserFactory()


@pytest.fixture
def graphql_client():
    return Client(schema)


@dataclass
class GraphqlContext:
    user: Any


@pytest.fixture
def authenticated_graphql_client(graphql_client, user):
    graphql_client.execute_options["context"] = GraphqlContext(user=user)
    return graphql_client
