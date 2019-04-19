# Dev guide

## python project

1. Installing `virtualenv` & `virtualenvwrapper` (optional)

2. Installing project, clone it and run

```bash
  git clone git@github.com:huongnhdh/byebase.git
  cd byebase
  pip install -r requirements.txt
  python setup.py develop # or  pip install -e .
```

## vscode editor

1. Setting file: ./vscode/settings.json
2. Installing extensions

```bash
cat ./vscode/vscode-extensions.list | xargs -L 1 code --install-extension
```
