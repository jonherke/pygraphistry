FROM jupyter/base-notebook
COPY ./environment.yml ./environment.yml
RUN conda update -y conda
RUN conda env create --file environment.yml
RUN conda install nb_conda_kernels
