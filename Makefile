build:
	docker build . -t task:6.3

start:
	docker run -d -p 65432:65432 --name task6.3 --volume \/var\/log:/task task:6.3 


stop:
	docker stop task6.3

clean: 
	docker rm task6.3
