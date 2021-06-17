
from asyncio import sleep

from app.test_engine.logger import test_engine_logger as logger
from app.test_engine.models import TestCase, TestStep
from app.user_prompt_support.prompt_request import PromptRequest
from app.user_prompt_support.user_prompt_manager import (
    PromptExchange,
    user_prompt_manager,
)


class TCSC4_6(TestCase):

    metadata = {
        "public_id": "TCSC4_6",
        "version": "0.0.1",
        "title": "",
        "description": "",
    }

    def create_test_steps(self) -> None:
        self.test_steps = [
            TestStep(
                "Test Step 4.2.2-1 TH1: TH1 is instructed to start advertising a service"),
            TestStep(
                "Test Step 4.2.2-1 DUT: DUT must register the service advertised by TH1 on Thread network"),
            TestStep(
                "Test Step 4.2.2-1 TH2: By any means, TH2 is instructed to discover all services in the CHIP network"),
        ]

    async def setup(self) -> None:
        logger.info("No setup")

    async def execute(self) -> None:
        # 4.2.2-1 TH1: TH1 is instructed to start advertising a service
        # TH1 should instruct the DUT about it’s service using SRP
        logger.info(
            "4.2.2-1 TH1: TH1 is instructed to start advertising a service")
        self.next_step()

        # 4.2.2-1 DUT: DUT must register the service advertised by TH1 on Thread network
        # DUT should register the service advertised by TH1
        logger.info(
            "4.2.2-1 DUT: DUT must register the service advertised by TH1 on Thread network")
        self.next_step()

        # 4.2.2-1 TH2: By any means, TH2 is instructed to discover all services in the CHIP network
        # TH2 should discover the service advertised by TH1
        # Each service must include the following:
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
        logger.info(
            "4.2.2-1 TH2: By any means, TH2 is instructed to discover all services in the CHIP network")
        self.next_step()

    async def cleanup(self) -> None:
        logger.info("No cleanup")
