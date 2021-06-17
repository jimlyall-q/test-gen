
from asyncio import sleep

from app.test_engine.logger import test_engine_logger as logger
from app.test_engine.models import TestCase, TestStep
from app.user_prompt_support.prompt_request import PromptRequest
from app.user_prompt_support.user_prompt_manager import (
    PromptExchange,
    user_prompt_manager,
)


class TCDD1_8(TestCase):

    metadata = {
        "public_id": "TCDD1_8",
        "version": "0.0.1",
        "title": "",
        "description": "",
    }

    def create_test_steps(self) -> None:
        self.test_steps = [
            TestStep("Test Step Spec 5.1.3.2: Verify using instruments"),
        ]

    async def setup(self) -> None:
        logger.info("No setup")

    async def execute(self) -> None:
        # Spec 5.1.3.2: Verify using instruments
        # The Manual Pairing Code should be printed using a minimum font size of 6 points, typically producing a typeface height of 2
        # 1 mm (6/72 inches)
        #
        logger.info("Spec 5.1.3.2: Verify using instruments")
        self.next_step()

    async def cleanup(self) -> None:
        logger.info("No cleanup")
