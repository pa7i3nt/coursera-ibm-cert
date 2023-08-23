#!/bin/bash
for file in $(find . -iname *.pdf); do
	ocrmypdf "${file}" "${file%.*}_ocr.pdf"
done;

