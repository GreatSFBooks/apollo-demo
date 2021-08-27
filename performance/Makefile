test:
	APOLLO_KEY=service:Performance-Testing:aHO8QcP2o41mf1CgBSKdwA \
  		rover subgraph publish Performance-Testing@current \
  		--name backend --schema server/schema.graphql --convert \
  		--routing-url http://server:8080/
	docker-compose --env-file .env up

siege:
	ab -n 4000 -c 5  -T "application/json" -p gql_post.json http://localhost:10100/

siegegw:
	ab -n 4000 -c 5  -T "application/json" -p gql_post.json http://localhost:10101/
	