FROM tensorflow/tensorflow:1.7.1
MAINTAINER Theis Hjalte Thorn Jakobsen <thornjakobsen@gmail.com>
MAINTAINER Terne Sasha Thorn Jakobsen <terne.thorn@gmail.com>

RUN apt-get update
RUN apt-get install wget -y

RUN pip install -U nltk
RUN pip install -U numpy

RUN pip install http://www.jbox.dk/sling/sling-1.0.0-cp27-none-linux_x86_64.whl
RUN cd /
RUN wget http://www.jbox.dk/sling/sempar.flow
