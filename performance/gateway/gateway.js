import { ApolloGateway, RemoteGraphQLDataSource } from "@apollo/gateway";
import { ApolloServer } from "apollo-server";
import  dotenv  from "dotenv";

dotenv.config();

const PORT = process.env.PORT || 4000;
const APOLLO_KEY = process.env.APOLLO_KEY || 4000;

const gateway = new ApolloGateway();

const server = new ApolloServer({
  gateway,
  debug: true,
  introspection: true, // Not for prod
  playground: true, // Not for prod
  subscriptions: false,
});

server.listen({ port: PORT }).then(({ url }) => {
  console.log(`Server ready at ${url}`);
}); 