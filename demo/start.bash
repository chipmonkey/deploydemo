#!/bin/bash

SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )
echo $SCRIPT_DIR

pip install /mnt/wheels/demo-1.0.1-py3-none-any.whl

# uvicorn --reload --host=0.0.0.0 demo.app:app
# gunicorn --bind 0.0.0.0 demo:app
# python ${SCRIPT_DIR}/demo/manage.py run -h 0.0.0.0 -p 8000
export FLASK_APP=demo
export FLASK_ENV=development
# flask run -h 0.0.0.0 -p 8000
flask run -h 0.0.0.0 -p 80
