cname = sakuraio-i2c
container = fisuda/sakuraio-i2c:1.0
device = --device /dev/i2c-1
env = -e INTERVAL=60

build:
	docker build -t $(container) .
run:
	docker run -d --name $(cname) $(env) $(device) $(container)
stop:
	docker stop $(cname)
rm:
	docker rm $(cname)
logs:
	docker logs $(cname)
