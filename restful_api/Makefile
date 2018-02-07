IMAGE=sillycat/public
TAG=water-monitor-restful-api
NAME=water-monitor-restful-api

docker-context:

build: docker-context
	docker build -t $(IMAGE):$(TAG) .

run:
	docker run -d -p 8000:8000 --name $(NAME) $(IMAGE):$(TAG)

debug:
	docker run -ti -p 8000:8000 --name $(NAME) $(IMAGE):$(TAG) /bin/bash

clean:
	docker stop ${NAME}
	docker rm ${NAME}

logs:
	docker logs ${NAME}

publish:
	docker push ${IMAGE}:${TAG}

fetch:
	docker pull ${IMAGE}:${TAG}