FROM alpine
COPY 7172_sia.asm .
RUN apk update && apk upgrade && apk add build-base nasm
RUN nasm -f elf64 7172_sia.asm && gcc -m64 -no-pie -o 7172_sia 7172_sia.o
CMD ./7172_sia

