# E-ticket Admin
## Requirements
```python~=3.*```
```pip~=3.*```
```Django~=2.1.*```
##  Installation:

```
# this is on main dir
conda create -n venv python=3.6 

sudo apt install python3-pip

. venv/bin/activate

pip3 install -r requirements.txt

python3.6 manage.py makemigrations

python3.6 manage.py migrate

python3.6 manage.py runserver

```

Create another env for cms service:
Open a new terminal and type (tmux prefered):

```conda create -n venv python=3.6
cd cms_panel

conda create -n venv_cms python=3.6

. venv_cms/bin/activate

pip3 install -r requirements.txt

sudo ./run_cms.sh
```