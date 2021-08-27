register-service:
	apollo service:push \
	--localSchemaFile=./graph/schema.graphqls \
	--graph=jesse-test-1xc6kq \
	--variant=current \
	--serviceName=authors \
	--serviceURL=https://authors-dot-jll-apollo-test.uc.r.appspot.com/query

publish:
	rover subgraph publish jesse-test-1xc6kq@current --schema ./graph/schema.graphqls \
		--name authors --routing-url https://authors-dot-jll-apollo-test.uc.r.appspot.com/query


regen:
	go run github.com/99designs/gqlgen init

deploy:
	gcloud app deploy

check:
	apollo service:check \
	--localSchemaFile=./graph/schema.graphqls \
	--graph=jesse-test-1xc6kq \
	--variant=current \
	--serviceName=authors

rcheck:
	rover subgraph check jesse-test-1xc6kq \
	--schema=./graph/schema.graphqls \
	--name=authors
