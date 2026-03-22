from fastapi import APIRouter

router = APIRouter(prefix="/retrieval", tags=["retrieval"])

@router.get("/")
def retrieval():
    print("retrieval working")

