build:
	docker build --tag mostafa/pipeline .

run: build
	docker run --rm -it mostafa/pipeline day1

pg:
	docker run --rm -it \
		--name pg \
		-e POSTGRES_USER="root" \
		-e POSTGRES_PASSWORD="root" \
		-e POSTGRES_DB="ny_taxi" \
		-p 3333:5432 \
		-v $(shell pwd)/ny_taxi_volume:/var/lib/postgresql/data \
		postgres:15

up:
	docker-compose up -d

logs:
	docker-compose logs -f

clean:
	docker-compose down
