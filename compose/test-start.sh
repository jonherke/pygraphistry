#!/bin/bash

# conda env update --file /opt/pygraphistry/environment.yml

source activate graphistry

pytest /opt/pygraphistry
