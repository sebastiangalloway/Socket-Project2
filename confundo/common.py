# -*- Mode: python; py-indent-offset: 4; indent-tabs-mode: nil; coding: utf-8; -*-
# Copyright 2019 Alex Afanasyev
#
#constants defined and update as per requirements

#MTU = size for congestion control operations is 412 (payload size)
MTU_SIZE = 412

HEADER_SIZE = 12

#Max packet size = The maximum UDP packet size is 424 bytes including a header (412 bytes for the payload)
MAX_PACKET_SIZE = 424

#MAX_SEQNO = The maximum sequence and acknowledgment number should be 50000 and be reset to zero whenever it reaches the maximum value.
MAX_SEQ_NUM = 50000

#Packet retransmission (and appropriate congestion control actions) should be triggered when no data was acknowledged for more than 0.5 seconds (fixed retransmission timeout).
RETX_TIME = 0.5
FIN_WAIT_TIME = 2.0
SYN_WAIT_TIME = 10.0

#Initial slow-start threshold (SS-THRESH) should be 12000
INITIAL_SS_THRESH = 12000

INITIAL_SEQ = 50000

#Initial sequence number should be 50000
GLOBAL_TIMEOUT = 10.0
