const fs = require('fs');
const { ApolloServer, gql } = require('apollo-server');
const { buildFederatedSchema } = require('@apollo/federation');
const { ApolloServerPluginInlineTrace } = require('apollo-server-core');

const dotenv = require('dotenv');

dotenv.config();

// A schema is a collection of type definitions (hence "typeDefs")
// that together define the "shape" of queries that are executed against
// your data.
const typeDefs = gql(fs.readFileSync('schema.graphql', 'utf8'))

const books = require('./data.json');

function fetchBooksForAuthor(author) {
  //logger.info('Fetch books for author: ' + author);
  //logger.info(books);
  var booksFound = [];
  for (var i = 0; i < books.length; i++) {
    if (books[i].author === author) {
      booksFound.push(books[i]);
    } 
  }
  //logger.info("Books found: " + booksFound.length);
  return booksFound;
}
  
// Resolvers define the technique for fetching the types defined in the
// schema. This resolver retrieves books from the "books" array above.
const resolvers = {
    Query: {
      books: () => books,
    },
    Author: {
      books(author) {
        return fetchBooksForAuthor(author.name);
      }
    }
  };
  
// The ApolloServer constructor requires two parameters: your schema
// definition and your set of resolvers.
const server = new ApolloServer({ 
  schema: buildFederatedSchema([{ typeDefs, resolvers }]),
  plugins: [ApolloServerPluginInlineTrace()]
});

const PORT = process.env.PORT || 8080;

// The `listen` method launches a web server.
server.listen({port:PORT}).then(({ url }) => {
  console.log(`🚀  Server ready at ${url}`);
});
