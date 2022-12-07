build:
	# TODO: Add commands for building the project here
	echo "Build!"
	c++ -std=c++11 -o main main.cpp ReverseFibonacci.cpp
run: build
	# TODO: Add commands for running the project here
	echo "Run!"
	./main 5
clean:
	# TODO: Add commands for cleaning up the build here
	echo "Clean!"
	rm main
