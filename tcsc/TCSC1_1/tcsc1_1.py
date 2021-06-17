
from asyncio import sleep

from app.test_engine.logger import test_engine_logger as logger
from app.test_engine.models import TestCase, TestStep
from app.user_prompt_support.prompt_request import PromptRequest
from app.user_prompt_support.user_prompt_manager import (
    PromptExchange,
    user_prompt_manager,
)


class TCSC1_1(TestCase):

    metadata = {
        "public_id": "TCSC1_1",
        "version": "0.0.1",
        "title": "",
        "description": "",
    }

    def create_test_steps(self) -> None:
        self.test_steps = [
            TestStep(
                "Test Step no ref: Configure TH/DUT to accept all packets received (no loss scenario)"),
            TestStep(
                "Test Step 4.14.3-1,4.3.4.1 (flags),4.3.4.6 (Ack Message Counter): TH sends a single reliable (R flag set) message to DUT"),
            TestStep(
                "Test Step no ref: Configure TH to ignore the first packet received (partial packet loss scenario)"),
            TestStep(
                "Test Step 4.14.3-1: TH sends a single reliable (R flag set) message to DUT"),
            TestStep("Test Step 4.14.3-1,4.14.10,4.2.2.5: Configure the TH to accept all packets received (no loss scenario). TH sends the same message as in step 2.b after waiting for MRP_RETRY_INTERVAL_IDLE milliseconds."),
            TestStep(
                "Test Step no ref: Configure TH to ignore all packets received (100% packet loss)"),
            TestStep(
                "Test Step 4.14.3-1: TH sends a single reliable (R flag set) message to DUT"),
            TestStep("Test Step 4.14.3-1,4.14.10: TH sends the same message as in step 3.b after waiting for MRP_RETRY_INTERVAL_IDLE milliseconds."),
        ]

    async def setup(self) -> None:
        logger.info("No setup")

    async def execute(self) -> None:
        # no ref: Configure TH/DUT to accept all packets received (no loss scenario)
        # no desc
        logger.info(
            "no ref: Configure TH/DUT to accept all packets received (no loss scenario)")
        self.next_step()

        # 4.14.3-1,4.3.4.1 (flags),4.3.4.6 (Ack Message Counter): TH sends a single reliable (R flag set) message to DUT
        # Verify DUT responds with an acknowledgement message with the A flag set and the Acknowledged Message Counter field set to the Message Counter of the received message
        #
        logger.info(
            "4.14.3-1,4.3.4.1 (flags),4.3.4.6 (Ack Message Counter): TH sends a single reliable (R flag set) message to DUT")
        self.next_step()

        # no ref: Configure TH to ignore the first packet received (partial packet loss scenario)
        # no desc
        logger.info(
            "no ref: Configure TH to ignore the first packet received (partial packet loss scenario)")
        self.next_step()

        # 4.14.3-1: TH sends a single reliable (R flag set) message to DUT
        # Verify TH ignores acknowledgement of receipt from DUT
        logger.info(
            "4.14.3-1: TH sends a single reliable (R flag set) message to DUT")
        self.next_step()

        # 4.14.3-1,4.14.10,4.2.2.5: Configure the TH to accept all packets received (no loss scenario). TH sends the same message as in step 2.b after waiting for MRP_RETRY_INTERVAL_IDLE milliseconds.
        # Verify TH receives an acknowledgement from the DUT with the A flag set and the Acknowledged Message Counter field set to the Message Counter of the received message
        #
        logger.info("4.14.3-1,4.14.10,4.2.2.5: Configure the TH to accept all packets received (no loss scenario). TH sends the same message as in step 2.b after waiting for MRP_RETRY_INTERVAL_IDLE milliseconds.")
        self.next_step()

        # no ref: Configure TH to ignore all packets received (100% packet loss)
        # no desc
        logger.info(
            "no ref: Configure TH to ignore all packets received (100% packet loss)")
        self.next_step()

        # 4.14.3-1: TH sends a single reliable (R flag set) message to DUT
        # Verify TH ignores acknowledgement of receipt from DUT
        logger.info(
            "4.14.3-1: TH sends a single reliable (R flag set) message to DUT")
        self.next_step()

        # 4.14.3-1,4.14.10: TH sends the same message as in step 3.b after waiting for MRP_RETRY_INTERVAL_IDLE milliseconds.
        # Verify TH ignores all acknowledgement of receipt from DUT until the maximum number of retransmissions have been sent, as defined by MRP_MAX_TRANSMISSIONS
        #
        logger.info(
            "4.14.3-1,4.14.10: TH sends the same message as in step 3.b after waiting for MRP_RETRY_INTERVAL_IDLE milliseconds.")
        self.next_step()

    async def cleanup(self) -> None:
        logger.info("No cleanup")
