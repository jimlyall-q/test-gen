
from asyncio import sleep

from app.test_engine.logger import test_engine_logger as logger
from app.test_engine.models import TestCase, TestStep
from app.user_prompt_support.prompt_request import PromptRequest
from app.user_prompt_support.user_prompt_manager import (
    PromptExchange,
    user_prompt_manager,
)

class TCDM1_2(TestCase):

    def create_test_steps(self) -> None:
        self.test_steps = [
            TestStep("Test Step 11.2.3.2-0: Reboot the DUT"),
            TestStep("Test Step 11.2.3.2-1: Shut down the DUT"),
            TestStep("Test Step 11.2.3.2-1: Send events/messages to DUT from TH"),
            TestStep("Test Step 11.2.3.2-2: Factory Reset the DUT"),
    ]
    async def setup(self) -> None:
        logger.info("No setup")

    async def execute(self) -> None:
        # 11.2.3.2-0: Reboot the DUT
        # Verify that the DUT sends the StartUp event before other events to TH
        logger.info("11.2.3.2-0: Reboot the DUT")
        self.next_step()

        # 11.2.3.2-1: Shut down the DUT
        # Verify that the DUT sends the ShutDown event to TH before shutting down
        # No other event from the DUT should be sent to TH
        # 
        logger.info("11.2.3.2-1: Shut down the DUT")
        self.next_step()

        # 11.2.3.2-1: Send events/messages to DUT from TH
        # Verify that the messages sent to the DUT are dropped
        logger.info("11.2.3.2-1: Send events/messages to DUT from TH")
        self.next_step()

        # 11.2.3.2-2: Factory Reset the DUT
        # Verify that the DUT sends the Leave event to TH
        # No more events from DUT should be sent
        # Verify incoming messages to DUT are dropped
        # 
        logger.info("11.2.3.2-2: Factory Reset the DUT")
        self.next_step()

    async def cleanup(self) -> None:
        logger.info("No cleanup")
