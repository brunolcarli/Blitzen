import graphene
import gifty.schema


class Query(gifty.schema.Query, graphene.ObjectType):
    pass


class Mutation(gifty.schema.Mutation, graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query, mutation=Mutation, auto_camelcase=False)