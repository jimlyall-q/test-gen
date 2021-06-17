
from asyncio import sleep

from app.test_engine.logger import test_engine_logger as logger
from app.test_engine.models import TestCase, TestStep
from app.user_prompt_support.prompt_request import PromptRequest
from app.user_prompt_support.user_prompt_manager import (
    PromptExchange,
    user_prompt_manager,
)


class TCSC4_7(TestCase):

    metadata = {
        "public_id": "TCSC4_7",
        "version": "0.0.1",
        "title": "",
        "description": "",
    }

    def create_test_steps(self) -> None:
        self.test_steps = [
            TestStep(
                "Test Step DUT: DUT is instructed to start advertising its presence as a commissioner in the network"),
            TestStep("Test Step 4.2.3-1 TH: Check DNS-SD subtypes used by DUT"),
        ]

    async def setup(self) -> None:
        logger.info("No setup")

    async def execute(self) -> None:
        # DUT: DUT is instructed to start advertising its presence as a commissioner in the network
        # no desc
        logger.info(
            "DUT: DUT is instructed to start advertising its presence as a commissioner in the network")
        self.next_step()

        # 4.2.3-1 TH: Check DNS-SD subtypes used by DUT
        # DUT must publish AAAA records for each IPv6 address with the following:
        # - DNS-SD instance name must be 64-bit randomly selected ID expressed as a sixteen-char hex string with capital letters
        # - service type must be _matterd
        # _udp
        # - service domain is
        # local
        # For Unicast DNS such as used on Thread the service domain SHALL be as configured automatically by the Thread Border Router
        # - if optional _T<ddd> subtype is present, <ddd> represents device type from Data Model and must be represented as a variable length decimal number in ASCII without leading zeroes
        #
        # - target hostname is the 48bit MAC address expressed as a twelve capital letter hex string
        # If the MAC is randomized for privacy, the randomized version must be used each time
        #
        # - if optional VP key is present must contain at least Vendor ID and if Product ID is present, values must be separated by a + sign
        #
        # - if optional DT key is present must contain the device type identifier from Data Model Device Types and must be encoded as a variable length decimal ASCII number without leading zeroes
        # - if optional DN key is present must be a UTF-8 encoded string with a maximum length of 32B
        logger.info("4.2.3-1 TH: Check DNS-SD subtypes used by DUT")
        self.next_step()

    async def cleanup(self) -> None:
        logger.info("No cleanup")
