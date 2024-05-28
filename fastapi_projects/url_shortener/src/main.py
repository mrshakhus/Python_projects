from fastapi import FastAPI
from pydantic import HttpUrl


app = FastAPI()

def is_valid_url(url: HttpUrl):
    return True
