
from asyncio import sleep

from app.test_engine.logger import test_engine_logger as logger
from app.test_engine.models import TestCase, TestStep
from app.user_prompt_support.prompt_request import PromptRequest
from app.user_prompt_support.user_prompt_manager import (
    PromptExchange,
    user_prompt_manager,
)


class TCSC1_2(TestCase):

    metadata = {
        "public_id": "TCSC1_2",
        "version": "0.0.1",
        "title": "",
        "description": "",
    }

    def create_test_steps(self) -> None:
        self.test_steps = [
            TestStep("Test Step 4.13.4-2: TH sends a single message to DUT with a message size equal to MRP_MAX_MESSAGE_SIZE and reliability bit set to 1"),
            TestStep("Test Step 4.13.4-2: TH sends a single message to DUT with a message size larger then MRP_MAX_MESSAGE_SIZE and reliability bit set to 1"),
        ]

    async def setup(self) -> None:
        logger.info("No setup")

    async def execute(self) -> None:
        # 4.13.4-2: TH sends a single message to DUT with a message size equal to MRP_MAX_MESSAGE_SIZE and reliability bit set to 1
        # Verify DUT responds with an acknowledgement of receipt
        #
        logger.info(
            "4.13.4-2: TH sends a single message to DUT with a message size equal to MRP_MAX_MESSAGE_SIZE and reliability bit set to 1")
        self.next_step()

        # 4.13.4-2: TH sends a single message to DUT with a message size larger then MRP_MAX_MESSAGE_SIZE and reliability bit set to 1
        # Verify DUT responds with an error message CHIP_ERROR_MESSAGE_TOO_LONG
        # Verify DUT aborts the MRP connection
        logger.info(
            "4.13.4-2: TH sends a single message to DUT with a message size larger then MRP_MAX_MESSAGE_SIZE and reliability bit set to 1")
        self.next_step()

    async def cleanup(self) -> None:
        logger.info("No cleanup")
