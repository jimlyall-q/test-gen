
from asyncio import sleep

from app.test_engine.logger import test_engine_logger as logger
from app.test_engine.models import TestCase, TestStep
from app.user_prompt_support.prompt_request import PromptRequest
from app.user_prompt_support.user_prompt_manager import (
    PromptExchange,
    user_prompt_manager,
)


class TCSC2_2(TestCase):

    metadata = {
        "public_id": "TCSC2_2",
        "version": "0.0.1",
        "title": "",
        "description": "",
    }

    def create_test_steps(self) -> None:
        self.test_steps = [
            TestStep(
                "Test Step Initiator: Initiator uses I2RKey to encrypt and send a message"),
            TestStep(
                "Test Step Responder: Responder uses R2IKey to decrypt the message"),
            TestStep(
                "Test Step Responder: Responder uses I2RKey to encrypt and send a message"),
            TestStep(
                "Test Step Initiator: Initiator uses R2IKey to decrypt the message"),
            TestStep(
                "Test Step All: An error is encountered in initiator or responder decryption"),
        ]

    async def setup(self) -> None:
        logger.info("No setup")

    async def execute(self) -> None:
        # Initiator: Initiator uses I2RKey to encrypt and send a message
        # Responder receives the encrypted message
        logger.info(
            "Initiator: Initiator uses I2RKey to encrypt and send a message")
        self.next_step()

        # Responder: Responder uses R2IKey to decrypt the message
        # Responder is able to decrypt the message
        logger.info("Responder: Responder uses R2IKey to decrypt the message")
        self.next_step()

        # Responder: Responder uses I2RKey to encrypt and send a message
        # Initiator receives the encrypted message
        logger.info(
            "Responder: Responder uses I2RKey to encrypt and send a message")
        self.next_step()

        # Initiator: Initiator uses R2IKey to decrypt the message
        # Initiator is able to decrypt the message
        logger.info("Initiator: Initiator uses R2IKey to decrypt the message")
        self.next_step()

        # All: An error is encountered in initiator or responder decryption
        # Session is terminated and keys are cleared from memory
        logger.info(
            "All: An error is encountered in initiator or responder decryption")
        self.next_step()

    async def cleanup(self) -> None:
        logger.info("No cleanup")
