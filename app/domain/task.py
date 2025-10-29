from pydantic import BaseModel, validator

class Task(BaseModel):
    id: int
    title: str
    status: str

    @validator("title")
    def validate_title(cls, value):
        if not value.strip():
            raise ValueError("title no puede estar vacío")
        return value

    @validator("status")
    def validate_status(cls, value):
        if value not in ["pending", "done"]:
            raise ValueError("status debe ser 'pending' o 'done'")
        return value
