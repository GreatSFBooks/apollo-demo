register-service:
	apollo service:push \
	--endpoint=https://books-dot-jll-apollo-test.uc.r.appspot.com \
	--graph=jesse-test-1xc6kq \
	--variant=current \
	--serviceName=books \
	--serviceURL=https://books-dot-jll-apollo-test.uc.r.appspot.com

deploy:
	gcloud app deploy

check:
	forever start --pidFile /tmp/bookserver.pid server.js 
	apollo service:check \
	--endpoint=http://localhost:8080 \
	--graph=jesse-test-1xc6kq \
	--variant=current \
	--serviceName=books
	kill -9 $(cat /tmp/bookserver.pid | awk '{print $1}')