import { ApolloGateway } from "@apollo/gateway";
import { ApolloServer } from "apollo-server";
import { createLogger } from "bunyan";
import { LoggingBunyan } from "@google-cloud/logging-bunyan";
import { ApolloServerPluginInlineTrace } from "apollo-server-core";

// Creates a Bunyan Cloud Logging client
const loggingBunyan = new LoggingBunyan();

// Create a Bunyan logger that streams to Cloud Logging
// Logs will be written to: "projects/YOUR_PROJECT_ID/logs/bunyan_log"
const logger = createLogger({
  // The JSON payload of the log as it appears in Cloud Logging
  // will contain "name": "my-service"
  name: 'apollo-gateway',
  streams: [
    // Log to the console at 'info' and above
    {stream: process.stdout, level: 'info'},
    // And log to Cloud Logging, logging at 'info' and above
    loggingBunyan.stream('info'),
  ],
});

const PORT = process.env.PORT || 4000;

const gateway = new ApolloGateway(/*{
  serviceList: [
    { name: "awards", url: "https://awards-dot-jll-apollo-test.uc.r.appspot.com" },
    { name: "authors", url: "https://authors-dot-jll-apollo-test.uc.r.appspot.com/query" },
    { name: "books", url: "https://books-dot-jll-apollo-test.uc.r.appspot.com" },
  ]
}*/);

const server = new ApolloServer({
  gateway,
  debug:true,
  introspection: true, // Not for prod
  playground:true, // Not for prod
  subscriptions: false,
  logger: logger
});

server.listen({ port: PORT }).then(({ url }) => {
  console.log(`Server ready at ${url}`);
}); 