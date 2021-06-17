
from asyncio import sleep

from app.test_engine.logger import test_engine_logger as logger
from app.test_engine.models import TestCase, TestStep
from app.user_prompt_support.prompt_request import PromptRequest
from app.user_prompt_support.user_prompt_manager import (
    PromptExchange,
    user_prompt_manager,
)


class TCSC4_1(TestCase):

    metadata = {
        "public_id": "TCSC4_1",
        "version": "0.0.1",
        "title": "",
        "description": "",
    }

    def create_test_steps(self) -> None:
        self.test_steps = [
            TestStep(
                "Test Step 4.2.1-1 DUT: If (PICS_WIFI) DUT should provide DHCPv4 leases over SoftAP"),
            TestStep(
                "Test Step DUT: DUT is put in Commissioning Mode and starts advertising its availability for commissioning"),
            TestStep("Test Step 4.2.1-5: TH"),
            TestStep(
                "Test Step DUT: Reboot DUT, put in non Commissioning Mode and start advertising its availability for commissioning"),
            TestStep("Test Step 4.2.1-5 TH: Check DNS-SD subtypes used by DUT"),
        ]

    async def setup(self) -> None:
        logger.info("No setup")

    async def execute(self) -> None:
        # TODO TABLE is not correct
        # 4.2.1-1 DUT: If (PICS_WIFI) DUT should provide DHCPv4 leases over SoftAP
        # Connecting to DUT’s SoftAP the Wi-Fi STA should obtain a DHCPv4 lease
        logger.info(
            "4.2.1-1 DUT: If (PICS_WIFI) DUT should provide DHCPv4 leases over SoftAP")
        self.next_step()

        # DUT: DUT is put in Commissioning Mode and starts advertising its availability for commissioning
        # no desc
        logger.info(
            "DUT: DUT is put in Commissioning Mode and starts advertising its availability for commissioning")
        self.next_step()

        # 4.2.1-5: TH
        # Check DNS-SD subtypes used by DUT
        # Check DUT advertising for:
        # - DNS-SD instance name must be 64-bit randomly selected ID expressed as a sixteen-char hex string with capital letters
        # - service type must be _matterc
        # _udp
        # - service domain is
        # local
        # For Unicast DNS such as used on Thread the service domain SHALL be as configured automatically by the Thread Border Router
        # - target hostname is the 48bit MAC address expressed as a twelve capital letter hex string
        # If the MAC is randomized for privacy, the randomized version must be used each time
        # - subtype _S<dd> 4-bit short discriminator, encoded as a variable-length decimal number in ASCII text, omitting any leading zeroes
        # - subtype _L<dddd> 12-bit long discriminator, encoded as a variable-length decimal number in ASCII text, omitting any leading zeroes
        # - subtype _C<d> must have a value of 1
        # - subtype _A1 must be present
        # - if optional subtype _V<ddddd> is present must be 16-bit vendor id, encoded as a variable-length decimal number in ASCII text, omitting any leading zeroes
        # - if optional subtype _T<ddd> is present, <ddd> represents device type from Data Model and must be represented as a variable length decimal number in ASCII without leading zeroes
        # - key D must be present and represents the discriminator which must be encoded as a variable-lenght decimal value with up to 4 digits omitting any leading zeroes
        # - if optional VP key is present must contain at least Vendor ID and if Product ID is present, values must be separated by a + sign
        #
        # - key AP=1 must be present
        # - key CM=1 must be present
        # - if optional DT key is present must contain the device type identifier from Data Model Device Types and must be encoded as a variable length decimal ASCII number without leading zeroes
        # - if optional DN key is present must be a UTF-8 encoded string with a maximum length of 32B
        # - if optional key RI is present must include the Rotating Device Identifier encoded as an octet string with a maximum length of 100 chars
        # - key PI encoded as a valid UTF-8 string with a maximum length of 128 bytes
        # - optional key PH encoded as a variable-length decimal number in ASCII text, omitting any leading zeroes
        # If present value must be different of 0
        # DUT must publish AAAA records for each IPv6 address upon which they are willing to accept CHIP messages
        #
        logger.info("4.2.1-5: TH")
        self.next_step()

        # DUT: Reboot DUT, put in non Commissioning Mode and start advertising its availability for commissioning
        # no desc
        logger.info(
            "DUT: Reboot DUT, put in non Commissioning Mode and start advertising its availability for commissioning")
        self.next_step()

        # 4.2.1-5 TH: Check DNS-SD subtypes used by DUT
        # Check DUT advertising for:
        # - DNS-SD instance name must be 64-bit randomly selected ID expressed as a sixteen-char hex string with capital letters and must be different from the one at step 3
        # - service type must be _matterc
        # _udp
        # - service domain is
        # local
        # For Unicast DNS such as used on Thread the service domain SHALL be as configured automatically by the Thread Border Router
        # - target hostname is the 48bit MAC address expressed as a twelve capital letter hex string
        # If the MAC is randomized for privacy, the randomized version must be used each time
        # - subtype _S<dd> 4-bit short discriminator, encoded as a variable-length decimal number in ASCII text, omitting any leading zeroes
        # - subtype _L<dddd> 12-bit long discriminator, encoded as a variable-length decimal number in ASCII text, omitting any leading zeroes
        # - subtype _C<d> must have a value of 0
        # - subtype _A1 must be present
        # - if optional subtype _V<ddddd> is present must be 16-bit vendor id, encoded as a variable-length decimal number in ASCII text, omitting any leading zeroes
        # - if optional subtype _T<ddd> is present, <ddd> represents device type from Data Model and must be represented as a variable length decimal number in ASCII without leading zeroes
        # - key D must be present and represents the discriminator which must be encoded as a variable-lenght decimal value with up to 4 digits omitting any leading zeroes
        # - if optional VP key is present must contain at least Vendor ID and if Product ID is present, values must be separated by a + sign
        #
        # - key AP=1 must be present
        # - if key CM is present must have a value of 0
        # - if optional DT key is present must contain the device type identifier from Data Model Device Types and must be encoded as a variable length decimal ASCII number without leading zeroes
        # - if optional DN key is present must be a UTF-8 encoded string with a maximum length of 32B
        # - if optional key RI is present must include the Rotating Device Identifier encoded as an octet string with a maximum length of 100 chars
        # - key PI encoded as a valid UTF-8 string with a maximum length of 128 bytes
        # - key PH encoded as a variable-length decimal number in ASCII text, omitting any leading zeroes
        # If present value must be different of 0
        # DUT must publish AAAA records for each IPv6 address upon which they are willing to accept CHIP messages
        #
        logger.info("4.2.1-5 TH: Check DNS-SD subtypes used by DUT")
        self.next_step()

    async def cleanup(self) -> None:
        logger.info("No cleanup")
