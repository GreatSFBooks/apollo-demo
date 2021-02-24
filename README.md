# Apollo Demo

Federated schema with 3 services:

 * authors/ - using GQLGen (GoLang)
 * awards-graphene/ - using Graphene (Python)
 * books/ - using Apollo Service (JS)

## Setup (local)

Add `.env` files in each service, gateway, and clients directory as documented here:
    https://www.apollographql.com/docs/tutorial/production/#set-environment-variables

Run `npm install` for the NodeJS projects. 

## Deployment

In each service:

```make deploy```

