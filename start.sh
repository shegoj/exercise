#!/bin/bash
set -e

# first run unit test
echo "Performing unit test"
test_result="$(python3  src/digit_to_words.py 123)"
echo "Performing unit test [${test_result}]"
if [[ "${test_result}" != "One Hundred Twenty Three " ]]
then
  echo "failed unit test"
  exit 1
fi

## build image
echo "Performing Docker build"
docker build --rm  -f Dockerfile -t number_conversion_in_python:1.0 .
if  [ $? -ne  0 ]
then
  echo "docker build failed"
  exit 1
fi

echo -ne "Build successful. Instantiating container instance....\n\n"
docker run -it  number_conversion_in_python:1.0

