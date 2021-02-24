push:
	apollo service:push \
	--endpoint=https://books-dot-jll-apollo-test.uc.r.appspot.com \
	--graph=jesse-test-1xc6kq \
	--variant=current \
	--serviceName=books \
	--serviceURL=https://books-dot-jll-apollo-test.uc.r.appspot.com

deploy:
	gcloud app deploy

check:
	PORT=4444 forever start -a --uid "book-check" --pidFile /tmp/bookserver.pid server.js 2>&1 1>/dev/null
	sleep 2
	apollo service:check \
	--endpoint=http://localhost:4444 \
	--graph=jesse-test-1xc6kq \
	--variant=current \
	--serviceName=books 2>/dev/null
	sleep 2
	forever stopall 2>&1 1>/dev/null