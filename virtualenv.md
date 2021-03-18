## install virtualenv
```
sudo pip3 install virtualenv
```

## list of packages in the current environment
```
pip3 list --local
```

## virtual environment
### create folder files
```
virtualenv projecto_scrapy
```
### create virtual enviroment with python version 3.6
```
virtualenv --python=python3.6 venv_name
```
### activate virtual enviroment
```
source projecto_scrapy/bin/activate
```
### deactivate virtual enviroment
```
deactivate
```

## check path
```
which python3
which pip3
```

## list in requirements format
```
pip3 freeze -l > requirements.txt
pip3 freeze --local > requirements.txt
```

## install packages from list
```
pip3 install -r requirements.txt
```

## unistall packages from list
```
pip3 uninstall -r requirements.txt -y
```
