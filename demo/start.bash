#!/bin/bash

# uvicorn --reload --host=0.0.0.0 demo.app:app
# gunicorn --bind 0.0.0.0 demo.app:app
python demo/manage.py run
