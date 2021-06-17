
from asyncio import sleep

from app.test_engine.logger import test_engine_logger as logger
from app.test_engine.models import TestCase, TestStep
from app.user_prompt_support.prompt_request import PromptRequest
from app.user_prompt_support.user_prompt_manager import (
    PromptExchange,
    user_prompt_manager,
)
class TCDM2_2(TestCase):
    def create_test_steps(self) -> None:
        self.test_steps = [
            TestStep("Test Step 11.22.6-1: Query OperationalCerts"),
            TestStep("Test Step 11.22.6-2: Query Fabrics"),
            TestStep("Test Step 11.22.6-3: Query SupportedFabrics"),
            TestStep("Test Step 11.22.6-4: Query CommissionedFabrics"),
    ]

    async def setup(self) -> None:
        logger.info("No setup")

    async def execute(self) -> None:
        # 11.22.6-1: Query OperationalCerts
        # Verify it is of type List
        logger.info("11.22.6-1: Query OperationalCerts")
        self.next_step()

        # 11.22.6-2: Query Fabrics
        # Verify it is of type List
        logger.info("11.22.6-2: Query Fabrics")
        self.next_step()

        # 11.22.6-3: Query SupportedFabrics
        # Verify it is of type uint8
        logger.info("11.22.6-3: Query SupportedFabrics")
        self.next_step()

        # 11.22.6-4: Query CommissionedFabrics
        # Verify it is of type uint8
        logger.info("11.22.6-4: Query CommissionedFabrics")
        self.next_step()

    async def cleanup(self) -> None:
        logger.info("No cleanup")
