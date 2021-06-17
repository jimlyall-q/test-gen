
from asyncio import sleep

from app.test_engine.logger import test_engine_logger as logger
from app.test_engine.models import TestCase, TestStep
from app.user_prompt_support.prompt_request import PromptRequest
from app.user_prompt_support.user_prompt_manager import (
    PromptExchange,
    user_prompt_manager,
)


class TCSC3_2(TestCase):

    metadata = {
        "public_id": "TCSC3_2",
        "version": "0.0.1",
        "title": "",
        "description": "",
    }

    def create_test_steps(self) -> None:
        self.test_steps = [
            TestStep("Test Step 4.12.2.3 Initiator: Initiator constructs and sends a TLV-encoded Sigma1_Resume message containing a random initiation value, destination identifier, resumption identifier, resumption message integrity check (MIC), and public key for its ephemeral key pair."),
            TestStep(
                "Test Step Responder: Responder validates the resumption identifier contained in the message."),
            TestStep("Test Step Responder: Responder constructs and sends a TLV-encoded Sigma2_Resume message containing a random responder value, responder resumption id, responder resumption MIC, and public key for its responder ephemeral key pair."),
            TestStep(
                "Test Step Initiator: Initiator validates the responder resumption MIC contained in the message."),
        ]

    async def setup(self) -> None:
        logger.info("No setup")

    async def execute(self) -> None:
        # 4.12.2.3 Initiator: Initiator constructs and sends a TLV-encoded Sigma1_Resume message containing a random initiation value, destination identifier, resumption identifier, resumption message integrity check (MIC), and public key for its ephemeral key pair.
        # Responder receives the message
        #
        logger.info("4.12.2.3 Initiator: Initiator constructs and sends a TLV-encoded Sigma1_Resume message containing a random initiation value, destination identifier, resumption identifier, resumption message integrity check (MIC), and public key for its ephemeral key pair.")
        self.next_step()

        # Responder: Responder validates the resumption identifier contained in the message.
        # If the resumption identifier matches the responder generated resumption identifier, the responder proceeds to generate a Sigma2_Resume message
        #
        # If the resumption identifier does not match the responder generated value, the responder treats the message as a Sigma1 message and follows the process in test case 6
        # 3
        # 1
        #
        logger.info(
            "Responder: Responder validates the resumption identifier contained in the message.")
        self.next_step()

        # Responder: Responder constructs and sends a TLV-encoded Sigma2_Resume message containing a random responder value, responder resumption id, responder resumption MIC, and public key for its responder ephemeral key pair.
        # Initiator receives the message
        #
        logger.info("Responder: Responder constructs and sends a TLV-encoded Sigma2_Resume message containing a random responder value, responder resumption id, responder resumption MIC, and public key for its responder ephemeral key pair.")
        self.next_step()

        # Initiator: Initiator validates the responder resumption MIC contained in the message.
        # If the responder resumption MIC matches the initiator generated resumption MIC, then the initiator generates session keys and the session is established
        #
        # If the responder resumption MIC does not match the initiator resumption MIC, then the initiator sends a SigmaError message with the InvalidParameter error code and performs no further processing
        #
        logger.info(
            "Initiator: Initiator validates the responder resumption MIC contained in the message.")
        self.next_step()

    async def cleanup(self) -> None:
        logger.info("No cleanup")
