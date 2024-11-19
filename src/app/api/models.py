from pydantic import BaseModel, Field


class DoctorSchema(BaseModel):
    name: str = Field(..., min_length=3, max_length=50)
    surname: str = Field(..., min_length=3, max_length=50)
    category: int = Field(..., min_length=3, max_length=3)
    speciality: str = Field(..., min_length=3, max_length=50)

class ClientSchema(BaseModel):
    name: str = Field(..., min_length=3, max_length=50)
    surname: str = Field(..., min_length=3, max_length=50)
    email: str = Field(..., min_length=5, max_length=50)
    age: int = Field(..., min_length=3, max_length=3)
    phone: int = Field(..., min_length=3, max_length=12)

class RoomSchema(BaseModel):
    number: int = Field(..., min_length=1, max_length=4)

class AppointmentSchema(BaseModel):
    date: int = Field(..., min_length=6, max_length=15)
    doctor_id: int = Field(default=None, foreign_key="doctor.id")
    client_id: int = Field(default=None, foreign_key="client.id")
    room_id: int = Field(default=None, foreign_key="room.id")

class DoctorDB(DoctorSchema):
    id: int

class ClientDB(ClientSchema):
    id: int

class RoomDB(RoomSchema):
    id: int

class AppointmentDB(AppointmentSchema):
    id: int