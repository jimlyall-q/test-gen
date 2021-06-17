
from asyncio import sleep

from app.test_engine.logger import test_engine_logger as logger
from app.test_engine.models import TestCase, TestStep
from app.user_prompt_support.prompt_request import PromptRequest
from app.user_prompt_support.user_prompt_manager import (
    PromptExchange,
    user_prompt_manager,
)


class TCDD1_3(TestCase):

    metadata = {
        "public_id": "TCDD1_3",
        "version": "0.0.1",
        "title": "",
        "description": "",
    }

    def create_test_steps(self) -> None:
        self.test_steps = [
            TestStep(
                "Test Step 0.0.0-1: Power up the DUT and put the DUT in pairing mode"),
            TestStep(
                "Test Step 0.0.0-1: Bring the NFC code reader close to the DUT"),
            TestStep(
                "Test Step 5.1.2 Table 31: Verify the QR code payload version"),
            TestStep(
                "Test Step 0.0.0-1: Verify 8-bit Rendezvous Capabilities bit mask"),
            TestStep("Test Step 0.0.0-1: Verify the 12-bit discriminator bit mask"),
            TestStep(
                "Test Step 0.0.0-1: Verify the onboarding payload contains a 27-bit Passcode"),
            TestStep("Test Step 0.0.0-1: Verify passcode is valid"),
            TestStep("Test Step 0.0.0-1: Verify QR code prefix"),
            TestStep("Test Step 0.0.0-1: Verify Vendor ID and Product ID"),
            TestStep(
                "Test Step 5.1.2 Table 31: Verify the packed binary data structure"),
            TestStep("Test Step 5.1.3: Verify Custom payload support"),
        ]

    async def setup(self) -> None:
        logger.info("No setup")

    async def execute(self) -> None:
        # 0.0.0-1: Power up the DUT and put the DUT in pairing mode
        # No desc
        logger.info("0.0.0-1: Power up the DUT and put the DUT in pairing mode")
        self.next_step()

        # 0.0.0-1: Bring the NFC code reader close to the DUT
        # No desc
        logger.info("0.0.0-1: Bring the NFC code reader close to the DUT")
        self.next_step()

        # 5.1.2 Table 31: Verify the QR code payload version
        # Verify the NFC code payload version is ‘000’
        #
        logger.info("5.1.2 Table 31: Verify the QR code payload version")
        self.next_step()

        # 0.0.0-1: Verify 8-bit Rendezvous Capabilities bit mask
        # Verify the onboarding payload contains an 8-bit Rendezvous Capabilities bit mask describing the transports which can be used for commissioning the DUT
        # Refer to spec 5
        # 1
        # 2 Table 32 for specifics of the bit mask
        #
        logger.info("0.0.0-1: Verify 8-bit Rendezvous Capabilities bit mask")
        self.next_step()

        # 0.0.0-1: Verify the 12-bit discriminator bit mask
        # Verify the 12-bit discriminator matches the value which a device advertises during commissioning
        #
        logger.info("0.0.0-1: Verify the 12-bit discriminator bit mask")
        self.next_step()

        # 0.0.0-1: Verify the onboarding payload contains a 27-bit Passcode
        # Verify the 27-bit unsigned integer encodes an 8-digit decimal numeric value and shall be a value between 0x0000001 to 0x5f5e0fe (00000001 to 99999998)
        logger.info(
            "0.0.0-1: Verify the onboarding payload contains a 27-bit Passcode")
        self.next_step()

        # 0.0.0-1: Verify passcode is valid
        # Verify passcode does not use any trivial values: 00000000, 11111111, 22222222, 33333333, 44444444, 55555555, 66666666, 77777777, 88888888, 99999999, 12345678, 87654321
        # Verify Passcode is not derived from public information as serial number, manufacturer date, MAC address, region of origin etc
        #
        logger.info("0.0.0-1: Verify passcode is valid")
        self.next_step()

        # 0.0.0-1: Verify QR code prefix
        # Verify QR code prefix is "MT:"
        logger.info("0.0.0-1: Verify QR code prefix")
        self.next_step()

        # 0.0.0-1: Verify Vendor ID and Product ID
        # Verify Vendor ID and Product ID match the values submitted by manufacturer in Distributed Compliance Ledger
        logger.info("0.0.0-1: Verify Vendor ID and Product ID")
        self.next_step()

        # 5.1.2 Table 31: Verify the packed binary data structure
        # Verify the packed binary data structure is padded with ‘0’ bits at the end of the structure to the nearest byte boundary
        #
        logger.info("5.1.2 Table 31: Verify the packed binary data structure")
        self.next_step()

        # 5.1.3: Verify Custom payload support
        # If set to 1, verify vendor has provided a commissioning URL which can be retrieved from the Distributed Compliance Ledger (refer to spec 8
        # 21) using the Vendor ID and Product ID pairing
        #
        # If set to 0, verify no additional information can be retrieved from Compliance ledger
        logger.info("5.1.3: Verify Custom payload support")
        self.next_step()

    async def cleanup(self) -> None:
        logger.info("No cleanup")
