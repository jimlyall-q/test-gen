
from asyncio import sleep

from app.test_engine.logger import test_engine_logger as logger
from app.test_engine.models import TestCase, TestStep
from app.user_prompt_support.prompt_request import PromptRequest
from app.user_prompt_support.user_prompt_manager import (
    PromptExchange,
    user_prompt_manager,
)


class TCSC1_3(TestCase):

    metadata = {
        "public_id": "TCSC1_3",
        "version": "0.0.1",
        "title": "",
        "description": "",
    }

    def create_test_steps(self) -> None:
        self.test_steps = [
            TestStep(
                "Test Step 4.13.7.1-1: TH sends a reliable (R flag set) MRP message to DUT that requires a data response."),
            TestStep(
                "Test Step 4.13.7.1-1: DUT must respond to the message with a MRP reply packet that piggybacks the ACK(A flag set)."),
            TestStep(
                "Test Step 4.13.7.1-2: TH sends a reliable (R flag set) MRP message to DUT that doesn’t require a data response."),
            TestStep(
                "Test Step 4.13.7.1-2: DUT must respond to the message with an ACK message."),
            TestStep(
                "Test Step 4.13.7.2-1: TH sends 5 unreliable (R flag not set) MRP messages to DUT that requires a data response."),
            TestStep("Test Step 4.13.7.2-2: DUT must respond to the message with a MRP reply packet that doesn’t piggyback the ACK(A flag not set)."),
            TestStep(
                "Test Step 4.13.7.3-1: TH sends a reliable MRP message that contains an invalid request with R flag set."),
        ]

    async def setup(self) -> None:
        logger.info("No setup")

    async def execute(self) -> None:
        # 4.13.7.1-1: TH sends a reliable (R flag set) MRP message to DUT that requires a data response.
        # DUT must receive the message
        #
        logger.info(
            "4.13.7.1-1: TH sends a reliable (R flag set) MRP message to DUT that requires a data response.")
        self.next_step()

        # 4.13.7.1-1: DUT must respond to the message with a MRP reply packet that piggybacks the ACK(A flag set).
        # DUT should piggyback the ACKs of the message in the reply to TH
        #
        logger.info(
            "4.13.7.1-1: DUT must respond to the message with a MRP reply packet that piggybacks the ACK(A flag set).")
        self.next_step()

        # 4.13.7.1-2: TH sends a reliable (R flag set) MRP message to DUT that doesn’t require a data response.
        # DUT must receive the message
        #
        logger.info(
            "4.13.7.1-2: TH sends a reliable (R flag set) MRP message to DUT that doesn’t require a data response.")
        self.next_step()

        # 4.13.7.1-2: DUT must respond to the message with an ACK message.
        # DUT must sent only the ACK packet to TH
        #
        logger.info(
            "4.13.7.1-2: DUT must respond to the message with an ACK message.")
        self.next_step()

        # 4.13.7.2-1: TH sends 5 unreliable (R flag not set) MRP messages to DUT that requires a data response.
        # DUT may receive the messages
        #
        logger.info(
            "4.13.7.2-1: TH sends 5 unreliable (R flag not set) MRP messages to DUT that requires a data response.")
        self.next_step()

        # 4.13.7.2-2: DUT must respond to the message with a MRP reply packet that doesn’t piggyback the ACK(A flag not set).
        # DUT should send only a MRP reply packet to TH with no ACK piggybacked or sent in a separate message
        #
        logger.info(
            "4.13.7.2-2: DUT must respond to the message with a MRP reply packet that doesn’t piggyback the ACK(A flag not set).")
        self.next_step()

        # 4.13.7.3-1: TH sends a reliable MRP message that contains an invalid request with R flag set.
        # DUT should send only an ACK to TH and no other packet signaling that the MRP session was closed
        #
        logger.info(
            "4.13.7.3-1: TH sends a reliable MRP message that contains an invalid request with R flag set.")
        self.next_step()

    async def cleanup(self) -> None:
        logger.info("No cleanup")
