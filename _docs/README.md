# Lecture Aid Documentation


## Requirements
This is the directory used to generate documentation, using [sphinx](https://www.sphinx-doc.org/en/master/).
- For Windows:
  - open command prompt and type `pip install Sphinx`
- For Linux or Mac:
  - open terminal and type `pip install Sphinx`
 
## How to generate documentation
This can be eventually automated with git tasks.

- run `./make_doc.sh`


[The make_doc.sh](make_doc.sh) file is used to automate these tasks.
1. Clears out the docs directory of old documentation
2. Runs `make clean` to clean past builds
3. Runs `make generate` to generate fresh documentation
4. Runs `make html` to translate to html
5. Moves the results from [the build directory](build/html) into the docs directory
   1. this is because when pushing to github pages, it prefers documentation is hosted at docs/index.html

[The makefile](Makefile) is used to generate the documentation (create .rst files) and then to convert them to html
+ `make generate` generates the .rst files. This is using sphinx-autodoc, and the results are placed in source
+ `make html` is used to translate the .rst files to html, and the results are placed in build

### Errors?
If you are getting an error about code not being a package, we reccomend using a PyCharm task instead. You will now emulate the make_doc.sh file
1. Remove everything inside the ../docs folder
2. Run `make clean` from this directory
3. Run `make generate`
4. The next step, make html, will be done in PyCharm
   + First, ensure you have the rst plugin installed
     - Then, add a run configuration
       - Type: python docs -> Sphinx task
     - Source: "proj_path"\_docs\source
     - Build: "proj_path"\_docs\build\html
     - Run
5. Move everything from build/* to ../docs
6. Make a new file within ../docs called .nojekyll, within nothing inside of it
   - tells github to include _ folders
   
## How to view documentation

+ If wishing to view in github, it is hosted in our github pages.
+ If wishing to view locally, run the `./make_doc.sh` to generate the documentation, then open ../docs in your local web browser


## Why document using sphinx

Our workflow is to only publish this to the documentation branch. This reduces confusion and reduces the large amount of files present on main.
Sphinx also automatically generates documentation, so instead of having to write recursive functions to generate documentation from each docstring,
Sphinx will do that for us. We just provide what folders to recurse into.


## Troubleshooting
- code is not a package
  - one workaround is to run a sphinx task instead (pycharm plugin)
- sphinx-build is not recognized
  - First, try and run `pip install Sphinx` and rerun the command 
  - Another option for windows is to run `pip uninstall Sphinx` and install using `choco install sphinx`