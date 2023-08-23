#!/bin/bash
for file in $(find . -iname *.pdf); do
	echo "${file}"
done;

