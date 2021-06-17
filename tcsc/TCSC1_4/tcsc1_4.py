
from asyncio import sleep

from app.test_engine.logger import test_engine_logger as logger
from app.test_engine.models import TestCase, TestStep
from app.user_prompt_support.prompt_request import PromptRequest
from app.user_prompt_support.user_prompt_manager import (
    PromptExchange,
    user_prompt_manager,
)


class TCSC1_4(TestCase):

    metadata = {
        "public_id": "TCSC1_4",
        "version": "0.0.1",
        "title": "",
        "description": "",
    }

    def create_test_steps(self) -> None:
        self.test_steps = [
            TestStep(
                "Test Step 4.13.4.2-1: Simulate TH to ignore all messages received by DUT (100% message loss)"),
            TestStep("Test Step 4.13.4.2-1: DUT sends messages to TH with Reliability bit set to 1, after the maximum number X of failed attempts has reached, DUT sends a message"),
        ]

    async def setup(self) -> None:
        logger.info("No setup")

    async def execute(self) -> None:
        # 4.13.4.2-1: Simulate TH to ignore all messages received by DUT (100% message loss)
        # no desc
        logger.info(
            "4.13.4.2-1: Simulate TH to ignore all messages received by DUT (100% message loss)")
        self.next_step()

        # 4.13.4.2-1: DUT sends messages to TH with Reliability bit set to 1, after the maximum number X of failed attempts has reached, DUT sends a message
        # Verify the Exchange associated with that last dropped message is closed and a CHIP_ERROR_MESSAGE_NOT_ACKNOWLEDGED error is signaled to the application layer on DUT
        logger.info("4.13.4.2-1: DUT sends messages to TH with Reliability bit set to 1, after the maximum number X of failed attempts has reached, DUT sends a message")
        self.next_step()

    async def cleanup(self) -> None:
        logger.info("No cleanup")
