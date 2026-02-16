from fastapi import FastAPI,Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from markupsafe import escape
from typing import Union
import uvicorn

app =FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
template=Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return template.TemplateResponse("index.html", {"request": request})

@app.post("/user", response_class=HTMLResponse)
async def about(request: Request):
    form = await request.form()
    name = form.get("name")
    email = form.get("email")
    message = form.get("message")

    return f"""
    <h2>Thank you for reaching out, {escape(name)}!</h2>
    <p>We will get back to you at {escape(email)}.</p>
    <p>Your Message: {escape(message)}</p>
    """
g
if __name__=='__main__':
    uvicorn.run(app,host='127.0.0.1',port=8000)

# This will not work beacuse of the file structure according to the Flask, so fastAPI will not work, will use it in another project.