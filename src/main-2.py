from fastapi import FastAPI  # <1>

app = FastAPI() # <2>

@app.get("/") # <3>
def read_index(): # <4>
    """
    Return a Python Dictionary that supports JSON serialization.
    """
    return {"Hello": "World"} # <5>

@app.get("/api/v1/hello-world/") # <1>
def read_hello_world(): # <2>
    """
    Return an API-like response.
    """
    return {"what": "road", "where": "kubernetes", "version": "v1"}  # <3>