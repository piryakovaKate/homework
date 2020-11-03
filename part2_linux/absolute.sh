#! /bin/bash


mkdir -p tmp/'hello world'
cd tmp/'hello world'
touch absolute.txt
echo 'hello world!!' > absolute.txt
cat -A absolute.txt
cd ..
cd ..
ls ls -lh ./tmp/'hello world'
