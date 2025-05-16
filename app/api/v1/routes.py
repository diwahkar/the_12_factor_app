from fastapi import APIRouter


router = APIRouter()

@router.get('/')
def hello_func():
    return 'main route'
