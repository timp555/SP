FROM alpine
COPY 7172_sia.sh .
RUN apk update && apk upgrade && apk add bash && chmod +x 7172_sia.sh 
CMD ./7172_sia.sh
