from fastapi import FastAPI

from srv.controllers import people_controller, planets_controller, starships_controller

srv = FastAPI()

srv.include_router(people_controller.router)
srv.include_router(planets_controller.router)
srv.include_router(starships_controller.router)


@srv.get("/")
async def root():
    return {"message": "Test Python task."}
