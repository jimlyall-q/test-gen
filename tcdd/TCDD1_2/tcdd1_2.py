
from asyncio import sleep

from app.test_engine.logger import test_engine_logger as logger
from app.test_engine.models import TestCase, TestStep
from app.user_prompt_support.prompt_request import PromptRequest
from app.user_prompt_support.user_prompt_manager import (
    PromptExchange,
    user_prompt_manager,
)
class TCDD1_2(TestCase):

    metadata = {
        "public_id": "TCDD1_2",
        "version": "0.0.1",
        "title": "",
        "description": "",
    }

    def create_test_steps(self) -> None:
        self.test_steps = [
            TestStep("Test Step Spec 5.1.3.1: Verify the first digit of the pairing code"),
            TestStep("Test Step Spec 5.1.3.1 - Table 35: If the pairing code is 11 digits/the VID_PID flag is not set, verify the encoded elements."),
            TestStep("Test Step Spec 5.1.3.1 - Table 36: If the pairing code is 21 digits/the VID_PID flag is set, verify the encoded elements."),
            TestStep("Test Step Spec 5.1.3.1- Check Digit (add in appendix?): Verify the check digit of the pairing code (digit 11 or 21) by entering the preceding digits in to the checksum script/Test Harness"),
        ]

    async def setup(self) -> None:
        logger.info("No setup")

    async def execute(self) -> None:
        # Spec 5.1.3.1: Verify the first digit of the pairing code
        # The first digit must be between 0 and 7
        # If the digit is between 0 and 3, the code length must be 11 digits (VID_PID flag not set)
        # 
        # If the digit is between 4 and 7, the code length must be 21 digits (VID_PID flag set)
        logger.info("Spec 5.1.3.1: Verify the first digit of the pairing code")
        self.next_step()

        # Spec 5.1.3.1 - Table 35: If the pairing code is 11 digits/the VID_PID flag is not set, verify the encoded elements.
        # Digits 2 through 6 must be between 00000 and 65535 Digits 7 through 10 must be between 0000 and 8191
        logger.info("Spec 5.1.3.1 - Table 35: If the pairing code is 11 digits/the VID_PID flag is not set, verify the encoded elements.")
        self.next_step()

        # Spec 5.1.3.1 - Table 36: If the pairing code is 21 digits/the VID_PID flag is set, verify the encoded elements.
        # Digits 2 through 6 must be between 00000 and 65535 Digits 7 through 10 must be between 0000 and 8191 Digits 11 through 15 must be between 00000 and 65535 Digits 16 through 20 must be between 00000 and 65535
        logger.info("Spec 5.1.3.1 - Table 36: If the pairing code is 21 digits/the VID_PID flag is set, verify the encoded elements.")
        self.next_step()

        # Spec 5.1.3.1- Check Digit (add in appendix?): Verify the "check digit" of the pairing code (digit 11 or 21) by entering the preceding digits in to the checksum script/Test Harness
        # Verify the final digit (11 or 21) of the pairing code printed on the DUT matches the generated digit by the script/Test Harness
        # 
        logger.info("Spec 5.1.3.1- Check Digit (add in appendix?): Verify the check digit of the pairing code (digit 11 or 21) by entering the preceding digits in to the checksum script/Test Harness")
        self.next_step()

    async def cleanup(self) -> None:
        logger.info("No cleanup")
