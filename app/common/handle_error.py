from http import HTTPStatus


class ErrorMessages:
    default = "Unhandled Error"
    bad_request = "Bad request"
    un_authorized = "Unauthorized"
    wrong = "Something went wrong"
    not_found = "Not found"
    method_not_allow = "Method not allowed"
    bad_request = "Bad request"

class APIException(Exception):
    http_status = HTTPStatus.INTERNAL_SERVER_ERROR
    message = ErrorMessages.default
    data = None
    extra = None
    success = False

    def __init__(
        self,
        success=False,
        data=None,
        http_status=HTTPStatus.INTERNAL_SERVER_ERROR,
        message=ErrorMessages.default,
        extra=None,
    ):
        super().__init__()
        self.success = success
        self.data = data
        self.http_status = http_status
        self.message = message
        self.extra = extra


class NotFoundException(APIException):
    message = ErrorMessages.not_found
    http_status = HTTPStatus.NOT_FOUND

    def __init__(self, message=ErrorMessages.not_found, extra=None):
        super().__init__(http_status=HTTPStatus.NOT_FOUND, message=message, extra=extra)

    def __str__(self):
        return "Not Found errors"


class BadRequestException(APIException):
    message = ErrorMessages.bad_request
    http_status = HTTPStatus.BAD_REQUEST

    def __init__(self, message=ErrorMessages.bad_request, extra=None):
        super().__init__(
            http_status=HTTPStatus.BAD_REQUEST, message=message, extra=extra
        )

    def __str__(self):
        return "Bad Request Errors"


class MethodNotAllowed(APIException):
    message = ErrorMessages.method_not_allow
    http_status = HTTPStatus.METHOD_NOT_ALLOWED

    def __int__(self, message=ErrorMessages.method_not_allow, extra=None):
        super().__init__(
            http_status=HTTPStatus.METHOD_NOT_ALLOWED, message=message, extra=extra
        )

    def __str__(self):
        return "Method not allowed"
