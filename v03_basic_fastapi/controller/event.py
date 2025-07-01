from fastapi import APIRouter

router = APIRouter(
    prefix='/event',
    tags=['event'],
    responses={404: {"description" : "Not found"}}
)

@router.get("/{event_id}")
def read_event(event_id : int):
    return {'event_id' : event_id}