push:
	apollo service:push \
	--localSchemaFile=schema.graphql \
	--graph=jesse-test-1xc6kq \
	--variant=current \
	--serviceName=books \
	--serviceURL=https://books-dot-jll-apollo-test.uc.r.appspot.com

deploy:
	gcloud app deploy

check:
	apollo service:check \
	--localSchemaFile=schema.graphql \
	--graph=jesse-test-1xc6kq \
	--variant=current \
	--serviceName=books 
