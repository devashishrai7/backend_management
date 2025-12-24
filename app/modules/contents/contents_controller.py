from sqlalchemy.orm import Session
from app.modules.contents.contents_model import Content
from app.modules.contents.contents_schema import Contents

def createContent(db: Session, data:Contents):
    obj = Content(
        subject = data.subject,
        description = data.description
    )
    db.add(obj)
    db.commit()
    return {
        'success' : True,
        'message' : 'Content created!'
    }

def getContent(db: Session):
    data = db.query(Content).all()
    return {
        'success' : True,
        'message' : 'Data fetched successfully',
        'data' : data
    }
    
