
from asyncio import sleep

from app.test_engine.logger import test_engine_logger as logger
from app.test_engine.models import TestCase, TestStep
from app.user_prompt_support.prompt_request import PromptRequest
from app.user_prompt_support.user_prompt_manager import (
    PromptExchange,
    user_prompt_manager,
)
class TCDD2_2(TestCase):

    metadata = {
        "public_id": "TCDD2_2",
        "version": "0.0.1",
        "title": "",
        "description": "",
    }

    def create_test_steps(self) -> None:
        self.test_steps = [
            TestStep("Test Step 5.4.3.1: If (PICS_BLE) TH start matter announcement procedure using BLE transport"),
            TestStep("Test Step 5.4.3.1: If (PICS_BLE) DUT start BLE scan"),
            TestStep("Test Step 5.4.3.1: If (PICS_BLE) DUT start scan in background using BLE transport"),
            TestStep("Test Step 5.4.3.1: If (PICS_BLE) TH start matter announcement using BLE transport"),
            TestStep("Test Step 5.4.3.1: missing test step"),
            TestStep("Test Step 5.4.3.2: If (PICS_WIFI) TH start SoftAP and begin matter announcement procedure"),
            TestStep("Test Step 5.4.3.2: If (PICS_WIFI) DUT start Wi-Fi scan"),
            TestStep("Test Step 5.4.3.2: If (PICS_WIFI) DUT scan using Wi-Fi in background"),
            TestStep("Test Step 5.4.3.2: If (PICS_WIFI) TH start SoftAP and begin matter announcement procedure"),
            TestStep("Test Step 5.4.3.2: DUT must find TH and provide onboarding data for validation."),
    ]

    async def setup(self) -> None:
        logger.info("No setup")

    async def execute(self) -> None:
        # 5.4.3.1: If (PICS_BLE) TH start matter announcement procedure using BLE transport
        # TH must start sending BLE advertisements
        # 
        logger.info("5.4.3.1: If (PICS_BLE) TH start matter announcement procedure using BLE transport")
        self.next_step()

        # 5.4.3.1: If (PICS_BLE) DUT start BLE scan
        # DUT must find TH and provide onboarding data to for validation
        # 
        # Pass Criteria: DUT is able to report the Onboarding payload as set on TH
        logger.info("5.4.3.1: If (PICS_BLE) DUT start BLE scan")
        self.next_step()

        # 5.4.3.1: If (PICS_BLE) DUT start scan in background using BLE transport
        # Missing description
        logger.info("5.4.3.1: If (PICS_BLE) DUT start scan in background using BLE transport")
        self.next_step()

        # 5.4.3.1: If (PICS_BLE) TH start matter announcement using BLE transport
        # TH must start sending BLE advertisements
        # 
        logger.info("5.4.3.1: If (PICS_BLE) TH start matter announcement using BLE transport")
        self.next_step()

        # 5.4.3.1: missing test step
        # DUT must find TH and provide onboarding data for validation
        # 
        # Pass Criteria: DUT is able to report the Onboarding payload as set on TH
        logger.info("5.4.3.1: missing test step")
        self.next_step()

        # 5.4.3.2: If (PICS_WIFI) TH start SoftAP and begin matter announcement procedure
        # TH must start SoftAP using Wi-Fi transport
        logger.info("5.4.3.2: If (PICS_WIFI) TH start SoftAP and begin matter announcement procedure")
        self.next_step()

        # 5.4.3.2: If (PICS_WIFI) DUT start Wi-Fi scan
        # DUT must find TH and provide onboarding data for validation
        # 
        # Pass Criteria: DUT is able to report the Onboarding payload as set on TH
        logger.info("5.4.3.2: If (PICS_WIFI) DUT start Wi-Fi scan")
        self.next_step()

        # 5.4.3.2: If (PICS_WIFI) DUT scan using Wi-Fi in background
        # missing description
        logger.info("5.4.3.2: If (PICS_WIFI) DUT scan using Wi-Fi in background")
        self.next_step()

        # 5.4.3.2: If (PICS_WIFI) TH start SoftAP and begin matter announcement procedure
        # TH must start SoftAP using Wi-Fi transport
        logger.info("5.4.3.2: If (PICS_WIFI) TH start SoftAP and begin matter announcement procedure")
        self.next_step()

        # 5.4.3.2: DUT must find TH and provide onboarding data for validation.
        # Pass Criteria: DUT is able to report the Onboarding payload as set on TH
        logger.info("5.4.3.2: DUT must find TH and provide onboarding data for validation.")
        self.next_step()
        
    async def cleanup(self) -> None:
        logger.info("No cleanup")
