from ariadne import ObjectType, QueryType, gql
from ariadne.contrib.federation import make_federated_schema
from ariadne.contrib.tracing.apollotracing import ApolloTracingExtension
from ariadne.wsgi import GraphQL

# Define types using Schema Definition Language (https://graphql.org/learn/schema/)
# Wrapping string in gql function provides validation and better error traceback
type_defs = gql("""
    type Query {
        awards: [Award!]!
    }

    type Award {
        bookTitle: String
        year: Int
        authorName: String
        awardTitle: String
    }
""")

# Map resolver functions to Query fields using QueryType
query = QueryType()

# Resolvers are simple python functions
@query.field("awards")
def resolve_award(*_):
    return [
        {"bookTitle": "Dune", "year": 1966, "awardName": "Hugo Award", "authorName": "Frank Herbert"},
        {"bookTitle": "Dune", "year": 1966, "awardName": "Nebula Award", "authorName": "Frank Herbert"},
        {"bookTitle": "The Left Hand of Darkness", "year": 1970, "awardName": "Nebula Award", "authorName": "Ursula K. Le Guin"},
    ]


# Map resolver functions to custom type fields using ObjectType
award = ObjectType("Award")

#@person.field("fullName")
#def resolve_person_fullname(person, *_):
#    return "%s %s" % (person["firstName"], person["lastName"])

# Create executable GraphQL schema
schema = make_federated_schema(type_defs, query, award)

# Create an ASGI app using the schema, running in debug mode
app = GraphQL(schema, debug=True, extensions=[ApolloTracingExtension])

