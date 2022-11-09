# Recruitment exercise for Brit Insurance

Create a system which includes a Database, backend and frontend. Chose Python for backend and
your choice of framework and language for frontend and database. Deploy it at your preferred
hosting solution ideally using free tier, for example, AWS, Azure, Heroku etc.

All calculations should happen in backend and not in the frontend. All data from the forms should be
saved in the database and not cached in the frontend.

If something is ambiguous, please use your best judgement. Use 1-3 hour for this delivery, it is fine
to take shortcuts to deliver it, please note them down.

There is no need to setup CI/CD but a git repo or any other source code management system is
important.

Below you can see the wireframes of the system and the basic requirements.

1. The user should be able to add items and the price
2. Once the user is happy, pressing summary button will show the total cost of all items


## Backend development

#### Setup
* `python3 -m venv .venv`
* `source .venv/bin/activate`
* `make install-deps`
* `make upgrade_db`
* `make fake`

#### Test
* `make local-test`

#### Run
* `make local-run`
* access the app at `http://localhost:9000`
* example routes:
 - `http://127.0.0.1:9000/api/pricelists/1`
 - `http://127.0.0.1:9000/api/pricelists/1/items`

## Frontend development
