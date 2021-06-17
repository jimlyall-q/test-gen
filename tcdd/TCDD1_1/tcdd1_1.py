
from asyncio import sleep

from app.test_engine.logger import test_engine_logger as logger
from app.test_engine.models import TestCase, TestStep
from app.user_prompt_support.prompt_request import PromptRequest
from app.user_prompt_support.user_prompt_manager import (
    PromptExchange,
    user_prompt_manager,
)


class TCDD1_1(TestCase):

    metadata = {
        "public_id": "TCDD1_1",
        "version": "0.0.1",
        "title": "",
        "description": "",
    }

    def create_test_steps(self) -> None:
        self.test_steps = [
            TestStep(
                "Test Step 5.1.7: Keep the DUT in packaging and bring in NFC scanner close to packaging."),
        ]

    async def setup(self) -> None:
        logger.info("No setup")

    async def execute(self) -> None:
        self.next_step()

    async def cleanup(self) -> None:
        logger.info("No cleanup")
