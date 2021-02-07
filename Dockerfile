FROM continuumio/miniconda3
RUN conda install pytest
WORKDIR /ia
CMD bash