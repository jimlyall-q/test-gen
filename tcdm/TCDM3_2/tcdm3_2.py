
from asyncio import sleep

from app.test_engine.logger import test_engine_logger as logger
from app.test_engine.models import TestCase, TestStep
from app.user_prompt_support.prompt_request import PromptRequest
from app.user_prompt_support.user_prompt_manager import (
    PromptExchange,
    user_prompt_manager,
)
class TCDM3_2(TestCase):
    def create_test_steps(self) -> None:
        self.test_steps = [
            TestStep("Test Step 11.9.8-1: DUT issues a ScanNetworks command"),
            TestStep("Test Step 11.9.8-2: if (PICS_WIFI) then DUT issues an AddWiFiNetwork command"),
            TestStep("Test Step 11.9.8-3: if (PICS_WIFI) then DUT issues an UpdateWiFiNetwork command"),
            TestStep("Test Step 11.9.8-4: if (PICS_THREAD) then DUT issues an AddThreadNetwork command"),
            TestStep("Test Step 11.9.8-5: if (PICS_THREAD) then DUT issues an UpdateThreadNetwork command"),
            TestStep("Test Step 11.9.8-6: if PICS_WIFI) OR (PICS_THREAD then DUT issues a RemoveNetwork command"),
            TestStep("Test Step 11.9.8-7: DUT issues an EnableNetwork command"),
            TestStep("Test Step 11.9.8-8: DUT issues a DisableNetwork command"),
            TestStep("Test Step 11.9.8-9: DUT issues a GetLastNetworkCommissioningResult command"),
    ]

    async def setup(self) -> None:
        logger.info("No setup")

    async def execute(self) -> None:
        # 11.9.8-1: DUT issues a ScanNetworks command
        # TH sends a ScanNetworksResponse and DUT properly receives that response with a list of scanned networks
        logger.info("11.9.8-1: DUT issues a ScanNetworks command")
        self.next_step()

        # 11.9.8-2: if (PICS_WIFI) then DUT issues an AddWiFiNetwork command
        # TH sends an AddWiFiNetworkResponse with a new WiFi network interface Id on the listed interfaces
        logger.info("11.9.8-2: if (PICS_WIFI) then DUT issues an AddWiFiNetwork command")
        self.next_step()

        # 11.9.8-3: if (PICS_WIFI) then DUT issues an UpdateWiFiNetwork command
        # TH sends an UpdateWiFiNetworkResponse with an updated WiFi network interface
        logger.info("11.9.8-3: if (PICS_WIFI) then DUT issues an UpdateWiFiNetwork command")
        self.next_step()

        # 11.9.8-4: if (PICS_THREAD) then DUT issues an AddThreadNetwork command
        # TH sends an AddThreadNetworkResponse with a new Thread network interface Id on the listed interfaces
        logger.info("11.9.8-4: if (PICS_THREAD) then DUT issues an AddThreadNetwork command")
        self.next_step()

        # 11.9.8-5: if (PICS_THREAD) then DUT issues an UpdateThreadNetwork command
        # TH sends an UpdateThreadNetworkResponse with an updated Thread network interface
        logger.info("11.9.8-5: if (PICS_THREAD) then DUT issues an UpdateThreadNetwork command")
        self.next_step()

        # 11.9.8-6: if PICS_WIFI) OR (PICS_THREAD then DUT issues a RemoveNetwork command
        # TH sends a RemoveNetworkResponse with an updated network interfaces list
        logger.info("11.9.8-6: if PICS_WIFI) OR (PICS_THREAD then DUT issues a RemoveNetwork command")
        self.next_step()

        # 11.9.8-7: DUT issues an EnableNetwork command
        # TH sends an EnableNetworkResponse and DUT properly receives that response with a list of enabled networks
        logger.info("11.9.8-7: DUT issues an EnableNetwork command")
        self.next_step()

        # 11.9.8-8: DUT issues a DisableNetwork command
        # TH sends a DisableNetworkResponse and DUT properly receives that response with a list of disabled networks
        logger.info("11.9.8-8: DUT issues a DisableNetwork command")
        self.next_step()

        # 11.9.8-9: DUT issues a GetLastNetworkCommissioningResult command
        # TH sends a response with the last Network Commissioning interface Id added to the list
        logger.info("11.9.8-9: DUT issues a GetLastNetworkCommissioningResult command")
        self.next_step()

    async def cleanup(self) -> None:
        logger.info("No cleanup")
