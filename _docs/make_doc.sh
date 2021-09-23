
rm -rf ../docs/*

make clean
make generate
make html

mv build/html/* ../docs