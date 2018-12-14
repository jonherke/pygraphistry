FROM conda/miniconda3
RUN conda update -y conda

COPY ./environment.yml /opt/pygraphistry-environment.yml
RUN conda env create --file /opt/pygraphistry-environment.yml

COPY ./compose/test-start.sh /usr/local/bin/test-graphistry-start.sh

CMD ["test-graphistry-start.sh"]
