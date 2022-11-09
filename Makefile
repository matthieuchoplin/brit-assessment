
.PHONY: local-run
local-run:
	PYTHONPATH=src FLASK_APP=app:app FLASK_DEBUG=True flask run --host 0.0.0.0 --port 9000

.PHONY: local-test
local-test:
	PYTHONPATH=src pytest

migrate:
	# e.g. make migrate K='New table foo'
	PYTHONPATH=src FLASK_APP=app:app flask db migrate --directory src/migrations -m "$(K)"

upgrade_db:
	PYTHONPATH=src FLASK_APP=app:app flask db upgrade --directory src/migrations

fake:
	PYTHONPATH=src FLASK_APP=app:app flask fake pricelist

rm_db:
	rm -f src/db.sqlite

start_fresh: rm_db upgrade_db fake local-run

install-deps:  ## install python requirements into your virtualenv
	pip install -U pip-tools
	pip install -r requirements.txt

update-deps:  ## update pinned requirements
	pip-compile requirements.in --output-file requirements.txt --upgrade --upgrade-package 'click<8.0'
	make install-deps

run_front_end:
	cd src/ui && npm install && npm start
