from fastapi import APIRouter, Depends, HTTPException
from fastapi.encoders import jsonable_encoder
from sqlalchemy import delete, insert, select, update

from src.database import get_async_session
from sqlalchemy.ext.asyncio import AsyncSession
from src.operations.models import operation
from src.operations.schemas import OperationCreate


router = APIRouter(
    prefix = "/operations",
    tags = ["Operation"]
)

@router.get("/")
async def get_specific_operation(id: int, session: AsyncSession = Depends(get_async_session)):
    # try:
        query = select(operation).where(operation.c.id == id)
        result = await session.execute(query)
        result = jsonable_encoder(result)
        print(result)
        return result
    #     return {
    #         "status": "succesful",
    #         "data": result.all(),
    #         "details": None
    #     }
    # except:
    #     raise HTTPException(status_code=500, detail={
    #         "status": "error",
    #         "data": None,
    #         "details": None
    #     })
    
# @router.post("/")
# async def add_specific_operation(new_operation: OperationCreate, session: AsyncSession = Depends(get_async_session)):
#     stmt = insert(operation).values(**new_operation.model_dump())
#     await session.execute(stmt)
#     await session.commit()
#     return {"status": "succesfull"}

# @router.put("/{id}")
# async def replace_spicific_operation(id: int, new_operation: OperationCreate, session: AsyncSession = Depends(get_async_session)):
#     try:
#         new_operation.id = id
#         stmt = update(operation).where(operation.c.id == id).values(**new_operation.model_dump())
#         await session.execute(stmt)
#         await session.commit()
#         return {
#             "status": "succesful",
#             "data": new_operation,
#             "details": None
#         }
#     except:
#         raise HTTPException(status_code=500, detail={
#             "status": "error",
#             "data": None,
#             "details": None
#         })

# @router.delete("/{id}")
# async def replace_spicific_operation(id: int, session: AsyncSession = Depends(get_async_session)):
#     try:
#         query = select(operation).where(operation.c.id == id)
#         stmt = delete(operation).where(operation.c.id == id)
#         result = await session.execute(query)
#         await session.execute(stmt)
#         return {
#             "status": "succesful",
#             "data": result.all(),
#             "details": None
#         }
#     except:
#         raise HTTPException(status_code=500, detail={
#             "status": "error",
#             "data": None,
#             "details": None
#         })
