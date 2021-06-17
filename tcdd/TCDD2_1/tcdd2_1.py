
from asyncio import sleep

from app.test_engine.logger import test_engine_logger as logger
from app.test_engine.models import TestCase, TestStep
from app.user_prompt_support.prompt_request import PromptRequest
from app.user_prompt_support.user_prompt_manager import (
    PromptExchange,
    user_prompt_manager,
)


class TCDD2_1(TestCase):

    metadata = {
        "public_id": "TCDD2_1",
        "version": "0.0.1",
        "title": "",
        "description": "",
    }

    def create_test_steps(self) -> None:
        self.test_steps = [
            TestStep("Test Step 5.2.3-2: TH starts the commissioning process"),
            TestStep("Test Step 5.2.3-3: If (PICS_CHIP_DEV) then"),
            TestStep("Test Step 5.2.3-4, 5.2.3-5: if (PICS_BLE)"),
            TestStep("Test Step 5.2.3-9: if (PICS_BLE)"),
            TestStep("Test Step 5.2.3-11: if (PICS_BLE)"),
            TestStep("Test Step 5.2.3-12: if (PICS_BLE)"),
            TestStep("Test Step 5.2.3-4, 5.2.3-5: if (PICS_BLE)"),
            TestStep("Test Step 5.2.3-15: if (PICS_WIFI)"),
            TestStep("Test Step 5.2.3.-16: if (PICS_WIFI)"),
            TestStep("Test Step 5.2.3-19, 5.2.3-21: if (PICS_WIFI) & (PICS_IE)"),
        ]

    async def setup(self) -> None:
        logger.info("No setup")

    async def execute(self) -> None:
        # 5.2.3-2: TH starts the commissioning process
        # if (PICS_BLE) & (PICS_WIFI) & (PICS_ETH) then DUT selects BLE
        logger.info("5.2.3-2: TH starts the commissioning process")
        self.next_step()

        # 5.2.3-3: If (PICS_CHIP_DEV) then
        # If !(PICS_CHIP_DEV) then
        # If (PICS_DEV_LOCK) then
        # If (PICS_DEV_BARRIER) then
        # DUT starts announcing automatically
        # DUT does not start announcing
        # DUT does not start announcing
        # DUT does not start announcing
        logger.info("5.2.3-3: If (PICS_CHIP_DEV) then")
        self.next_step()

        # 5.2.3-4, 5.2.3-5: if (PICS_BLE)
        # TH does not respond to DUT and DUT keeps sending ADVs
        # DUT contains in the ADV:
        # >12-bit "Discriminator" field
        # DUT may contain in the ADV:
        # >16-bit "Vendor ID" field
        # >16-bit "Product ID" field
        # Length variable "Extended Data" field
        logger.info("5.2.3-4, 5.2.3-5: if (PICS_BLE)")
        self.next_step()

        # 5.2.3-9: if (PICS_BLE)
        # TH does not respond to DUT and DUT keeps sending ADVs
        # If (PICS_BLE) the ADV contains a GAP peripheral and uses the GAP General Discoverable mode
        logger.info("5.2.3-9: if (PICS_BLE)")
        self.next_step()

        # 5.2.3-11: if (PICS_BLE)
        # TH does not respond to DUT and DUT keeps sending ADVs
        # Between T0 and 30s, DUT should sends ADVs each 20ms to 60ms
        # Between 30s and 15min, DUT should sends ADVs each 150ms to 1200ms
        logger.info("5.2.3-11: if (PICS_BLE)")
        self.next_step()

        # 5.2.3-12: if (PICS_BLE)
        # TH does not respond to DUT and sends a power cycle command to DUT
        # DUT restarts the ADV sending process and uses a new address (the previous address must be stored by TH in the previous step)
        #
        logger.info("5.2.3-12: if (PICS_BLE)")
        self.next_step()

        # 5.2.3-4, 5.2.3-5: if (PICS_BLE)
        # TH does not respond to DUT and DUT keeps sending ADVs
        # TH waits at least 15 minutes
        # DUT stops sending ADV in 15 minutes or less
        #
        logger.info("5.2.3-4, 5.2.3-5: if (PICS_BLE)")
        self.next_step()

        # 5.2.3-15: if (PICS_WIFI)
        # TH scans and finds the DUT SSID
        # DUT SSID is not hidden and has the format: CHIP-ddd-vvvv-pppp
        logger.info("5.2.3-15: if (PICS_WIFI)")
        self.next_step()

        # 5.2.3.-16: if (PICS_WIFI)
        # TH scans and finds the DUT SSID
        # TH sends to DUT a 1st power cycle command (or reset manually)
        # TH sends to DUT a 2nd power cycle command (or reset manually)
        # DUT BSSID is random on each boot
        # DUT BSSID has the value X
        # After 1st power cycle, DUT BSSID is random with respect X (is not X, X+1, X-1, X*2, X/2, etc
        # )
        # After 2nd power cycle, DUT BSSID is random with respect X (is not X, X+1, X-1, X*2, X/2, etc
        # )
        # DUT bcast bit is set
        #
        # DUT locally-administered bit is set
        #
        logger.info("5.2.3.-16: if (PICS_WIFI)")
        self.next_step()

        # 5.2.3-19, 5.2.3-21: if (PICS_WIFI) & (PICS_IE)
        # TH scans and finds the DUT SSID
        # DUT IE is carried in the Wi-Fi soft-AP Beacon and Probe response frames
        # AND
        # DUT includes in that IE the following fields:
        # 0x00 (Reserved)
        # 0x01 (Device State)
        # 0x02 (Device Information)
        # 0x03 (Rotating Device Id)
        # 0x04 - 0xFF (Reserved)
        logger.info("5.2.3-19, 5.2.3-21: if (PICS_WIFI) & (PICS_IE)")
        self.next_step()

    async def cleanup(self) -> None:
        logger.info("No cleanup")
