# Performance testing for Zero Downtime Deployments

Note that locust can be fickle with the URL specified.  Per locusts' documentation, API URLs are coded with a leading slash (`/`), however some URLs can throw a 500 error if the URL has adjacent slashes, so when running locust you should specify a URL that does NOT contain a trailing slash. i.e. `https://34.35.36.37` NOT `https://34.35.36.37/`.

## Prerequisites:

Tested on python versions 3.7, 3.8, and 3.9.

```
pip install --upgrade pip
pip-compile
pip install -r requirements.txt
make perftest
```

## Custom run

To run with custom parameters you can run locust directly:

```
locust -f locust_tests.py -H https://34.35.36.37 --users 100 --spawn-rate 5
```
