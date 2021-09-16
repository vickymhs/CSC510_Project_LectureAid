# Lecture Aid Documentation

This is the directory used to generate documentation, using [sphinx](https://www.sphinx-doc.org/en/master/). 

[The makefile](Makefile) is used to generate the documentation (create .rst files) and then to convert them to html
+ `make generate` generates the .rst files. This is using sphinx-autodoc, and the results are placed in source
+ `make html` is used to translate the .rst files to html, and the results are placed in build

[The make_doc.sh](make_doc.sh) file is used to automate these tasks.
1. Clears out the docs directy of old documentation
2. runs `make clean` to clean past builds
3. runs `make generate` to generate fresh documentation
4. runs `make html` to translate to html
5. moves the results from [the build directory](build/html) into the docs directory
   1. this is because when pushing to github pages, it prefers documentation is hosted at docs/index.html


## How to view documentation

+ If wishing to view in github, it is hosted in our github pages.
+ If wishing to view locally, run the `./make_doc.sh` to generate the documentation, then open ../docs in your local web browser


# Why document using sphinx

Our workflow is to only publish this to the documentation branch. This reduces confusion and reduces the large amount of files present on main.