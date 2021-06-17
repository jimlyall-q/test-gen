
from asyncio import sleep

from app.test_engine.logger import test_engine_logger as logger
from app.test_engine.models import TestCase, TestStep
from app.user_prompt_support.prompt_request import PromptRequest
from app.user_prompt_support.user_prompt_manager import (
    PromptExchange,
    user_prompt_manager,
)


class TCSC2_1(TestCase):

    metadata = {
        "public_id": "TCSC2_1",
        "version": "0.0.1",
        "title": "",
        "description": "",
    }

    def create_test_steps(self) -> None:
        self.test_steps = [
            TestStep(
                "Test Step Initiator: Initiator generates a 32 byte random value, constructs and sends PBKDFParamRequest"),
            TestStep("Test Step Responder: Responder generates a 32 byte random value, constructs crypto parameter set, and sends PBKDFParamResponse"),
            TestStep("Test Step Initiator: Initiator chooses a session identifier"),
            TestStep("Test Step Initiator: Initiator constructs and sends PAKE_1"),
            TestStep("Test Step Responder: Responder chooses a session identifier"),
            TestStep("Test Step Responder: Responder constructs and sends PAKE_2"),
            TestStep("Test Step Initiator: Initiator validates PAKE_2"),
            TestStep("Test Step Initiator: Initiator constructs and sends PAKE_3"),
            TestStep("Test Step Responder: Responder validates PAKE_3"),
        ]

    async def setup(self) -> None:
        logger.info("No setup")

    async def execute(self) -> None:
        # Initiator: Initiator generates a 32 byte random value, constructs and sends PBKDFParamRequest
        # Responder receives PBKDFParamRequest
        logger.info(
            "Initiator: Initiator generates a 32 byte random value, constructs and sends PBKDFParamRequest")
        self.next_step()

        # Responder: Responder generates a 32 byte random value, constructs crypto parameter set, and sends PBKDFParamResponse
        # Initiator receives PBKDFParamResponse
        logger.info(
            "Responder: Responder generates a 32 byte random value, constructs crypto parameter set, and sends PBKDFParamResponse")
        self.next_step()

        # Initiator: Initiator chooses a session identifier
        # Session identifier uses the session key key type (refer to spec 4
        # 3
        # 3
        # 7) Session identifier does not overlap with any existing PASE or CASE key identifier in use at the initiator
        logger.info("Initiator: Initiator chooses a session identifier")
        self.next_step()

        # Initiator: Initiator constructs and sends PAKE_1
        # Responder receives PAKE_1
        logger.info("Initiator: Initiator constructs and sends PAKE_1")
        self.next_step()

        # Responder: Responder chooses a session identifier
        # Session identifier uses the session key key type (refer to spec 4
        # 3
        # 3
        # 7) Session identifier does not overlap with any existing PASE or CASE key identifier in use at the initiator
        logger.info("Responder: Responder chooses a session identifier")
        self.next_step()

        # Responder: Responder constructs and sends PAKE_2
        # Initiator receives PAKE_2
        logger.info("Responder: Responder constructs and sends PAKE_2")
        self.next_step()

        # Initiator: Initiator validates PAKE_2
        # Verification succeeds
        # If If verification fails, the initiator responds with a PAKE_Error with error code InvalidKeyConfirmation
        logger.info("Initiator: Initiator validates PAKE_2")
        self.next_step()

        # Initiator: Initiator constructs and sends PAKE_3
        # Responder receives PAKE_3
        logger.info("Initiator: Initiator constructs and sends PAKE_3")
        self.next_step()

        # Responder: Responder validates PAKE_3
        # Verification succeeds
        # If If verification fails, the responder responds with a PAKE_Error with error code InvalidKeyConfirmation
        logger.info("Responder: Responder validates PAKE_3")
        self.next_step()

    async def cleanup(self) -> None:
        logger.info("No cleanup")
