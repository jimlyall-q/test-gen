
from asyncio import sleep

from app.test_engine.logger import test_engine_logger as logger
from app.test_engine.models import TestCase, TestStep
from app.user_prompt_support.prompt_request import PromptRequest
from app.user_prompt_support.user_prompt_manager import (
    PromptExchange,
    user_prompt_manager,
)
class TCDD3_2(TestCase):

    metadata = {
        "public_id": "TCDD3_2",
        "version": "0.0.1",
        "title": "",
        "description": "",
    }

    def create_test_steps(self) -> None:
        self.test_steps = [
            TestStep("Test Step 5.4.6.1: Commissioner and Commissionee discover each other and connect via the discovery mode applicable for the DUT."),
            TestStep("Test Step 5.4.6.1: Establish encryption keys with Password Authenticated Session Establishment on the commissioning channel"),
            TestStep("Test Step 5.4.6.1: Commissioner arms Fail-safe timer on the Commissionee using ArmFailSafe command"),
            TestStep("Test Step 5.4.6.1: Commissioner configures the Commissionee UTC time, timezone, DST offset, and regulatory information at the Commissionee."),
            TestStep("Test Step 5.4.6.1: Commissioner establishes the authenticity of the Commissionee as a certified CHIP device."),
            TestStep("Test Step 5.4.6.1: Commissioner configures Fabric information using SetFabric command."),
            TestStep("Test Step 5.4.6.1: Commissioner requests operational CSR from Commissionee with OperationalCSRRequest command"),
            TestStep("Test Step 5.4.6.1: Commissioner generates or otherwise obtains an Operational Certificate containing Operational ID in response OperationalCSRRequest command using ecosystem-specific means"),
            TestStep("Test Step 5.4.6.1: Commissioner configures operational credentials"),
            TestStep("Test Step 5.4.6.1: Commissioner configures ACL."),
            TestStep("Test Step 5.4.6.1: Commissioner configures the operational network at the Commissionee."),
            TestStep("Test Step 5.4.6.1: Commissioner triggers the Commissionee to connect to the operational network"),
            TestStep("Test Step 5.4.6.1: Commissioner and Commissionee discover each other on the operational network using operational discovery"),
            TestStep("Test Step 5.4.6.1: Commissioner and Commissionee establish encryption keys with CASE"),
            TestStep("Test Step 5.4.6.1: Commissioner and Commissionee perform commissioning complete message exchange using CommissioningComplete command and CommissioningCompleteResponse command"),
            TestStep("Test Step 5.4.6.1: Same steps as 1.a. Force exit any step in 1.."),
    ]


    async def setup(self) -> None:
        logger.info("No setup")

    async def execute(self) -> None:
        # 5.4.6.1: Commissioner and Commissionee discover each other and connect via the discovery mode applicable for the DUT.
        # Commissioner and Commissionee can discover each other and connect to each other
        # 
        # Refer to Discovery test case 6
        # 2
        # 2 (DD-6
        # 2
        # 2) for validation steps
        # 
        logger.info("5.4.6.1: Commissioner and Commissionee discover each other and connect via the discovery mode applicable for the DUT.")
        self.next_step()

        # 5.4.6.1: Establish encryption keys with Password Authenticated Session Establishment on the commissioning channel
        # Refer to Secure Channel test case 6
        # 2
        # 1 (SC-6
        # 2
        # 1) for validation steps
        # 
        logger.info("5.4.6.1: Establish encryption keys with Password Authenticated Session Establishment on the commissioning channel")
        self.next_step()

        # 5.4.6.1: Commissioner arms Fail-safe timer on the Commissionee using ArmFailSafe command
        # Refer to General Commissioning Cluster test case TBD for validation steps (spec 8
        # 11
        # 7
        # 3, 8
        # 11
        # 6
        # 3)
        logger.info("5.4.6.1: Commissioner arms Fail-safe timer on the Commissionee using ArmFailSafe command")
        self.next_step()

        # 5.4.6.1: Commissioner configures the Commissionee UTC time, timezone, DST offset, and regulatory information at the Commissionee.
        # Refer to Time Synchronization Cluster test case TBD (spec 8
        # 18) and General Cluster test case TBD (spec 8
        # 11
        # 7
        # 1) for validation steps
        # 
        logger.info("5.4.6.1: Commissioner configures the Commissionee UTC time, timezone, DST offset, and regulatory information at the Commissionee.")
        self.next_step()

        # 5.4.6.1: Commissioner establishes the authenticity of the Commissionee as a certified CHIP device.
        # Refer to Device Attestation test case TBD (spec 6
        # 1
        # 3) for validation steps
        # 
        logger.info("5.4.6.1: Commissioner establishes the authenticity of the Commissionee as a certified CHIP device.")
        self.next_step()

        # 5.4.6.1: Commissioner configures Fabric information using SetFabric command.
        # Refer to General Commissioning Cluster test case TBD for validation steps (spec 8
        # 11
        # 7
        # 1)
        logger.info("5.4.6.1: Commissioner configures Fabric information using SetFabric command.")
        self.next_step()

        # 5.4.6.1: Commissioner requests operational CSR from Commissionee with OperationalCSRRequest command
        # Refer to Operational Credential Cluster test case TBD for validation steps (spec 8
        # 23
        # 7
        # 5)
        logger.info("5.4.6.1: Commissioner requests operational CSR from Commissionee with OperationalCSRRequest command")
        self.next_step()

        # 5.4.6.1: Commissioner generates or otherwise obtains an Operational Certificate containing Operational ID in response OperationalCSRRequest command using ecosystem-specific means
        # Refer to Operational Credential Cluster test case TBD for validation steps (spec 8
        # 23
        # 7
        # 5)
        logger.info("5.4.6.1: Commissioner generates or otherwise obtains an Operational Certificate containing Operational ID in response OperationalCSRRequest command using ecosystem-specific means")
        self.next_step()

        # 5.4.6.1: Commissioner configures operational credentials
        # Refer to Operational Credential Cluster test case TBD for validation steps (spec 8
        # 23
        # 7
        # 5)
        logger.info("5.4.6.1: Commissioner configures operational credentials")
        self.next_step()

        # 5.4.6.1: Commissioner configures ACL.
        # Refer to Access Control List Cluster test case TBD for validation steps (spec 7
        # 4
        # 9)
        logger.info("5.4.6.1: Commissioner configures ACL.")
        self.next_step()

        # 5.4.6.1: Commissioner configures the operational network at the Commissionee.
        # Refer to Network Commissioning Cluster test case TBD for validation steps (spec 8
        # 10
        # 8
        # *)
        logger.info("5.4.6.1: Commissioner configures the operational network at the Commissionee.")
        self.next_step()

        # 5.4.6.1: Commissioner triggers the Commissionee to connect to the operational network
        # Verify if the device is on the network by checking for the device on the network
        # 
        # Refer to Network Commissioning Cluster test case TBD for further validation steps (spec 8
        # 10
        # 8
        # 14)
        logger.info("5.4.6.1: Commissioner triggers the Commissionee to connect to the operational network")
        self.next_step()

        # 5.4.6.1: Commissioner and Commissionee discover each other on the operational network using operational discovery
        # Refer to Secure Channel test case TBD for further validation steps (spec 4
        # 2
        # 2)
        logger.info("5.4.6.1: Commissioner and Commissionee discover each other on the operational network using operational discovery")
        self.next_step()

        # 5.4.6.1: Commissioner and Commissionee establish encryption keys with CASE
        # Refer to Secure Channel test case TBD for further validation steps (spec 4
        # 13
        # 2)
        logger.info("5.4.6.1: Commissioner and Commissionee establish encryption keys with CASE")
        self.next_step()

        # 5.4.6.1: Commissioner and Commissionee perform commissioning complete message exchange using CommissioningComplete command and CommissioningCompleteResponse command
        # Verify if both Commissioner and Commissionee can talk to each other
        # 
        # Verify that the commissioning connection is terminated
        # 
        # Refer to General Commissioning Cluster test case TBD for validation steps (spec 8
        # 11
        # 7)
        logger.info("5.4.6.1: Commissioner and Commissionee perform commissioning complete message exchange using CommissioningComplete command and CommissioningCompleteResponse command")
        self.next_step()

        # 5.4.6.1: Same steps as 1.a. Force exit any step in 1..
        # The Commissioner and Commissionee terminate commissioning
        # Should go back to step 1a and start commissioning again
        # 
        logger.info("5.4.6.1: Same steps as 1.a. Force exit any step in 1..")
        self.next_step()
    async def cleanup(self) -> None:
        logger.info("No cleanup")
