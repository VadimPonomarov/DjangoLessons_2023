REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'configs.extra_conf.pagination.CustomPagination',
    'DEFAULT_FILTER_BACKEND': ['django_filters.rest_framework.DjangoFilterBackend']
}
