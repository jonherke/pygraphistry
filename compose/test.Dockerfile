FROM conda/miniconda3
RUN conda update -y conda

COPY ./environment.yml /opt/pygraphistry-environment.yml
RUN conda env create --file /opt/pygraphistry-environment.yml
