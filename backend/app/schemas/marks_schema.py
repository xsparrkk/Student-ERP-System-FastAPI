from pydantic import BaseModel


class MarksCreate(BaseModel):

    student_id: str
    student_class: int
    subject: str
    marks: int
    year: int


class MarksResponse(MarksCreate):

    id: int

    model_config = {
        "from_attributes": True
    }