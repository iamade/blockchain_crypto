stopped at video 52

**Activate the virtual environment for py3.9**
```
source mac-bchain-env/bin/activate
```

**Activate the virtual environment for py3.11**
```
source mac-py311-blochain-env/bin/activate
```

**Install all packages**
```
pip3 install -r requirements.txt
```

**Run the tests**
Make sure to activate the virtual environment

```
python3 -m pytest backend/tests
```

**Run Flask API**
```
python3 -m backend.app
```