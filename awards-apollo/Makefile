push:
	apollo service:push \
	--localSchemaFile=schema.graphql \
	--graph=jesse-test-1xc6kq \
	--variant=current \
	--serviceName=awards \
	--serviceURL=https://awards-dot-jll-apollo-test.uc.r.appspot.com

publish:
	rover subgraph publish jesse-test-1xc6kq@current --schema ./schema.graphql \
		--name awards --routing-url https://awards-dot-jll-apollo-test.uc.r.appspot.com


deploy:
	gcloud app deploy

check:
	apollo service:check \
	--localSchemaFile=schema.graphql \
	--graph=jesse-test-1xc6kq \
	--variant=current \
	--serviceName=awards
#	--validationPeriod=20736000 

rcheck:
	rover subgraph check jesse-test-1xc6kq \
	--schema=schema.graphql \
	--name=awards