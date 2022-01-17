# deploydemo
Fun and exciting ways to deploy a standard web app backend

#### Debugging:

This seems to work...

```
export FLASK_APP=demo
pip install -e ./demo
flask run
```


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

`python -m manage db migrate -m "add users"` or `python manage.py db upgrade`

For whatever reason, this works but `flask db...` commands (`init`, `migrate`, etc.). does not.

