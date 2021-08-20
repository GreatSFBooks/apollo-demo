import random

from gql import gql, Client
from gql.transport.requests import RequestsHTTPTransport


client_name = [
    "iOS",
    "web",
    "Android",
]

versions = ['1.0', '1.1', '1.2']

# Select your transport with a defined url endpoint
transport = RequestsHTTPTransport(
    url="https://jll-apollo-test.uc.r.appspot.com/", 
    headers={
        'apollographql-client-name': random.choice(client_name),
        'apollographql-client-version': random.choice(versions)
    }, verify=True, retries=3,
)
# Create a GraphQL client using the defined transport
client = Client(transport=transport, fetch_schema_from_transport=False)

client_types = []
queries = [
gql("query getAwards { awards { awardTitle }}"),
gql("query getAuthors { authors { name }}"),
gql("query getBooks { books { title }}"),
]


for i in range(random.randint(50,100)):
    # Provide a GraphQL query
    query = random.choice(queries)
    print(query)
    # Execute the query on the transport
    result = client.execute(query)
