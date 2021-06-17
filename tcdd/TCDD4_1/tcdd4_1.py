
from asyncio import sleep

from app.test_engine.logger import test_engine_logger as logger
from app.test_engine.models import TestCase, TestStep
from app.user_prompt_support.prompt_request import PromptRequest
from app.user_prompt_support.user_prompt_manager import (
    PromptExchange,
    user_prompt_manager,
)
class TCDD4_1(TestCase):

    metadata = {
        "public_id": "TCDD4_1",
        "version": "0.0.1",
        "title": "",
        "description": "",
    }

    def create_test_steps(self) -> None:
        self.test_steps = [
            TestStep("Test Step 5.5.2-1: TH starts the commissioning process"),
            TestStep("Test Step 5.5.2-1: DUT creates an Onboarding Payload"),
            TestStep("Test Step 5.5.2-2,5.5.2-3,5.5.2-4: DUT begins to advertise"),
            TestStep("Test Step 5.5.2-5, 5.5.2-6, 5.5.2-7: TH performs the Attestation procedure and include the Commissioning Certification"),
            TestStep("Test Step 5.5.2-8, 5.5.2-9, 5.5.2-11: TH selects an Operational Certificate Authority to use"),
            TestStep("Test Step 5.5.2-15: TH does not create an ACL (Access Control List) entry for the DUT (authorized Node)"),
            TestStep("Test Step 5.5.2-12, 5.5.2-14, 5.5.2-16, 5.5.2-17: TH creates an ACL (Access Control List) entry for the DUT (authorized Node)"),
            TestStep("Test Step 5.5.2-18: TH does not give to DUT enough privileges to delete the used operational CA in the process"),
            TestStep("Test Step 5.5.2-19: TH gives to DUT enough privileges to delete the used operational CA in the process"),
    ]

    async def setup(self) -> None:
        logger.info("No setup")

    async def execute(self) -> None:
        # 5.5.2-1: TH starts the commissioning process
        # DUT completes the commissioning process (DUT is the Commissionee)
        logger.info("5.5.2-1: TH starts the commissioning process")
        self.next_step()

        # 5.5.2-1: DUT creates an Onboarding Payload
        # The Onboarding Payload is well-formed and contains the following fields:
        logger.info("5.5.2-1: DUT creates an Onboarding Payload")
        self.next_step()

        # 5.5.2-2,5.5.2-3,5.5.2-4: DUT begins to advertise
        # TH discovers the DUT and performs a Password Authentication Session
        # After a successful Commissioning flow, the TH receives a valid Operational CSR from DUT
        logger.info("5.5.2-2,5.5.2-3,5.5.2-4: DUT begins to advertise")
        self.next_step()

        # 5.5.2-5, 5.5.2-6, 5.5.2-7: TH performs the Attestation procedure and include the Commissioning Certification
        # DUT can pass the attestation procedure or DUT can fail
        # 
        # If the attestation procedure fails, the DUT can send an error message
        # 
        logger.info("5.5.2-5, 5.5.2-6, 5.5.2-7: TH performs the Attestation procedure and include the Commissioning Certification")
        self.next_step()

        # 5.5.2-8, 5.5.2-9, 5.5.2-11: TH selects an Operational Certificate Authority to use
        # <to specify which one>
        # TH generates Operational Credential for the DUT
        # TH sends relevant Fabric information, Operational Certificate and Root CA Certificate to DUT
        # DUT receives and processes in a proper way all those certificates and stores in the DUT certificates repository
        # TH registers the DUT as an authorized Node
        logger.info("5.5.2-8, 5.5.2-9, 5.5.2-11: TH selects an Operational Certificate Authority to use")
        self.next_step()

        # 5.5.2-15: TH does not create an ACL (Access Control List) entry for the DUT (authorized Node)
        # DUT tries to initiate a secure connection by using a Certificate Authentication Session and creates an error response from its SigmaR1 message
        logger.info("5.5.2-15: TH does not create an ACL (Access Control List) entry for the DUT (authorized Node)")
        self.next_step()

        # 5.5.2-12, 5.5.2-14, 5.5.2-16, 5.5.2-17: TH creates an ACL (Access Control List) entry for the DUT (authorized Node)
        # DUT initiates a secure connection by using a Certificate Authentication Session
        # DUT could validate the Device Attestation information
        logger.info("5.5.2-12, 5.5.2-14, 5.5.2-16, 5.5.2-17: TH creates an ACL (Access Control List) entry for the DUT (authorized Node)")
        self.next_step()

        # 5.5.2-18: TH does not give to DUT enough privileges to delete the used operational CA in the process
        # DUT is not able to remove operational CA
        logger.info("5.5.2-18: TH does not give to DUT enough privileges to delete the used operational CA in the process")
        self.next_step()

        # 5.5.2-19: TH gives to DUT enough privileges to delete the used operational CA in the process
        # DUT removes operational CA
        logger.info("5.5.2-19: TH gives to DUT enough privileges to delete the used operational CA in the process")
        self.next_step()

    async def cleanup(self) -> None:
        logger.info("No cleanup")
