#!/bin/bash
for file in *.pdf; do
	ocrmypdf "${file}" "${file%.*}_ocr.pdf"
done;

