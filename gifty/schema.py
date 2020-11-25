import graphene
from django.conf import settings

class Query:
    """
    Gifty main queries.
    """
    version = graphene.String(description='Returns the service version!')

    def resolve_version(self, info, **kwargs):
        return settings.VERSION
