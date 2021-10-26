import { ApolloGateway, RemoteGraphQLDataSource } from "@apollo/gateway";
import { ApolloServer } from "apollo-server";
import { bootstrap } from 'global-agent';
import { ApolloServerPluginInlineTrace } from "apollo-server-core";
import  dotenv  from "dotenv";
import fetch from "make-fetch-happen";

//console.log(process.env.GLOBAL_AGENT_HTTP_PROXY);
//console.log(process.env.GLOBAL_AGENT_HTTPS_PROXY);
//bootstrap();

class AuthenticatedDataSource extends RemoteGraphQLDataSource {
  willSendRequest({ request, context }) {
    request.http.headers.set('apiKey', 'Y7Lp2iwJqbw3WwqT7lqhGBFIrrVB7NodeKYkD4VXTQsZMPJ0n0fnsQ5w1VT7DpzC');
  }
}

dotenv.config();

const PORT = process.env.PORT || 4000;
const APOLLO_KEY = process.env.APOLLO_KEY;

//global.GLOBAL_AGENT.HTTP_PROXY = 'https://127.0.0.1:9090';

const gateway = new ApolloGateway({
  buildService({ name, url }) {
    return new AuthenticatedDataSource({ url });
  },
});

const server = new ApolloServer({
  gateway,
  context: ({ req }) => {
    // Get the Mongo API Key from the headers
    const apiKey = req.headers.apiKey || '';
    return { apiKey };
  },
  debug: false,
  introspection: false, // Not for prod
  playground: false, // Not for prod
  subscriptions: false,
  
  //logger: logger,
  plugins: [ApolloServerPluginInlineTrace()]
});

server.listen({ port: PORT }).then(({ url }) => {
  console.log(`Server ready at ${url}`);
}); 