from http import HTTPStatus

from fastapi import APIRouter, HTTPException

from srv.log import SrvLogger
from utils.file_utils import FileUtils

router = APIRouter()

ROUTE = "/starships"
RESPONSE_PATH = "responses/starships/"
MSG_404 = "There are no info found."
LOG_MSG_TPL = "Route [{route}] with response code [{status_code}] was called."

log = SrvLogger().create_logger("Starships Route", "starships.log")


@router.get(ROUTE)
async def get_starships():
    try:
        response = FileUtils().get_all_files_from_dir(RESPONSE_PATH)
        log.info(LOG_MSG_TPL.format(route=ROUTE, status_code=HTTPStatus.OK))
        return response
    except FileNotFoundError:
        log.error(LOG_MSG_TPL.format(route=ROUTE, status_code=HTTPStatus.NOT_FOUND))
        raise HTTPException(status_code=HTTPStatus.NOT_FOUND, detail=MSG_404)


@router.get(ROUTE + "/{id}/")
async def get_starships_by_id(id: int):
    try:
        response = FileUtils().read_file(f"{RESPONSE_PATH}starships_{id}.json")
        log.info(LOG_MSG_TPL.format(route=f"{ROUTE}/{id}", status_code=HTTPStatus.OK))
        return response
    except FileNotFoundError:
        log.error(LOG_MSG_TPL.format(route=f"{ROUTE}/{id}", status_code=HTTPStatus.NOT_FOUND))
        raise HTTPException(status_code=HTTPStatus.NOT_FOUND, detail=MSG_404)
