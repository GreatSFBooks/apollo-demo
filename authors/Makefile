register-service:
	apollo service:push \
	--localSchemaFile=./graph/schema.graphqls \
	--graph=jesse-test-1xc6kq \
	--variant=current \
	--serviceName=authors \
	--serviceURL=https://authors-dot-jll-apollo-test.uc.r.appspot.com/query

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
