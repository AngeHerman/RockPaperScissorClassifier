
main:
	python3 main.py

test:
	python3 ./test/test_requests.py

clean:
	rm -rf __pycache__

default: main

.PHONY: main test clean default