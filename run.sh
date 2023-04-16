#!/bin/sh
#
set -eu

BASEDIR=${0%/*}

if ! [ -f "$BASEDIR/venv/bin/activate" ]
then
	echo "Virtualenv not found in '$BASEDIR/venv'" >&2
	exit 1
fi

cd "$BASEDIR"
. "venv/bin/activate"

exec gunicorn -b 0.0.0.0:8000 'sharp_remote:create_app()'

