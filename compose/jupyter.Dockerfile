FROM jupyter/base-notebook
RUN conda update -y conda
RUN conda install nb_conda_kernels
RUN conda env create --file /opt/pygraphistry/environment.yml
