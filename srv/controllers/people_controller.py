from http import HTTPStatus
from random import randint
from time import sleep

from fastapi import APIRouter, HTTPException

from srv.log import SrvLogger
from utils.file_utils import FileUtils

router = APIRouter()

ROUTE = "/people"
RESPONSE_PATH = "responses/people/"
MSG_404 = "There are no info found."
LOG_MSG_TPL = "Route [{route}] with response code [{status_code}] was called."

log = SrvLogger().create_logger("People Route", "peoples.log")


@router.get(ROUTE)
async def get_peoples():
    sleep(randint(1, 5))
    try:
        response = FileUtils().get_all_files_from_dir(RESPONSE_PATH)
        log.info(LOG_MSG_TPL.format(route=ROUTE, status_code=HTTPStatus.OK))
        return response
    except FileNotFoundError:
        log.error(LOG_MSG_TPL.format(route=ROUTE, status_code=HTTPStatus.NOT_FOUND))
        raise HTTPException(status_code=HTTPStatus.NOT_FOUND, detail=MSG_404)


@router.get(ROUTE + "/{id}/")
async def get_people_by_id(id: int):
    sleep(randint(1, 5))
    try:
        response = FileUtils().read_file(f"{RESPONSE_PATH}people_{id}.json")
        log.info(LOG_MSG_TPL.format(route=f"{ROUTE}/{id}", status_code=HTTPStatus.OK))
        return response
    except FileNotFoundError:
        log.error(LOG_MSG_TPL.format(route=f"{ROUTE}/{id}", status_code=HTTPStatus.NOT_FOUND))
        raise HTTPException(status_code=HTTPStatus.NOT_FOUND, detail=MSG_404)
