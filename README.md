# Random_Quotes_Api

## To use API on swagger
1. Activate virtual environment 

2. Run the requirements.txt file to install dependencies

```pip install -r requirements.txt```

3. Run app

```uvicorn index:app --host localhost --port 8000```

*Or to reload upon change run* 

``` uvicorn index:app --host localhost --port 8000 --reload```

4. Navigate to http://localhost:8000/docs

5. Authorize user

6. Use API

---

## To use API on a UI
1. Activate virtual environment 

2. Run the requirements file to install dependencies

```pip install -r requirements.txt```

3. Run app

```uvicorn main:app --host localhost --port 8000```

*Or to reload upon change run* 

``` uvicorn main:app --host localhost --port 8000 --reload```

4. Navigate to http://localhost:8000/login

5. Authorize user

6. Use API
