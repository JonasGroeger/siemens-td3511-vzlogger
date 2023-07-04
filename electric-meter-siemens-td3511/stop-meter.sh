#!/usr/bin/env sh

# Makes the Siemens TD3511 stop sending data
# See 5.2.8.12. Break B0 in amis_td3510.pdf

# SOH B 0 ETX BCC \r \n
echo -en '\x01\x42\x30\x03\x71\x0D\x0A' > /dev/ttyUSB0
