from graphql_auth.settings import DEFAULTS

GRAPHENE = {
    "SCHEMA": "graphQL.schema.schema",
    'MIDDLEWARE': [
        'graphql_jwt.middleware.JSONWebTokenMiddleware',
    ],
}
AUTHENTICATION_BACKENDS = [
    "graphql_jwt.backends.JSONWebTokenBackend",
    "django.contrib.auth.backends.ModelBackend",
]


DEFAULTS['LOGIN_ALLOWED_FIELDS'] = ['email']
DEFAULTS['REGISTER_MUTATION_FIELDS'] = ['email']
DEFAULTS['USER_NODE_FILTER_FIELDS'] = {
    'email': ['exact'],
    'is_active': ['exact'],
    'status__archived': ['exact'],
    'status__verified': ['exact'],
    'status__secondary_email': ['exact'],
}
GRAPHQL_AUTH = DEFAULTS
