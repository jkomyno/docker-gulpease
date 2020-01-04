#!/bin/bash

echo "Converting pdf files in ./pdf to txt files"

find ./pdf -iname '*.pdf' -print0 | while IFS= read -r -d $'\0' line; do
  docker run --rm -i kalledk/pdftotext < "$line" > "${line::-3}txt"
done

echo "Spawning Gulpease process"

docker-compose up --build

echo "Python Gulpease report:"
cat report/report.json
