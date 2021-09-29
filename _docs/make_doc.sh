
rm -rf ../docs/*

make clean
make generate
mkdir build/html
make html

mv build/html/* ../docs
# tells github to include _ folders
echo "" >> ../docs/.nojekyll