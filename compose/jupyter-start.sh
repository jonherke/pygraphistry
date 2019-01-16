#!/bin/bash

# conda env update --file /opt/pygraphistry/environment.yml

source activate graphistry

pip install -e /opt/pygraphistry

exec /usr/local/bin/start-notebook.sh $*
