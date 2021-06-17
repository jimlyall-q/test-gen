
from asyncio import sleep

from app.test_engine.logger import test_engine_logger as logger
from app.test_engine.models import TestCase, TestStep
from app.user_prompt_support.prompt_request import PromptRequest
from app.user_prompt_support.user_prompt_manager import (
    PromptExchange,
    user_prompt_manager,
)


class TCDD1_6(TestCase):

    metadata = {
        "public_id": "TCDD1_6",
        "version": "0.0.1",
        "title": "",
        "description": "",
    }

    def create_test_steps(self) -> None:
        self.test_steps = [
            TestStep(
                "Test Step 5.1.7: Keep the DUT in packaging and bring in NFC scanner close to packaging."),
            TestStep("Test Step 5.1.7: Unpack DUT from its packaging, make sure DUT is not powered on and do not put the DUT in pairing mode. Bring in NFC scanner close to the DUT’s NFC tag"),
            TestStep(
                "Test Step 5.1.7: Power on DUT and do not put the DUT in pairing mode. Bring in NFC scanner close to the DUT’s NFC tag"),
            TestStep(
                "Test Step 5.1.7: DUT must have an explicit trigger of the the NFC pairing mode"),
            TestStep(
                "Test Step 5.1.7: Power on DUT and put the DUT in pairing mode. Bring in NFC scanner close to NFC tag"),
            TestStep(
                "Test Step 5.1.7: Wait for the pairing mode to expire on accessory"),
            TestStep(
                "Test Step 5.1.5: For Read only Tags, try to write using NFC tool a payload to DUT"),
            TestStep(
                "Test Step 5.1.5: For Programmable Tag, NFC tag must be read only OTA. Try to write using NFC tool a payload to DUT"),
            TestStep(
                "Test Step 5.1.5: Optional — For Programmable Tag, NFC tag may be reconfigured using wired means"),
            TestStep(
                "Test Step 5.1.5: Using NFC reader - read NFC tag Reader type"),
        ]

    async def setup(self) -> None:
        logger.info("No setup")

    async def execute(self) -> None:
        # 5.1.7: Keep the DUT in packaging and bring in NFC scanner close to packaging.
        # Bring in the NFC scanner close to the DUT packaging and verify the DUT’s NFC tag containing Onboarding Payload is not scannable and readable
        logger.info(
            "5.1.7: Keep the DUT in packaging and bring in NFC scanner close to packaging.")
        self.next_step()

        # 5.1.7: Unpack DUT from its packaging, make sure DUT is not powered on and do not put the DUT in pairing mode. Bring in NFC scanner close to the DUT’s NFC tag
        # Verify that the programmable tag does not advertise the Onboarding Payload and cannot be modified over the air
        #
        logger.info("5.1.7: Unpack DUT from its packaging, make sure DUT is not powered on and do not put the DUT in pairing mode. Bring in NFC scanner close to the DUT’s NFC tag")
        self.next_step()

        # 5.1.7: Power on DUT and do not put the DUT in pairing mode. Bring in NFC scanner close to the DUT’s NFC tag
        # Verify programmable tag when not in pairing mode, does not advertise the Onboarding Payload and cannot be modified over the air
        #
        logger.info(
            "5.1.7: Power on DUT and do not put the DUT in pairing mode. Bring in NFC scanner close to the DUT’s NFC tag")
        self.next_step()

        # 5.1.7: DUT must have an explicit trigger of the the NFC pairing mode
        # Verify the DUT has an explicit trigger (a physical action that enables the NFC pairing flow)
        logger.info(
            "5.1.7: DUT must have an explicit trigger of the the NFC pairing mode")
        self.next_step()

        # 5.1.7: Power on DUT and put the DUT in pairing mode. Bring in NFC scanner close to NFC tag
        # Verify the complete onboarding payload is presented
        logger.info(
            "5.1.7: Power on DUT and put the DUT in pairing mode. Bring in NFC scanner close to NFC tag")
        self.next_step()

        # 5.1.7: Wait for the pairing mode to expire on accessory
        # Verify the DUT terminates the advertising upon termination of pairing mode
        #
        logger.info("5.1.7: Wait for the pairing mode to expire on accessory")
        self.next_step()

        # 5.1.5: For Read only Tags, try to write using NFC tool a payload to DUT
        # Verify it is rejected and payload can’t be written to tag
        logger.info(
            "5.1.5: For Read only Tags, try to write using NFC tool a payload to DUT")
        self.next_step()

        # 5.1.5: For Programmable Tag, NFC tag must be read only OTA. Try to write using NFC tool a payload to DUT
        # Verify it is rejected and payload can’t be written to tag
        logger.info(
            "5.1.5: For Programmable Tag, NFC tag must be read only OTA. Try to write using NFC tool a payload to DUT")
        self.next_step()

        # 5.1.5: Optional — For Programmable Tag, NFC tag may be reconfigured using wired means
        # Verify payload can be written through wired means
        logger.info(
            "5.1.5: Optional — For Programmable Tag, NFC tag may be reconfigured using wired means")
        self.next_step()

        # 5.1.5: Using NFC reader - read NFC tag Reader type
        # Verify the NFC tag on a device is Type 2 or greater
        logger.info("5.1.5: Using NFC reader - read NFC tag Reader type")
        self.next_step()

    async def cleanup(self) -> None:
        logger.info("No cleanup")
