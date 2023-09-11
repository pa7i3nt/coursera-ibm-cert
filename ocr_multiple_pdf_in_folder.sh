#!/bin/bash

echo 'Checking if ocrmypdf library exists...'

if ! command -v ocrmypdf &> /dev/null
then
  echo "ocrmypdf not found. Installing..."
  sudo apt install ocrmypdf
fi

echo 'Done.'

echo 'Ocr-ing...'

for file in *.pdf; do
	ocrmypdf "${file}" "${file%.*}_ocr.pdf"
done;

echo 'Have a good day.'
