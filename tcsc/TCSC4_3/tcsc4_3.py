
from asyncio import sleep

from app.test_engine.logger import test_engine_logger as logger
from app.test_engine.models import TestCase, TestStep
from app.user_prompt_support.prompt_request import PromptRequest
from app.user_prompt_support.user_prompt_manager import (
    PromptExchange,
    user_prompt_manager,
)


class TCSC4_3(TestCase):

    metadata = {
        "public_id": "TCSC4_3",
        "version": "0.0.1",
        "title": "",
        "description": "",
    }

    def create_test_steps(self) -> None:
        self.test_steps = [
            TestStep(
                "Test Step 4.2.2-1 TH: TH is instructed to start advertising a service using DNS-SD"),
            TestStep("Test Step 4.2.2-1 DUT: Scan for DNS-SD advertising"),
            TestStep(
                "Test Step 4.2.2-1 DUT: DUT is instructed to advertise it’s service"),
            TestStep("Test Step 4.2.2-1 TH: Scan for DNS-SD advertising"),
        ]

    async def setup(self) -> None:
        logger.info("No setup")

    async def execute(self) -> None:
        # 4.2.2-1 TH: TH is instructed to start advertising a service using DNS-SD
        # TH should start advertising its service
        logger.info(
            "4.2.2-1 TH: TH is instructed to start advertising a service using DNS-SD")
        self.next_step()

        # 4.2.2-1 DUT: Scan for DNS-SD advertising
        # Check TH advertising for:
        # - DNS-SD instance name must be 64-bit compressed FabricID
        # - service type must be _matter
        # _tcp
        # - service domain is
        # local
        # For Unicast DNS such as used on Thread the service domain SHALL be as configured automatically by the Thread Border Router
        # - target hostname is the 48bit MAC address expressed as a twelve capital letter hex string
        # If the MAC is randomized for privacy, the randomized version must be used each time
        #
        # - if optional key CRI is available it must have a maximum value of 3600000 and must be encoded as a decimal value omitting any leading zeroes
        # if key is not available or has an invalid value, the default MRP_RETRY_INTERVAL_IDLE value must be used
        # - if optional key CRA is available it must have a maximum value of 3600000 and must be encoded as a decimal value omitting any leading zeroes
        # if key is not available or has an invalid value, the default MRP_RETRY_INTERVAL_ACTIVE value must be used
        # - if optional key T is available it can have only 0 or 1 values and must be encoded as a decimal value omitting any leading zeroes
        # if key is not available or has an invalid value, the default value 1 must be used
        # TH must publish AAAA records for each IPv6 address upon which they are willing to accept CHIP messages
        #
        logger.info("4.2.2-1 DUT: Scan for DNS-SD advertising")
        self.next_step()

        # 4.2.2-1 DUT: DUT is instructed to advertise it’s service
        # DUT should start to advertise it’s service via DNS-SD
        logger.info("4.2.2-1 DUT: DUT is instructed to advertise it’s service")
        self.next_step()

        # 4.2.2-1 TH: Scan for DNS-SD advertising
        # Check DUT advertising for:
        # - DNS-SD instance name must be 64-bit compressed FabricID
        # - service type must be _matter
        # _tcp
        # - service domain is
        # local
        # For Unicast DNS such as used on Thread the service domain SHALL be as configured automatically by the Thread Border Router
        # - target hostname is the 48bit MAC address expressed as a twelve capital letter hex string
        # If the MAC is randomized for privacy, the randomized version must be used each time
        #
        # - if optional key CRI is available it must have a maximum value of 3600000 and must be encoded as a decimal value omitting any leading zeroes
        # if key is not available or has an invalid value, the default MRP_RETRY_INTERVAL_IDLE value must be used
        # - if optional key CRA is available it must have a maximum value of 3600000 and must be encoded as a decimal value omitting any leading zeroes
        # if key is not available or has an invalid value, the default MRP_RETRY_INTERVAL_ACTIVE value must be used
        # - if optional key T is available it can have only 0 or 1 values and must be encoded as a decimal value omitting any leading zeroes
        # if key is not available or has an invalid value, the default value 1 must be used
        # DUT must publish AAAA records for each IPv6 address upon which they are willing to accept CHIP messages
        #
        logger.info("4.2.2-1 TH: Scan for DNS-SD advertising")
        self.next_step()

    async def cleanup(self) -> None:
        logger.info("No cleanup")
