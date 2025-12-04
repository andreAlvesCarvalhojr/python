from fastapi import APIRouter, status, Response

router = APIRouter()

@router.get("/health", status_code=status.HTTP_200_OK)
def creaete_products(response: Response):
    return

