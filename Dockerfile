FROM tensorflow/tensorflow:1.7.1
MAINTAINER Theis Hjalte Thorn Jakobsen <thornjakobsen@gmail.com>
MAINTAINER Terne Sasha Thorn Jakobsen <terne.thorn@gmail.com>

RUN apt-get update && \
    apt-get install -y wget

RUN pip install -U nltk numpy

RUN pip install http://www.jbox.dk/sling/sling-1.0.0-cp27-none-linux_x86_64.whl
WORKDIR /
RUN wget http://www.jbox.dk/sling/sempar.flow
