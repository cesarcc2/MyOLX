from sqlalchemy.orm import Session
from models.search import Search
from schemas.search import SearchSchema

# Get All Search Data
def get_search(db:Session, skip:int=0, limit:int=100):
    return db.query(Search).offset(skip).limit(limit).all()

# Get Search By ID
def get_search_by_id(db:Session, search_id:int):
    return db.query(Search).filter(Search.id == search_id).first()

# Create a new Search
def create_search(db:Session, search:SearchSchema):
    try:
        _search = Search(transcript = search.transcript,
                     numberOfResults = search.numberOfResults)
        db.add(_search)
        db.commit()
        db.refresh(_search)
        return _search
    except Exception as e:
        print("ERROR - [CRUD] create_search :" , e)
        return e
    
    

# Remove Search By ID
def remove_search(db:Session, search_id:int):
    _search = get_search_by_id(db,search_id)
    db.delete(_search)
    db.commit()

# Update Search by ID
def update_search(db:Session, search_id:int, transcript:str, numberOfRecords:int):
    try:
        _search = get_search_by_id(db,search_id)
        try:
            _search.transcript = transcript
            _search.numberOfRecords = numberOfRecords
            db.commit()
            db.refresh(_search)
            return _search
        except Exception as e:
            print("ERROR - [CRUD] update_search :" , e)
            return e
    except Exception as e:
        print("ERROR - [CRUD] update_search :" , e)
        return e
    