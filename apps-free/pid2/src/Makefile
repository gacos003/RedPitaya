CC=$(CROSS_COMPILE)gcc
RM=rm

OBJECTS=main.o fpga.o worker.o calib.o fpga_awg.o generate.o fpga_pid.o pid.o

CFLAGS+= -Wall -Werror -g -fPIC $(INCLUDE)
LDFLAGS=-shared -L/opt/redpitaya/lib -lrp

CONTROLLER = ../controllerhf.so

all: $(CONTROLLER)

$(CONTROLLER): $(OBJECTS)
	$(CC) -o $(CONTROLLER) $(OBJECTS) $(CFLAGS) $(LDFLAGS)

clean:
	-$(RM) -f $(OBJECTS)
