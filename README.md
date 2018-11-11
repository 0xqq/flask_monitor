# monitor
---
> diretory

```
- monitor/          # main
  - __init__.py     # flask app init
  - apps/           # app directory
    - monitor_app/  # monitor app
      - models.py
      - urls.py
      - views.py
  - utils/          # app util diretory
  - static/         # statics diretory
  - templates/      # templates diretory
  - test/
    - test_db.py    # test Flask-SQLAlchemy module
```

>Usage

```
1.git clone
2.cd monitor/
3.pip install -r requirements.txt
4.export FLASK_APP=monitor
5.flask run --host 127.0.0.1 --port 5001
```