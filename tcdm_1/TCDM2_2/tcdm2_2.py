
from asyncio import sleep

from app.test_engine.logger import test_engine_logger as logger
from app.test_engine.models import TestCase, TestStep
from app.user_prompt_support.prompt_request import PromptRequest
from app.user_prompt_support.user_prompt_manager import (
    PromptExchange,
    user_prompt_manager,
)
class TCDM2_2(TestCase):

    async def setup(self) -> None:
        logger.info("No setup")

    async def execute(self) -> None:

    async def cleanup(self) -> None:
        logger.info("No cleanup")
