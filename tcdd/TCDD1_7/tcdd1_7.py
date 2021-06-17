
from asyncio import sleep

from app.test_engine.logger import test_engine_logger as logger
from app.test_engine.models import TestCase, TestStep
from app.user_prompt_support.prompt_request import PromptRequest
from app.user_prompt_support.user_prompt_manager import (
    PromptExchange,
    user_prompt_manager,
)


class TCDD1_7(TestCase):

    metadata = {
        "public_id": "TCDD1_7",
        "version": "0.0.1",
        "title": "",
        "description": "",
    }

    def create_test_steps(self) -> None:
        self.test_steps = [
            TestStep(
                "Test Step 5.1.2.2: Scan the DUT’s QR code using a QR code reader"),
            TestStep("Test Step 5.1.2.2: Verify QR code version"),
        ]

    async def setup(self) -> None:
        logger.info("No setup")

    async def execute(self) -> None:
        # 5.1.2.2: Scan the DUT’s QR code using a QR code reader
        # Verify the QR code gets scanned successfully
        # Verify The QR code must be of sufficient size and contrast respective to surface material as to be readable with standard readers such as smartphones in normal lighting conditions
        # Refer to spec 5
        # 1
        # 2
        # 2 “Example QR Code Sizes and Payloads”
        logger.info("5.1.2.2: Scan the DUT’s QR code using a QR code reader")
        self.next_step()

        # 5.1.2.2: Verify QR code version
        # QR code version must be of version 1 or higher
        logger.info("5.1.2.2: Verify QR code version")
        self.next_step()

    async def cleanup(self) -> None:
        logger.info("No cleanup")
