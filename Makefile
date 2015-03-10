all:
	python parse.py > test.h
	gcc test.c -o test.bin
	./test.bin
