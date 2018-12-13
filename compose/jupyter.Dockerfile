FROM jupyter/base-notebook
RUN conda update -y conda
RUN conda install nb_conda_kernels

COPY ./environment.yml /opt/pygraphistry-environment.yml
RUN conda env create --file /opt/pygraphistry-environment.yml
