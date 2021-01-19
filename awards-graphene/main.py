import graphene
import logging
from graphene_federation import build_schema, key, extend, external
from middleware import TracingMiddleware

from flask import Flask
from flask_graphql import GraphQLView

app = Flask(__name__)

@key(fields='awardName year')
class Award(graphene.ObjectType):
    bookTitle = graphene.String()
    year = graphene.Int()
    authorName = graphene.String()
    awardTitle = graphene.String()
    awardName = graphene.String()

@extend(fields='name')
class Author(graphene.ObjectType):
    name = external(graphene.String(required=True))
    awards = graphene.List(Award)

    def resolve_awards(parent, info):
        logging.error(parent)
        logging.error(info)
        author_awards = []
        for a in awards:
            if a.authorName == parent.name:
                author_awards.append(a)
        return author_awards



awards = [
    Award(bookTitle= "Dune", year= 1966, awardName="Hugo Award", authorName= "Frank Herbert"),
    Award(bookTitle= "Dune", year= 1966, awardName= "Nebula Award", authorName="Frank Herbert"),
    Award(bookTitle= "The Left Hand of Darkness", year= 1970, awardName= "Nebula Award", authorName="Ursula K. Le Guin"),
]


class Query(graphene.ObjectType):

    awards = graphene.List(Award)

    def resolve_awards(root, info):
        return awards




schema = build_schema(Query, types=[Author])


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