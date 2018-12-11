FROM conda/miniconda3
RUN conda update -y conda
COPY ./environment.yml ./environment.yml
RUN conda env create --file environment.yml
COPY ./run-tests.sh ./run-tests.sh
ENTRYPOINT ["/bin/bash", "./run-tests.sh"]