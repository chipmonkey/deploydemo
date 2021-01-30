# deploydemo
Fun and exciting ways to deploy a standard web app backend

## This is a demo
The code is undoubtedly horrible.

The ideas are good tho.  Like...

* A/B Testing
* Experiment Groups
* Canary Deployments
* Red/Green Deployments
* Zero-Downtime Deployments
* That sort of thing


# Zero Downtime Demo

Good luck.

## Demo Notes:
(this is kind of a script, but needs to be cleaned up).
Apologies that these only appear in Main - keep this open in an editor since the file will go away when you `git checkout` things!

open 4 terminals to the demo repo
Open chrome to pgadmin, locust, github, whatever
(not everything will be up yet)

	git checkout main

	docker-compose up -d pgadmin
	docker-compose up -d demo-postgres

login to pgadmin:  pgadmin@test.com / password
Connect pgadmin to host: demo-postgres username: demo

# Show tags:
	git tag
	git checkout v1.0.0
	make docker-start
	make db-upgrade

	./demo/demo/POST\_test.sh
	show postgres
	show http://localhost:8000/users/

	curl -X PATCH -H "Content-Type: application/json" -d '{"name":"Paul Simon", "userid":"1"}' http://localhost:8000/user/
	show postgres
	show http://localhost:8000/users/

# Show locust users:
	make perftest
	browse to locust and see 

# PAUSE HERE FOR APPLAUSE


	git checkout v2.0.0
	make db-upgrade

# FAIL FAIL FAIL
	Check pgadmin
	Check Locust - FAIL FAIL
	Clear Lock
	Check Locust - all is well
# AHHHHH

# Emergency branch and update
Show what changed in github compare/diff

	git checkout v1.0.1

	docker-compose up -d demo-api-v101

	docker-compose logs -f demo-api
	docker-compose logs -f demo-api-v101

	git checkout v2.0.0
	make db-upgrade

# FAIL FAIL FAIL AGAIN!
	Check pgadmin
	Check Locust - FAIL FAIL
	Clear Lock in pgAdmin
	Check Locust - all is well

	docker-compose stop demo-api

These next two commands won't work:

	make db-upgrade
	docker-compose exec --env FLASK\_APP=demo demo-api flask db upgrade --directory /mnt/migrations

# BECAUSE V2.0.0 DOES NOT KNOW ABOUT V1.0.1!

docker-compose up -d demo-api-v2
	make db-upgrade

# FINALLY

Check pgadmin:

	select * from users
	where id < 51;

No last names?!  OK, no, we haven't rolled out any front end changes.
Stop and reload locust (as if we deployed the front-end updates to users):

	make perftest
# Check the nginx.conf - try a canary deployment?
	cp nginx/nginx-v2-canary.conf ./nginx.conf

	docker-compose logs -f demo-api-v2
	docker-compose logs -f demo-api-v101

	make reload\_nginx

# SHOULD see slow logs and fast logs
# Check for uptime then fully deploy
	cp nginx/ngix-v2.conf ./nginx.conf


# Yay, v2 is released!
	select * from users

# OH NO!!!! DATA CORRUPTION!!
Names don't match first + last names!  The Horror!

Compare v2.0.1 in github compare/diff

	git checkout v2.0.1

	docker-compose up -d demo-api-v201
	docker-compose logs -f demo-api-v201

	cat nginx.conf

	make nginx\_reload

# SQL Scripts for somewhere along the way...
Note that these are useless if ran at the wrong time
(that's why they're sneaky here at the end).

Too soon and users just overwrite things with bad data.
Too late and users have overwritten things with _worse_ data (in our case).

	set name = first || ' ' || last
	where name != first || ' ' || last;

	update users
	set first = split\_part(name, ' ', 1),
		last = split\_part(name, ' ', 2)
	where first is null;

	select *
	from users
	where
	first != split\_part(name, ' ', 1) or
		name is null or
		first is null;

# Tear it all down...
	docker-compose down --remove-orphans

