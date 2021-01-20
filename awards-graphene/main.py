import graphene
import logging
import json
from graphene_federation import build_schema, key, extend, external
from middleware import TracingMiddleware

from flask import Flask
from flask_graphql import GraphQLView

app = Flask(__name__)

@key(fields='awardName year')
class Award(graphene.ObjectType):
    class Meta:
        description = "An award for a work of literature."

    bookTitle = graphene.String(description="The title of the book")
    year = graphene.Int(description="The year the award was given.")
    authorName = graphene.String(description="The author name.")
    awardTitle = graphene.String(description="The title of the award (ie, 'Best Novel').")
    awardName = graphene.String(description="The name of the award (ie, 'Hugo Award').")

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



awards = []
award_data = json.loads(open('awards.json').read())
for award in award_data:
    awards.append(Award(
        bookTitle=award['bookTitle'], 
        year=award['year'], 
        awardName=award['awardName'], 
        awardTitle=award['awardTitle'],
        authorName=award['authorName'] 
    ))

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