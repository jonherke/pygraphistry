FROM jupyter/base-notebook

USER root

COPY ./environment.yml /opt/pygraphistry/environment.yml

RUN conda update -y conda \
 && conda install nb_conda_kernels \
 && conda env update --file /opt/pygraphistry/environment.yml

# RUN add-apt-repository ppa:igraph/ppa
RUN apt-get update -y \
 && apt-get install --no-install-recommends -y \
    python-igraph

COPY ./compose/jupyter-start.sh /usr/local/bin/jupyter-graphistry-start.sh

CMD ["jupyter-graphistry-start.sh"]
