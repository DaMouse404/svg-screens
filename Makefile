###############################################################################
# C flags
CFLAGS		+= -Os -g
CFLAGS		+= -Wextra -Wshadow -Wimplicit-function-declaration
CFLAGS		+= -Wredundant-decls -Wmissing-prototypes -Wstrict-prototypes
CFLAGS		+= -fno-common -ffunction-sections -fdata-sections

###############################################################################
# C & C++ preprocessor common flags
CPPFLAGS	+= -MD
CPPFLAGS	+= -Wall -Wundef

all:
	python parse.py > test.h
	gcc $(CFLAGS) $(CPPFLAGS) test.c -o test.bin
	./test.bin
