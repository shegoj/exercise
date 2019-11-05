#!/bin/bash

set -e
ARG=$1
RED='\033[0;31m'
BLACK='\033[0m'

function translation_assert  {
  digit="123"
  expected="One Hundred Twenty Three "
  actual=$(python3  digit_to_words.py $digit )
  echo -ne ">123 = expected:[${expected}] actual:[${actual}]"
  if [[ "${actual}" == "${expected}" ]]
  then
    echo -ne "\n>test passed"
  else
    echo -ne ">${RED} test failed ${BLACK}"
    exit 1
  fi
}

function usage  {
echo -ne ">use 'test' to run unittest \n>type number to convert to words 12345 \n> type 'stop' to exit \n> any other key for help\n>"
}

usage
echo -ne ">"
while read
  do
    case "$REPLY"  in
    "test")
      echo -ne ">$(translation_assert)\n>"
      ;;
    [0-9]*)
      echo -ne ">$(python3  digit_to_words.py $REPLY)\n>"
      ;;
    "stop")
      exit 0
      ;;
    *)
      usage
      ;;
    esac
done
