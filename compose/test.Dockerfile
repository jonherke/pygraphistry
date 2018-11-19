FROM conda/miniconda3

RUN conda update -y conda

COPY ./compose/test-start.sh /usr/local/bin/test-graphistry-start.sh

CMD ["test-graphistry-start.sh"]
