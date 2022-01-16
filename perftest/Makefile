# Make all the things

.PHONY: perftest
perftest:
	locust -f locust_tests.py

v2test:
	locust -f v2_tests.py

lint:
	pylint locust_tests.py
