yum install iscsi-initiator-utils -y
iscsiadm --mode discoverydb --type sendtargets --portal 192.168.122.163 --discover
iscsiadm --mode node --targetname cool --portal 192.168.122.163:3260 --login
