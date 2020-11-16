# dev
build-prod:
	$(MAKE) build options="--target production

# production
compose-start:
	docker-compose up --remove-orphans $(options)