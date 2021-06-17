
from asyncio import sleep

from app.test_engine.logger import test_engine_logger as logger
from app.test_engine.models import TestCase, TestStep
from app.user_prompt_support.prompt_request import PromptRequest
from app.user_prompt_support.user_prompt_manager import (
    PromptExchange,
    user_prompt_manager,
)


class TCDD1_4(TestCase):

    metadata = {
        "public_id": "TCDD1_4",
        "version": "0.0.1",
        "title": "",
        "description": "",
    }

    def create_test_steps(self) -> None:
        self.test_steps = [
            TestStep("Test Step 5.1.5 Concatenation: If supported, scan larger QR code that will support the commissioning of all the DUTs in the packaging using the QR code scanner"),
        ]

    async def setup(self) -> None:
        logger.info("No setup")

    async def execute(self) -> None:
        # 5.1.5 Concatenation: If supported, scan larger QR code that will support the commissioning of all the DUTs in the packaging using the QR code scanner
        # Verify that each DUT onboarding payload is delimited with a * depending on the number of DUTs that will be onboarded
        # example: CH:<onboarding-base-38-content_bulb1>*<onboarding-base-38-content_bulb2>*<onboarding-base-38-content_bulb3>*<onboarding-base-38-content_bulb4>
        logger.info("5.1.5 Concatenation: If supported, scan larger QR code that will support the commissioning of all the DUTs in the packaging using the QR code scanner")
        self.next_step()

    async def cleanup(self) -> None:
        logger.info("No cleanup")
