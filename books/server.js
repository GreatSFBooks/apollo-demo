const { ApolloServer, gql } = require('apollo-server');
const { buildFederatedSchema } = require('@apollo/federation');

const dotenv = require('dotenv');
const bunyan = require('bunyan');

// Imports the Google Cloud client library for Bunyan
const {LoggingBunyan} = require('@google-cloud/logging-bunyan');

// Creates a Bunyan Cloud Logging client
const loggingBunyan = new LoggingBunyan();

// Create a Bunyan logger that streams to Cloud Logging
// Logs will be written to: "projects/YOUR_PROJECT_ID/logs/bunyan_log"
const logger = bunyan.createLogger({
  // The JSON payload of the log as it appears in Cloud Logging
  // will contain "name": "my-service"
  name: 'book-service',
  streams: [
    // Log to the console at 'info' and above
    {stream: process.stdout, level: 'info'},
    // And log to Cloud Logging, logging at 'info' and above
    loggingBunyan.stream('info'),
  ],
});

dotenv.config();

// A schema is a collection of type definitions (hence "typeDefs")
// that together define the "shape" of queries that are executed against
// your data.
const typeDefs = gql`
  # Comments in GraphQL strings (such as this one) start with the hash (#) symbol.

  # This "Book" type defines the queryable fields for every book in our data source.
  " A book (work of literature)."
  type Book @key(fields: "title") @key(fields: "author") {
    " The title of the book. "
    title: String
    author: String
    publisher: String
    published_date: String
  }

  extend type Author @key(fields: "name") {
    name: String! @external
    books: [Book]
  }

  # The "Query" type is special: it lists all of the available queries that
  # clients can execute, along with the return type for each. In this
  # case, the "books" query returns an array of zero or more Books (defined above).
  type Query {
    books: [Book]
  }
`;

const books = require('./books.json');

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
  schema: buildFederatedSchema([{ typeDefs, resolvers }])
});

const PORT = process.env.PORT || 8080;

// The `listen` method launches a web server.
server.listen({port:PORT}).then(({ url }) => {
  console.log(`🚀  Server ready at ${url}`);
});
