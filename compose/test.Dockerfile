FROM conda/miniconda3

COPY ./environment.yml /opt/pygraphistry/environment.yml

RUN conda update -y conda \
 && conda env update --file /opt/pygraphistry/environment.yml

COPY ./compose/test-start.sh /usr/local/bin/test-graphistry-start.sh

CMD ["test-graphistry-start.sh"]
