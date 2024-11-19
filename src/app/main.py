from fastapi import FastAPI
from app.api import doctors, clients, rooms, appointments
from app.db	import database, engine, metadata

metadata.create_all(engine)
app = FastAPI()

@app.on_event("startup")
async def startup():
		await database.connect()

@app.on_event("shutdown")
async def shutdown():
		await database.disconnect()

app.include_router(doctors.router, prefix = "/doctors", tags =["doctors"])
app.include_router(clients.router, prefix = "/clients", tags =["clients"])
app.include_router(rooms.router, prefix = "/rooms", tags =["rooms"])
