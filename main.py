import os

import uvicorn
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from line_api import api_routes
# from view import view



app = FastAPI()

templates = Jinja2Templates(directory="templates")

# app.mount("/static", StaticFiles(directory="static"), name="static")

# LINE Chatbot
app.include_router(api_routes)



if __name__ == "__main__":
    # Local WSGI: Uvicorn
    # port = int(os.getenv("PORT", 8000))
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        # port=port,
        # workers=4,
        # log_level="info",
        # access_log=True,
        # use_colors=True,
        reload=True,
    )