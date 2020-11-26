import graphene
from django.conf import settings


class CNASType(graphene.ObjectType):
    """
    Defines a CNAS register GraphQL structure.
    CNAS stands for `Conselho Nacional de Assistência Social`
                     (National Social Assistance Council)
    """
    registration_number = graphene.String(description='Registration number.')


class FederalPublicUtilityCertificateType(graphene.ObjectType):
    """
    Defines a Federal Public Utility Certificate Graphql structure
    """
    cnpj = graphene.String(description='CNPJ registration number.')
    mj_process = graphene.String(description='MJ process number.')


class StatePublicUtilityCertificateType(graphene.ObjectType):
    """
    Defines a State Public Utility Certificate Graphql structure
    """
    cnpj = graphene.String(description='CNPJ registration number.')
    mj_process = graphene.String(description='MJ process number.')


class MunicipalPublicUtilityCertificateType(graphene.ObjectType):
    """
    Defines a Municipal Public Utility Certificate Graphql structure
    """
    cnpj = graphene.String(description='CNPJ registration number.')
    mj_process = graphene.String(description='MJ process number.')


class GeolocationType(graphene.ObjectType):
    """
    Defines a Geolocation GraphQL structure.,
    """
    latitude = graphene.Float(description='Latitude value.')
    longitude = graphene.Float(description='Longitude value.')

class ONGType(graphene.ObjectType):
    """
    Defines a GraphQL structure for an `ONG`.
    """
    class Meta:
        interfaces = (graphene.relay.Node,)

    name = graphene.String(description='ONG name or reference.')
    cnas = graphene.Field(CNASType, description='CNAS register number')
    federal_public_utility_certificate = graphene.Field(
        FederalPublicUtilityCertificateType,
        description='Federal Public Utility Certificate register.'
    )
    state_public_utility_certificate = graphene.Field(
        StatePublicUtilityCertificateType,
        description='State Public Utility Certificate register.'
    )
    municipal_public_utility_certificate = graphene.Field(
        MunicipalPublicUtilityCertificateType,
        description='Municipal Public Utility Certificate register.'
    )
    phone_contact = graphene.String(description='Phone contact number.')
    address = graphene.String(description='ONG location address.')
    country = graphene.String(description='Country name.')
    state = graphene.String(description='State name.')
    city = graphene.String(description='City name')
    description = graphene.String(description='ONG description.')


class ONGConnection(graphene.relay.Connection):
    class Meta:
        node = ONGType

class Query:
    """
    Gifty main queries.
    """
    node = graphene.relay.Node.Field()

    # Version
    version = graphene.String(description='Returns the service version!')

    def resolve_version(self, info, **kwargs):
        return settings.VERSION

    # ONGs
    ongs = graphene.relay.ConnectionField(ONGConnection)

    def resolve_ongs(self, info, *kwargs):
        return [ONGType()]

