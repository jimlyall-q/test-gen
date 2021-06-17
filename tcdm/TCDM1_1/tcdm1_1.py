
from asyncio import sleep

from app.test_engine.logger import test_engine_logger as logger
from app.test_engine.models import TestCase, TestStep
from app.user_prompt_support.prompt_request import PromptRequest
from app.user_prompt_support.user_prompt_manager import (
    PromptExchange,
    user_prompt_manager,
)


class TCDM1_1(TestCase):

    def create_test_steps(self) -> None:
        self.test_steps = [
            TestStep("Test Step 11.2.3.1-1: TH queries Vendor Name"),
            TestStep("Test Step 11.2.3.1-2: TH queries VendorID"),
            TestStep("Test Step 11.2.3.1-3: TH queries Product Name"),
            TestStep("Test Step 11.2.3.1-4: TH queries ProductID"),
            TestStep("Test Step 11.2.3.1-5: TH queries UserLabel"),
            TestStep("Test Step 11.2.3.1-6: TH queries Location"),
            TestStep("Test Step 11.2.3.1-7: TH queries HardwareVersion"),
            TestStep("Test Step 11.2.3.1-8: TH queries HardwareVersionString"),
            TestStep("Test Step 11.2.3.1-9: TH queries SoftwareVersion"),
            TestStep("Test Step 11.2.3.1-10: TH queries SoftwareVersionString"),
            TestStep("Test Step 11.2.3.1-11: TH queries ManufacturingDate"),
            TestStep("Test Step 11.2.3.1-12: TH queries PartNumber"),
            TestStep("Test Step 11.2.3.1-13: TH queries ProductURL"),
            TestStep("Test Step 11.2.3.1-14: TH queries ProductLabel"),
            TestStep("Test Step 11.2.3.1-15: TH queries SerialNumber"),
            TestStep("Test Step 11.2.3.1-16: TH queries LocalConfigDisabled"),
        ]

    async def setup(self) -> None:
        logger.info("No setup")

    async def execute(self) -> None:
        # 11.2.3.1-1: TH queries Vendor Name
        # Verify it is of type string
        # Verify it is less than 32 chars
        logger.info("11.2.3.1-1: TH queries Vendor Name")
        self.next_step()

        # 11.2.3.1-2: TH queries VendorID
        # Verify it is of type uint16
        logger.info("11.2.3.1-2: TH queries VendorID")
        self.next_step()

        # 11.2.3.1-3: TH queries Product Name
        # Verify it is a string
        # Verify it is less than 32 chars
        logger.info("11.2.3.1-3: TH queries Product Name")
        self.next_step()

        # 11.2.3.1-4: TH queries ProductID
        # Verify it is of type uint16
        logger.info("11.2.3.1-4: TH queries ProductID")
        self.next_step()

        # 11.2.3.1-5: TH queries UserLabel
        # Verify it is of type string
        # Verify it is less than 32 chars
        logger.info("11.2.3.1-5: TH queries UserLabel")
        self.next_step()

        # 11.2.3.1-6: TH queries Location
        # Verify it is of type string
        # Verify it is less than 16 chars Verify it follows ISO 3166-1 alpha-2 code
        logger.info("11.2.3.1-6: TH queries Location")
        self.next_step()

        # 11.2.3.1-7: TH queries HardwareVersion
        # Verify it is of type uint16
        logger.info("11.2.3.1-7: TH queries HardwareVersion")
        self.next_step()

        # 11.2.3.1-8: TH queries HardwareVersionString
        # Verify it is of type string
        # Verify it is less than 64 chars
        logger.info("11.2.3.1-8: TH queries HardwareVersionString")
        self.next_step()

        # 11.2.3.1-9: TH queries SoftwareVersion
        # Verify it is of type uint32
        logger.info("11.2.3.1-9: TH queries SoftwareVersion")
        self.next_step()

        # 11.2.3.1-10: TH queries SoftwareVersionString
        # Verify it is of type string
        # Verify it is less than 64 chars of UTF-8 characters
        # Verify it uses 7-bit ASCII alphanumeric and punctuation characters
        logger.info("11.2.3.1-10: TH queries SoftwareVersionString")
        self.next_step()

        # 11.2.3.1-11: TH queries ManufacturingDate
        # Verify it is of type string
        # Verify it is less than 16 chars Verify if the first 8 characters specify date according to ISO 8601, i
        # e, YYYYMMDD
        #
        logger.info("11.2.3.1-11: TH queries ManufacturingDate")
        self.next_step()

        # 11.2.3.1-12: TH queries PartNumber
        # Verify it is of type string
        logger.info("11.2.3.1-12: TH queries PartNumber")
        self.next_step()

        # 11.2.3.1-13: TH queries ProductURL
        # Verify it is of type string
        # Verify it is less than 256 ASCII characters
        # Verify that it follows the syntax rules specified in RFC 3986
        logger.info("11.2.3.1-13: TH queries ProductURL")
        self.next_step()

        # 11.2.3.1-14: TH queries ProductLabel
        # Verify it is of type string
        # Verify it is less than 64 chars
        logger.info("11.2.3.1-14: TH queries ProductLabel")
        self.next_step()

        # 11.2.3.1-15: TH queries SerialNumber
        # Verify it is of type string
        # Verify it is less than 32 chars
        logger.info("11.2.3.1-15: TH queries SerialNumber")
        self.next_step()

        # 11.2.3.1-16: TH queries LocalConfigDisabled
        # Verify it is of type bool
        logger.info("11.2.3.1-16: TH queries LocalConfigDisabled")
        self.next_step()

    async def cleanup(self) -> None:
        logger.info("No cleanup")
