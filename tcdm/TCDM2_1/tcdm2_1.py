
from asyncio import sleep

from app.test_engine.logger import test_engine_logger as logger
from app.test_engine.models import TestCase, TestStep
from app.user_prompt_support.prompt_request import PromptRequest
from app.user_prompt_support.user_prompt_manager import (
    PromptExchange,
    user_prompt_manager,
)


class TCDM2_1(TestCase):

    def create_test_steps(self) -> None:
        self.test_steps = [
            TestStep("Test Step 11.22.7: Start commissioning between DUT and TH"),
            TestStep("Test Step 11.22.7: DUT Sends Attestation Request to TH"),
            TestStep(
                "Test Step 11.22.7: DUT Sends Attestation Certificate Chain Request to TH"),
            TestStep("Test Step 11.22.7: DUT Sends CSR Request to TH"),
            TestStep("Test Step 11.22.7: DUT Sends Add Op Cert Request to TH"),
            TestStep("Test Step 11.22.7: DUT Sends Add Op Cert Request to TH"),
            TestStep("Test Step 11.22.7: DUT Sends Update Op Cert Request to TH"),
            TestStep(
                "Test Step 11.22.7: DUT Sends Update Op Cert Request to TH with a Fabric Label not already in use"),
            TestStep(
                "Test Step 11.22.7: DUT Sends Update Op Cert Request to TH with a Fabric label already in use"),
            TestStep(
                "Test Step 11.22.7: DUT Sends Remove Fabric Request to TH with a non-Valid Fabric ID"),
            TestStep(
                "Test Step 11.22.7.12: DUT Sends Remove Fabric Request to TH with a non-Valid Fabric index"),
            TestStep(
                "Test Step 11.22.7.12: DUT Sends Remove Fabric Request to TH with a non-Valid Fabric ID"),
    ]

    async def setup(self) -> None:
        logger.info("No setup")

    async def execute(self) -> None:
        # 11.22.7: Start commissioning between DUT and TH
        # No outcome
        logger.info("11.22.7: Start commissioning between DUT and TH")
        self.next_step()

        # 11.22.7: DUT Sends Attestation Request to TH
        # Verify the request is successful and TH responds with Attestation Response
        #
        logger.info("11.22.7: DUT Sends Attestation Request to TH")
        self.next_step()

        # 11.22.7: DUT Sends Attestation Certificate Chain Request to TH
        # Verify the request is successful and TH responds with Certificate Chain Response
        #
        logger.info("11.22.7: DUT Sends Attestation Certificate Chain Request to TH")
        self.next_step()

        # 11.22.7: DUT Sends CSR Request to TH
        # Verify the request is successful and TH responds with CSR Response
        #
        logger.info("11.22.7: DUT Sends CSR Request to TH")
        self.next_step()

        # 11.22.7: DUT Sends Add Op Cert Request to TH
        # Verify the request is successful and TH responds with Op Cert Response
        #
        logger.info("11.22.7: DUT Sends Add Op Cert Request to TH")
        self.next_step()

        # 11.22.7: DUT Sends Add Op Cert Request to TH
        # Verify DUT and TH are on the same Fabric
        logger.info("11.22.7: DUT Sends Add Op Cert Request to TH")
        self.next_step()

        # 11.22.7: DUT Sends Update Op Cert Request to TH
        # Verify the request is successful and TH responds with Op Cert Response
        #
        logger.info("11.22.7: DUT Sends Update Op Cert Request to TH")
        self.next_step()

        # 11.22.7: DUT Sends Update Op Cert Request to TH with a Fabric Label not already in use
        # Verify the request is successful and TH responds with Op Cert Response
        #
        logger.info("11.22.7: DUT Sends Update Op Cert Request to TH with a Fabric Label not already in use")
        self.next_step()

        # 11.22.7: DUT Sends Update Op Cert Request to TH with a Fabric label already in use
        # Verify the request is successful and TH responds with Op Cert Response including an error “Label Conflict”
        logger.info("11.22.7: DUT Sends Update Op Cert Request to TH with a Fabric label already in use")
        self.next_step()

        # 11.22.7: DUT Sends Remove Fabric Request to TH with a non-Valid Fabric ID
        # Verify the request is successful and TH responds with Op Cert Response including an error “Invalid Fabric Index”
        #
        logger.info("11.22.7: DUT Sends Remove Fabric Request to TH with a non-Valid Fabric ID")
        self.next_step()

        # 11.22.7.12: DUT Sends Remove Fabric Request to TH with a non-Valid Fabric index
        # Verify the request is successful and TH responds with Op Cert Response including an error “Invalid Fabric Index”
        logger.info("11.22.7.12: DUT Sends Remove Fabric Request to TH with a non-Valid Fabric index")
        self.next_step()

        # 11.22.7.12: DUT Sends Remove Fabric Request to TH with a non-Valid Fabric ID
        # Verify the request is successful and TH responds with Op Cert Response
        logger.info("11.22.7.12: DUT Sends Remove Fabric Request to TH with a non-Valid Fabric ID")
        self.next_step()

    async def cleanup(self) -> None:
        logger.info("No cleanup")
