MSG="New commit"
HOST=localhost

.PHONY : help
help:
	@fgrep -h "##" $(MAKEFILE_LIST) | fgrep -v fgrep | sed -e 's/\\$$//' | sed -e 's/##//'

.PHONY : commit
commit: ## "commit COMMIT_MSG="Commit message" : Add changes to git and commit"
	echo $(MSG)
	git add --all
	git commit -a -S -m "$(MSG)"
	git push

.PHONY : lint
lint: ## "Check linting flake8"
	source p3env/bin/activate &&  flake8 twilliosms/ --ignore=E501,F401

.PHONY : build
build: ## "Build piyp package"
	source p3env/bin/activate && python3 setup.py sdist bdist_wheel

.PHONY : upload
upload: ## "Upload package to Pyp"
	source p3env/bin/activate && python3 -m twine upload --skip-existing dist/*

.PHONY : check
check: ## "Upload package to Pyp"
	source p3env/bin/activate && python3 -m twine check  dist/*


.PHONY : code_format
code_format: ## "Format code using black -t py38
	source p3env/bin/activate &&  black twilliosms/ -v -t py38

.PHONY : code_format_check
code_format_check: ## "Check code format with black"
	source p3env/bin/activate &&  black twilliosms/ -v -t py38 --check --diff
