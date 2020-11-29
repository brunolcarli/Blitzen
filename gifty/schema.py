import graphene
from django.conf import settings
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField
from gifty.models import (Ong, FederalPublicUtilityCertificate, 
                          StatePublicUtilityCertificate,
                          MunicipalPublicUtilityCertificate)


##########################################################################
# Object types
##########################################################################
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


class ONGType(DjangoObjectType):
    """
    Defines a GraphQL structure for an `ONG`.
    """
    class Meta:
        model = Ong
        interfaces = (graphene.relay.Node,)
        filter_fields = {
            'name': ['exact', 'icontains', 'in'],
            'cnas': ['exact', 'in'],
            'federal_public_utility_certificate__cnpj': ['exact', 'in'],
            'federal_public_utility_certificate__mj_process': ['exact', 'in'],
            'state_public_utility_certificate__cnpj': ['exact', 'in'],
            'state_public_utility_certificate__mj_process': ['exact', 'in'],
            'municipal_public_utility_certificate__cnpj': ['exact', 'in'],
            'municipal_public_utility_certificate__mj_process': ['exact', 'in'],
            'phone_contact': ['exact', 'in'],
            'address': ['exact', 'in', 'icontains'],
            'country': ['exact', 'in', 'icontains'],
            'state': ['exact', 'in', 'icontains'],
            'city': ['exact', 'in', 'icontains'],
        }

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
    geolocation = graphene.Field(
        GeolocationType,
        description='ONG location points'
    )
    description = graphene.String(description='ONG description.')
    donation_link = graphene.String(
        description='Link for donation contributions.'
    )

    def resolve_cnas(self, info, **kwargs):
        return CNASType(registration_number=self.cnas)

    def resolve_geolocation(self, info, **kwargs):
        return GeolocationType(latitude=self.latitude, longitude=self.longitude)


##########################################################################
# InputTypes, Relay COnnections and other schema support stuff
##########################################################################
class ONGConnection(graphene.relay.Connection):
    class Meta:
        node = ONGType

    nodes = graphene.List(ONGType)
    count = graphene.Int(description='Number of registered elements.')
    total = graphene.Int(description='Total number of registered elements.')

    def resolve_nodes(self, info, **kwargs):
        return [item.node for item in self.edges]

    def resolve_count(self, info, **kwargs):
        return len(self.edges)

    def resolve_total(self, info, **kwargs):
        return len(self.iterable)


class GeolocationInput(graphene.InputObjectType):
    latitude = graphene.Float(description='Latitude value.')
    longitude = graphene.Float(description='Longitude value.')


class FederalPublicUtilityCertificateInput(graphene.InputObjectType):
    cnpj = graphene.String(description='CNPJ registration number.')
    mj_process = graphene.String(description='MJ process number.')


class StatePublicUtilityCertificateInput(graphene.InputObjectType):
    cnpj = graphene.String(description='CNPJ registration number.')
    mj_process = graphene.String(description='MJ process number.')


class MunicipalPublicUtilityCertificateInput(graphene.InputObjectType):
    cnpj = graphene.String(description='CNPJ registration number.')
    mj_process = graphene.String(description='MJ process number.')


##########################################################################
# QUERY
##########################################################################
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
    ongs = DjangoFilterConnectionField(
        ONGType,
        orderBy=graphene.String(description='Order results by field name.')
    )

    def resolve_ongs(self, info, **kwargs):
        ordenation = kwargs.pop('orderBy', 'id')  # id is default

        if not kwargs:
            return Ong.objects.all().order_by(ordenation)

        return Ong.objects.filter(**kwargs).order_by(ordenation)


##########################################################################
# MUTATIONS
##########################################################################
class CreateOng(graphene.relay.ClientIDMutation):
    """
    Creates a ong on database.
    """
    ong = graphene.Field(
        ONGType,
        description='Created ong data response.'
    )
    class Input:
        name = graphene.String(
            description='Ong name.',
            required=True
        )
        # TODO: add descriptions
        cnas_registration_number = graphene.String(required=True)
        phone_contact = graphene.String(required=True)
        address = graphene.String(
            required=True,
            description='ONG location address.'
        )
        country = graphene.String(
            required=True,
            description='Country name.'
        )
        state = graphene.String(
            required=True,
            description='State name.'
        )
        city = graphene.String(
            required=True,
            description='City name'
        )
        geolocation = graphene.Argument(
            GeolocationInput,
            required=True
        )
        federal_public_utility_certificate = graphene.Argument(
            FederalPublicUtilityCertificateInput,
            required=True
        )
        state_public_utility_certificate = graphene.Argument(
            FederalPublicUtilityCertificateInput,
            required=True
        )
        municipal_public_utility_certificate = graphene.Argument(
            MunicipalPublicUtilityCertificateInput,
            required=True
        )
        description=graphene.String()
        donation_link=graphene.String()


    # @access_required  # TODO: authentication
    def mutate_and_get_payload(self, info, **kwargs):
        geolocation = kwargs.get('geolocation',  {})

        # create the certificate first
        try:
            federal_certificate = FederalPublicUtilityCertificate(
                **kwargs.get('federal_public_utility_certificate', {})
            )
        except Exception as exception:  # TODO write a better handler
            raise Exception(exception)

        try:
            state_certificate = StatePublicUtilityCertificate(
                **kwargs.get('state_public_utility_certificate', {})
            )
        except Exception as exception:  # TODO write a better handler
            raise Exception(exception)

        try:
            municipal_certificate = MunicipalPublicUtilityCertificate(
                **kwargs.get('municipal_public_utility_certificate', {})
            )
        except Exception as exception:  # TODO write a better handler
            raise Exception(exception)

        federal_certificate.save()
        state_certificate.save()
        municipal_certificate.save()

        try:
            ong = Ong.objects.create(
                name=kwargs.get('name'),
                cnas=kwargs.get('cnas_registration_number'),
                phone_contact=kwargs.get('phone_contact'),
                address=kwargs.get('address'),
                country=kwargs.get('country'),
                state=kwargs.get('state'),
                city=kwargs.get('city'),
                latitude=geolocation.get('latitude'),
                longitude=geolocation.get('longitude'),
                federal_public_utility_certificate=federal_certificate,
                state_public_utility_certificate=state_certificate,
                municipal_public_utility_certificate=municipal_certificate,
                description=kwargs.get('description'),
                donation_link=kwargs.get('donation_link')
            )

        except Exception as exception:
            raise(exception)

        ong.save()

        return CreateOng(ong)


class Mutation:
    create_ong = CreateOng.Field()
