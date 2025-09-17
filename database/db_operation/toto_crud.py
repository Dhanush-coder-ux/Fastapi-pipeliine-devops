from database.db_models.todo import AddToDo
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select,update,delete
from uuid import uuid4
from datetime import datetime,timezone
from fastapi import HTTPException



class __TodoCrudInputs:
    def __init__(self,db:AsyncSession):
        self.db=db
class TodoCrud(__TodoCrudInputs):
    async def todoAdd(self , data:str):
        try:
            id = uuid4().__str__()
            date =datetime.now(timezone.utc)
            adddb = AddToDo(
                id = id,
                data = data,
                date_time=date
            )
            self.db.add(adddb)
            await self.db.commit()
            return f'sucessfully added {data} !'
        except Exception as e:
            HTTPException(status_code=500,detail=f"somthing went wrong while adding todo {e}")

    async def getTodo(self):
        try:
            getdb= (await self.db.execute(
                select(
                    AddToDo.id,
                    AddToDo.data,
                    AddToDo.date_time
                )
            )).mappings().all()
            return {'todos': getdb}
        except Exception as e:
            HTTPException(status_code=500,detail=f'something went wrong while getting data{e}')


    async def updateTodo(self,id:str,data:str):
        try:
            putdb =( await self.db.execute(
                update(
                    AddToDo
                ).where(AddToDo.id==id).values(
                    data=data
                )
                .returning(AddToDo.id)
            )).scalar_one_or_none()
            print(putdb)

            
            
            if putdb:
                await self.db.commit()
                return "data hasbeen updated !!"
            
            else:
                raise HTTPException(status_code=404)
        except HTTPException:
            raise
        except Exception as e:
            HTTPException(status_code=500,detail=f"update failed {e}")   


    async def deleteTodo(self,id):
        try:
            deltodo = (await self.db.execute(
                delete(
                    AddToDo
                ).where(
                    id == AddToDo.id
                ).returning(AddToDo.id)
            ) ).scalar_one_or_none()
            if deltodo:
                await self.db.commit()
                return 'successfully deleted '
            else:
                raise HTTPException(
                    status_code=404
                )
        except HTTPException:
            raise
        except Exception as e:
            HTTPException(
                status_code=500,detail=f'something went wrong while deleting data {e}'
            )
                



            
        

        
    


