from fastapi.responses import HTMLResponse, RedirectResponse
import uvicorn
from fastapi import FastAPI, Path, Query, Request,Form
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
import starlette.status as status
from starlette.routing import URL





app = FastAPI()


# @app.get("/")
# async def index():
#    return {"message": "Hello World"}

# Path params
# @app.get("/hello/{name}/{age}")
# async def hello(name:str,age:int):
#    return {"name": name, "age":age} 

# # Query params
# @app.get("/hi")
# async def hi(name:str,age:int):
#    return {"name": name, "age":age}

# # Path Validation condition
# @app.get("/ola/{name}/{age}")
# async def ola(*,name:str=Path(...,min_length=5,max_length=20),age:int = Path(..., ge=1, le=100),percent:float=Query(..., ge=0, le=100)):
#    return {"name": name}

# @app.get("/ch/")
# async def ch():
#    ret='''
# <html>
# <body>
# <h2>Hello World!</h2>
# </body>
# </html>
# '''
#    return HTMLResponse(content=ret)



templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")


############################################

# @app.get("/", response_class=HTMLResponse)
# async def login(request: Request):
#    return templates.TemplateResponse("login.html", {"request": request})


# @app.post("/submit/", response_class=RedirectResponse)
# async def submit(request:Request, data: dict):
#    name = data.get("username").strip().lower()
#    password = data.get("password").strip().lower()
#    print(name, password)
#    if name=="tushar" and password=="rawat":
#       print("Inside if")
#       return RedirectResponse(url=f"/pilo/{name}", status_code=303)

#    else:
#       print("Inside else")
#       ret='''
#             <html>
#             <body>
#             <h2>User not found!</h2>
#             </body>
#             </html>
#          '''
#       return HTMLResponse(content=ret)
   

# @app.get("/pilo/{name}", response_class=HTMLResponse)
# async def pilo(request: Request, name:str):
#    print("Pilo")
#    return templates.TemplateResponse("hello.html", context={"request": request, "name":name})



user = {"email": "tman@gmail.com", "password": "Rawat"}


@app.get("/", response_class=HTMLResponse)
async def signin(request: Request):
   return templates.TemplateResponse("signin.html", context={"request": request})


@app.post("/", response_class=RedirectResponse)
async def Validate(request: Request, email: str = Form(...), password: str = Form(...)):
   if(email==user["email"] and password==user["password"]):
      return templates.TemplateResponse("hello.html",context={"request":request, "name":email})    
   else:
      return templates.TemplateResponse("signin.html", context={"request": request},
                                          headers={"x-error": "Invalid credentials"}, status_code=status.HTTP_404_NOT_FOUND)


if __name__ == "__main__":
   uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)

