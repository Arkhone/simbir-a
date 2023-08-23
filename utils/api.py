import logging

from utils.requests import Client

logger = logging.getLogger("api")


class Api:
    def __init__(self, url: str):
        self.url = url
        self.client = Client()

    def folder(self, method: str, prefix: str, headers: dict):
        response = self.client.custom_request(method, f"{self.url}{prefix}", headers=headers)
        logger.info("A %s request recieved %s code", method, response.status_code)
        logger.info(response.text)
        return response
