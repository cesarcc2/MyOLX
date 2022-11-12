from fastapi import APIRouter, HTTPException, Path, Depends
from config.config import SessionLocal
from sqlalchemy.orm import Session
from schemas.search import SearchSchema, RequestSearch, Response
import crud.search as Crud

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post('/create')
async def create(request:RequestSearch, db: Session=Depends(get_db)):
    result = Crud.create_search(db, search = request.parameter)
    if isinstance(result, Exception):
        return Response(code=500, status="Error", message="Was not able to create Search: " + str(result)).dict(exclude_none=True)
    else:
        return Response(code=200, status="Ok", message="Search created successfully").dict(exclude_none=True)

@router.get("/")
async def get(db:Session=Depends(get_db)):
    _search = Crud.get_search(db,0,100)
    if len(_search) > 0:
        return Response(code=200, status="Ok",message="Success Fetched all data", result=_search).dict(exclude_none=True)
    else:
        return Response(code=404, status="Not Found",message="No searches found", result=_search).dict(exclude_none=True)

@router.get("/{id}")
async def get_by_id(id:int, db:Session=Depends(get_db)):
    _search = Crud.get_search_by_id(db,id)
    if _search != None:
        return Response(code=200, status="Ok",message="Success Fetching Search", result=_search).dict(exclude_none=True)
    else:
        return Response(code=404, status="Not Found",message="Search not found", result=_search).dict(exclude_none=True)
    
@router.post("/update")
async def update_search(request: RequestSearch, db:Session=Depends(get_db)):
    result = Crud.update_search(db, search_id = request.parameter.id, transcript = request.parameter.transcript, numberOfRecords = request.parameter.numberOfResults)
    if isinstance(result, Exception):
        return Response(code=500, status="Error", message="Was not able to update Search: " + str(result)).dict(exclude_none=True)
    else:
        return Response(code=200, status="Ok", message="Search updated successfully").dict(exclude_none=True)
    
@router.delete("/{id}")
async def delete(id: int, db:Session=Depends(get_db)):
    result = Crud.remove_search(db, search_id = id)
    return Response(code=200, status="Ok", message="Search deleted successfully").dict(exclude_none=True)