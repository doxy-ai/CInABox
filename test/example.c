#! -I../libs/
#include <libc>
#include "empty.cpp"



void load(void) {
	printf("loaded\n");
}

void start(void) {
	printf("started\n");
}

void go(struct stop_token* stop) {
	printf("gone\n");
}