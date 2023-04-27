# from typing import Any
# from typing import Generator
#
# import pytest
# from fastapi import FastAPI
# from fastapi.testclient import TestClient
#
# from router.api.endpoints import router
#
#
# def start_application() -> FastAPI:
#     router = FastAPI()
#     router.include_router(router)
#     return router
#
#
# @pytest.fixture(scope="module")
# def client() -> Generator:
#     router = start_application()
#     with TestClient(router) as test_client:
#         yield test_client
