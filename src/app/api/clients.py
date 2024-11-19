from fastapi import APIRouter, HTTPException, Path
from app.api import crud
from app.api.models import ClientDB, ClientSchema
from typing import List

router = APIRouter()


@router.post("/", response_model=ClientDB, status_code=201)
async def Add_client(payload: ClientSchema):
    client_id = await crud.post(payload)

    response_object = {
        "id": client_id,
        "name": payload.name,
        "surname": payload.sarname,
        "email": payload.email,
        "age": payload.age,
        "phone": payload.phone
    }
    return response_object

@router.get("/{id}/", response_model=ClientDB)
async def read_client(id: int = Path(..., gt=0),):
    client = await crud.get(id)
    if not client:
        raise HTTPException(status_code=404, detail="Client not found")
    return client

@router.get("/", response_model=List[ClientDB])
async def read_all_clients():
    return await crud.get_all()

@router.put("/{id}/", response_model=ClientDB)
async def update_client(payload: ClientSchema, id: int = Path(..., gt=0),):
    client = await crud.get(id)
    if not client:
        raise HTTPException(status_code=404, detail="Client not found")

    client_id = await crud.put(id, payload)

    response_object = {
        "id": client_id,
        "name": payload.name,
        "surname": payload.sarname,
        "email": payload.email,
        "age": payload.age,
        "phone": payload.phone
    }
    return response_object

@router.delete("/{id}/", response_model=ClientDB)
async def delete_client(id: int = Path(..., gt=0)):
    client = await crud.get(id)
    if not client:
        raise HTTPException(status_code=404, detail="Client not found")

    await crud.delete(id)

    return client