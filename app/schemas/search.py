from typing import List, Optional, Generic, TypeVar
from pydantic import BaseModel, Field
from pydantic.generics import GenericModel

T = TypeVar('T')

class SearchSchema(BaseModel):
    id: Optional[int] = None
    transcript: Optional[str] = None
    numberOfResults: Optional[int] = None
    
    class Config:
        orm_mode = True
        
class RequestSearch(BaseModel):
    parameter: SearchSchema = Field(...)
    
class Response(GenericModel,Generic[T]):
    code:str
    status:str
    message:str
    result: Optional[T]