.PHONY: all

all: build/sweep.mpy build/kb.mpy build/boot.mpy
	echo "all..."

build/%.mpy: %.py
	mpy-cross -o $@ $<
