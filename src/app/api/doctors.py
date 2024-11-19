from fastapi import APIRouter, HTTPException, Path
from app.api import crud
from app.api.models import DoctorDB, DoctorSchema
from typing import List

router = APIRouter()


@router.post("/", response_model=DoctorDB, status_code=201)
async def Add_doctor(payload: DoctorSchema):
    doctor_id = await crud.post(payload)

    response_object = {
        "id": doctor_id,
        "name": payload.name,
        "surname": payload.sarname,
        "category": payload.category,
        "speciality": payload.speciality,
    }
    return response_object

@router.get("/{id}/", response_model=DoctorDB)
async def read_doctor(id: int = Path(..., gt=0),):
    doctor = await crud.get(id)
    if not doctor:
        raise HTTPException(status_code=404, detail="Doctor not found")
    return doctor

@router.get("/", response_model=List[DoctorDB])
async def read_all_doctors():
    return await crud.get_all()

@router.put("/{id}/", response_model=DoctorDB)
async def update_doctor(payload: DoctorSchema, id: int = Path(..., gt=0),):
    doctor = await crud.get(id)
    if not doctor:
        raise HTTPException(status_code=404, detail="Doctor not found")

    doctor_id = await crud.put(id, payload)

    response_object = {
        "id": doctor_id,
        "name": payload.name,
        "surname": payload.surname,
        "category": payload.category,
        "speciality": payload.speciality,
    }
    return response_object

@router.delete("/{id}/", response_model=DoctorDB)
async def delete_doctor(id: int = Path(..., gt=0)):
    doctor = await crud.get(id)
    if not doctor:
        raise HTTPException(status_code=404, detail="Doctor not found")

    await crud.delete(id)

    return doctor