FROM jupyter/base-notebook

RUN conda update -y conda
RUN conda install nb_conda_kernels

COPY ./compose/jupyter-start.sh /usr/local/bin/jupyter-graphistry-start.sh

CMD ["jupyter-graphistry-start.sh"]
