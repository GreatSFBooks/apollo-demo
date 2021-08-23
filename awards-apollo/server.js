const fs = require('fs');
const { ApolloServer, gql } = require('apollo-server');
const { buildFederatedSchema } = require('@apollo/federation');
const { ApolloServerPluginInlineTrace } = require('apollo-server-core');

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
  name: 'awards-service',
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
const typeDefs = gql(fs.readFileSync('schema.graphql', 'utf8'))

const awards = require('./awards.json');

function fetchAwardsForAuthor(author) {
  //logger.info('Fetch awards for author: ' + author);
  //logger.info(awards);
  var awardsFound = [];
  for (var i = 0; i < awards.length; i++) {
    if (awards[i].authorName === author) {
        awardsFound.push(awards[i]);
    } 
  }
  //logger.info("Books found: " + awardsFound.length);
  return awardsFound;
}
  
// Resolvers define the technique for fetching the types defined in the
// schema. This resolver retrieves awards from the "awards" array above.
const resolvers = {
    Query: {
      awards: () => awards,
    },
    Author: {
      awards(author) {
        return fetchAwardsForAuthor(author.name);
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
