
from app.test_engine.logger import test_engine_logger as logger
from app.test_engine.models import TestSuite


class TCDM1TestSuite(TestSuite):
    async def setup(self) -> None:
        logger.info("No setup")

    async def cleanup(self) -> None:
        logger.info("No cleanup")
