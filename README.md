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


# Dev Notes:

Do this to connect to postgresql:

`psql -U demo -W -h localhost`

and use password: `password`

# Postgresql upgrades:

For now, from INSIDE the demo/demo folder (where `app.py` is), run:

`python manage.py db upgrade`

Or the usual `flask db...` commands (`init`, `migrate`, etc.).

