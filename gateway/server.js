import { ApolloGateway } from "@apollo/gateway";
import { ApolloServer } from "apollo-server";


const PORT = process.env.PORT || 4000;

const gateway = new ApolloGateway({
  serviceList: [
    { name: "awards", url: "https://awards-dot-jll-apollo-test.uc.r.appspot.com" },
    { name: "authors", url: "https://authors-dot-jll-apollo-test.uc.r.appspot.com/query" },
    { name: "books", url: "https://books-dot-jll-apollo-test.uc.r.appspot.com" },
  ]
});

const server = new ApolloServer({
  gateway,
  playground: true,
  subscriptions: false
});

server.listen({ port: PORT }).then(({ url }) => {
  console.log(`Server ready at ${url}`);
});