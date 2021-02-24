push:
	apollo service:push \
	--endpoint=https://awards-dot-jll-apollo-test.uc.r.appspot.com \
	--graph=jesse-test-1xc6kq \
	--variant=current \
	--serviceName=awards \
	--serviceURL=https://awards-dot-jll-apollo-test.uc.r.appspot.com

check:
	apollo service:check --serviceName=awards --endpoint=https://awards-dot-jll-apollo-test.uc.r.appspot.com

deploy:
	gcloud app deploy