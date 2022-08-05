class LogRequest:

    def __init__(self, request, response, body, duration):
        self.req_method = request.method
        self.req_path = request.url.path
        self.req_path_params = request.path_params
        self.req_query_params = dict(request.query_params)
        self.req_body = body
        self.req_ip = request.client.host
        self.res_status = response.status_code
        self.duration = duration


    def __str__(self):
        return (
            f"[Request] "
            f"method={self.req_method} "
            f"path={self.req_path} "
            f"path_params={self.req_path_params} "
            f"query_params={self.req_query_params} "
            f"body={self.req_body} "
            f"ip={self.req_ip} "
            f"status={self.res_status} "
            f"duration={self.duration}ms"
        )
