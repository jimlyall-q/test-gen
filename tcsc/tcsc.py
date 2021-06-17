
from app.test_engine.logger import test_engine_logger as logger
from app.test_engine.models import TestSuite


class TCSCTestSuite(TestSuite):
    metadata = {
        "public_id": "TCSCTestSuite",
        "version": "0.0.1",
        "title": "",
        "description": "",
    }


    async def setup(self) -> None:
        logger.info("No setup")

    async def cleanup(self) -> None:
        logger.info("No cleanup")
