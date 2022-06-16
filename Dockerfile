FROM continuumio/anaconda3

RUN conda install --yes -c pytorch pytorch=1.7.1 torchvision cudatoolkit=11.0
RUN pip install ftfy regex tqdm
RUN pip install git+https://github.com/openai/CLIP.git

