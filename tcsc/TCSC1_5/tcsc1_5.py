
from asyncio import sleep

from app.test_engine.logger import test_engine_logger as logger
from app.test_engine.models import TestCase, TestStep
from app.user_prompt_support.prompt_request import PromptRequest
from app.user_prompt_support.user_prompt_manager import (
    PromptExchange,
    user_prompt_manager,
)


class TCSC1_5(TestCase):

    metadata = {
        "public_id": "TCSC1_5",
        "version": "0.0.1",
        "title": "",
        "description": "",
    }

    def create_test_steps(self) -> None:
        self.test_steps = [
            TestStep("Test Step 4.13.4.2-1: TH sends duplicate message to DUT with reliability bit set to 1. Messages sent have the same message counter"),
            TestStep("Test Step 4.13.4.2-1: no test step"),
        ]

    async def setup(self) -> None:
        logger.info("No setup")

    async def execute(self) -> None:
        # 4.13.4.2-1: TH sends duplicate message to DUT with reliability bit set to 1. Messages sent have the same message counter
        # Verify the DUT detects the duplicate messages and discards the additional duplicate messages
        logger.info(
            "4.13.4.2-1: TH sends duplicate message to DUT with reliability bit set to 1. Messages sent have the same message counter")
        self.next_step()

        # 4.13.4.2-1: no test step
        # Verify the DUT sends an acknowledgement message to the TH for the initial instance of the authenticated message
        logger.info("4.13.4.2-1: no test step")
        self.next_step()

    async def cleanup(self) -> None:
        logger.info("No cleanup")
