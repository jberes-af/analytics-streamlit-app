

```text

python -m venv venv

OR

C:\Python312\python -m venv .venv

```

<br>

```text

.\.venv\Scripts\activate

```

<br>

```text

python -m streamlit run src/gui/streamlit/app.py

```





```text

C:\Python312\python -m venv .venv

.\.venv\Scripts\activate

python -m pip install --upgrade pip

pip install -e .

python -m pip install -r requirements.txt

VERIFY:
pip list | findstr your-package-name
```





```text
C:\Python312\python -m venv .venv

.\.venv\Scripts\Activate.ps1

python -m pip install --upgrade pip setuptools wheel

pip install -r requirements.txt

pip install -e .


VERIFY:
pip list | findstr alerta_home_analytics
```





### Github Repo Creation

1. Create empty repo on GitHub

<br>

2. Create local GitHub repo. In project parent folder: 

```text
git clone https://github.com/jberes-af/analytics-streamlit-app.git
```

<br>

3. Copy files to new local folder

<br>

4. Steps

```text
git init

git add .

git commit -m "Initial commit"

git branch -M main

git remote add origin https://github.com/jberes-af/analytics-streamlit-app.git

git push -u origin main


CHECK:
git remote -v

```



