FROM ubuntu
COPY asm-7172_sia.cpp .
RUN apt-get update && apt-get install -y build-essential gcc-multilib
RUN g++ -masm=intel asm-7172_sia.cpp -o 7172_sia -static
CMD ./7172_sia

