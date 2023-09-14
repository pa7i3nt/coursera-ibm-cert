#!/bin/bash

echo "Installing mongoimport and mongoexport..."

wget https://fastdl.mongodb.org/tools/db/mongodb-database-tools-ubuntu1804-x86_64-100.5.0.deb

sudo apt install ./mongodb-database-tools-*-100.5.0.deb -y

which mongoimport

which mongoexport

echo "Good luck have fun."
