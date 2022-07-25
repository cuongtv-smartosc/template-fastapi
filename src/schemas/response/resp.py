from typing import Union
from fastapi.responses import JSONResponse, Response
from fastapi.encoders import jsonable_encoder
from fastapi import status as http_status


class Resp(object):
    def __init__(self, status: int, msg: str, code: int):
        self.status = status
        self.msg = msg
        self.code = code

    def set_msg(self, msg):
        self.msg = msg
        return self


def success(*, data: Union[list, dict, str] = None, pagination: dict = None, msg: str = "success") -> Response:
    return_dict = {
        'status': 200,
        'msg': msg,
        'data': data,
    }
    if pagination:
        return_dict["pagination"] = pagination

    return JSONResponse(
        status_code=http_status.HTTP_200_OK,
        content=jsonable_encoder(return_dict)
    )


def fail(resp: Resp) -> Response:
    return JSONResponse(
        status_code=resp.code,
        content=jsonable_encoder({
            'status': resp.status,
            'msg': resp.msg,
        })
    )
