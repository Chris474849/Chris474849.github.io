from pydantic import BaseModel

class ConfigBase(BaseModel):
    status: str
    data: dict

class ConfigCreate(ConfigBase):
    pass

class ConfigUpdate(BaseModel):
    data: dict

class ConfigOut(BaseModel):
    id: int
    status: str
    data: dict

    class Config:
        orm_mode = True
