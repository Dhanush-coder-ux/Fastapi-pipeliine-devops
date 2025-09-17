from fastapi import APIRouter,Depends
from database.db_operation.toto_crud import TodoCrud
from database.main import get_db
from pydantic import BaseModel

router = APIRouter(
    tags=['todocrud']
)
class TodoSchema(BaseModel):
    data:str
class TodoSchemaput(BaseModel):
    id:str
    data:str
class TodoSchemaputdel(BaseModel):
    id:str
    


@router.post('/todo')
async def add_ToDo(res:TodoSchema,db=Depends(get_db)):
    return  await TodoCrud(db=db).todoAdd(res.data)

@router.get('/todo')
async def get_ToDo(db = Depends(get_db)):
    return await TodoCrud(db=db).getTodo()

@router.put('/todo')
async def put_ToDo(res:TodoSchemaput,db=Depends(get_db)):
    return await TodoCrud(db=db).updateTodo(res.id,res.data)

@router.delete('/todo')
async def del_ToDo(res:TodoSchemaputdel,db=Depends(get_db)):
    return await TodoCrud(db=db).deleteTodo(res.id)


