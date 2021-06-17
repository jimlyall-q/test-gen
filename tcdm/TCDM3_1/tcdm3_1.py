
from asyncio import sleep

from app.test_engine.logger import test_engine_logger as logger
from app.test_engine.models import TestCase, TestStep
from app.user_prompt_support.prompt_request import PromptRequest
from app.user_prompt_support.user_prompt_manager import (
    PromptExchange,
    user_prompt_manager,
)
class TCDM3_1(TestCase):
    def create_test_steps(self) -> None:
        self.test_steps = [
            TestStep("Test Step 11.9.7-1: if (PICS_WIFI) Query MaxNetworks"),
            TestStep("Test Step 11.9.7-2: if (PICS_WIFI) Query Networks"),
    ]

    async def setup(self) -> None:
        logger.info("No setup")

    async def execute(self) -> None:
        # 11.9.7-1: if (PICS_WIFI) Query MaxNetworks
        # Verify it is of type uint8
        logger.info("11.9.7-1: if (PICS_WIFI) Query MaxNetworks")
        self.next_step()

        # 11.9.7-2: if (PICS_WIFI) Query Networks
        # Verify it is of type List
        logger.info("11.9.7-2: if (PICS_WIFI) Query Networks")
        self.next_step()

    async def cleanup(self) -> None:
        logger.info("No cleanup")
