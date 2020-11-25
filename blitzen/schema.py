import graphene
import gifty.schema


class Query(gifty.schema.Query, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query, auto_camelcase=False)