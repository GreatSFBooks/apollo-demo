push:
	apollo service:push \
	--localSchemaFile=schema.graphql \
	--graph=jesse-test-1xc6kq \
	--variant=current \
	--serviceName=books \
	--serviceURL=https://books-dot-lovelace-presales-demo.ue.r.appspot.com

publish:
	rover subgraph publish jesse-test-1xc6kq@current --schema ./schema.graphql \
		--name books --routing-url https://books-dot-lovelace-presales-demo.ue.r.appspot.com

deploy:
	gcloud app deploy

check:
	apollo service:check \
	--localSchemaFile=schema.graphql \
	--graph=jesse-test-1xc6kq \
	--variant=current \
	--serviceName=books 
#	--validationPeriod=20736000 

rcheck:
	rover subgraph check jesse-test-1xc6kq \
	--schema=schema.graphql \
	--name=books --validation-period=4weeks