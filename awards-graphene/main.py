import graphene
from graphene_federation import build_schema
from middleware import TracingMiddleware

from flask import Flask
from flask_graphql import GraphQLView

app = Flask(__name__)


class Award(graphene.ObjectType):
    bookTitle = graphene.String()
    year = graphene.Int()
    authorName = graphene.String()
    awardTitle = graphene.String()
    awardName = graphene.String()


awards = [
    Award(bookTitle= "Dune", year= 1966, awardName="Hugo Award", authorName= "Frank Herbert"),
    Award(bookTitle= "Dune", year= 1966, awardName= "Nebula Award", authorName="Frank Herbert"),
    Award(bookTitle= "The Left Hand of Darkness", year= 1970, awardName= "Nebula Award", authorName="Ursula K. Le Guin"),
]


class Query(graphene.ObjectType):

    awards = graphene.List(Award)

    def resolve_awards(root, info):
        return awards


schema = build_schema(Query)


app.add_url_rule('/', view_func=GraphQLView.as_view(
    'graphql',
    schema=schema,
    graphiql=True,
    debug=True
    #middleware=[TracingMiddleware()]
))

# Optional, for adding batch query support (used in Apollo-Client)
app.add_url_rule('/graphql/batch', view_func=GraphQLView.as_view(
    'graphql_batch',
    schema=schema,
    batch=True,
    debug=True
))

if __name__ == '__main__':
    app.run()