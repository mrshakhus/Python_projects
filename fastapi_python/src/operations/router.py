from typing import List
from fastapi import APIRouter, Depends, HTTPException
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
async def read_specific_operation(id: int, session: AsyncSession = Depends(get_async_session)):
    try:
        query = select(operation).where(operation.c.id == id)
        result = await session.execute(query)

        return {
            "status": "succesful",
            "data": result.mappings().all(),
            "details": None
        }
    except:
        raise HTTPException(status_code=500, detail={
            "status": "error",
            "data": None,
            "details": None
        })
    
@router.post("/")
async def create_specific_operation(new_operation: OperationCreate, session: AsyncSession = Depends(get_async_session)):
    try:
        stmt = insert(operation).values(**new_operation.model_dump())
        await session.execute(stmt)
        await session.commit()

        # query = select(operation).where(operation.c.id == new_operation.id)
        # added_operation = await session.execute(query)
        
        return {
                "status": "succesful",
                "data": new_operation, #added_operation.mappings().all(),
                "details": None
            }
    except:
        raise HTTPException(status_code=500, detail={
            "status": "error",
            "data": None,
            "details": None
        })

@router.put("/{id}")
async def replace_spicific_operation(id: int, new_operation: OperationCreate, session: AsyncSession = Depends(get_async_session)):
    try:
        new_operation.id = id
        query = select(operation).where(operation.c.id == id)
        result = await session.execute(query)
        op_to_update = result.mappings().all()

        #for debug
        print(op_to_update)
        print(type(op_to_update))

        op_to_update = dict(op_to_update[0])
        op_to_update = OperationCreate(**op_to_update)
        updated_op = op_to_update.model_copy(update=new_operation.model_dump(exclude_unset=True))

        stmt = update(operation).where(operation.c.id == id).values(**updated_op.model_dump())
        await session.execute(stmt)
        await session.commit()
        return {
            "status": "succesful",
            "data": updated_op,
            "details": None
        }
    except:
        raise HTTPException(status_code=500, detail={
            "status": "error",
            "data": None,
            "details": None
        })

@router.delete("/{id}")
async def replace_spicific_operation(id: int, session: AsyncSession = Depends(get_async_session)):
    try:
        query = select(operation).where(operation.c.id == id)
        stmt = delete(operation).where(operation.c.id == id)
        operation_to_delete = await session.execute(query)
        await session.execute(stmt)
        await session.commit()
        return {
            "status": "succesful",
            "data": operation_to_delete.mappings().all(),
            "details": None
        }
    except:
        raise HTTPException(status_code=500, detail={
            "status": "error",
            "data": None,
            "details": None
        })
