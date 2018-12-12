FROM conda/miniconda3
RUN conda update -y conda
RUN conda env create --file /opt/pygraphistry/environment.yml
