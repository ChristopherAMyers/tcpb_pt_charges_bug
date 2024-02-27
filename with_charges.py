#!/usr/bin/env python
# Basic energy calculation
import sys
import numpy as np
from tcpb import TCProtobufClient as TCPBClient

if len(sys.argv) != 3:
    print("Usage: {} host port".format(sys.argv[0]))
    exit(1)

# Water system
atoms = ["O", "H", "H"]
geom = np.array([
    [-4.4798000, -2.8400000,  4.2456000],
    [-4.8525000, -3.7649000,  4.3951000],
    [-3.6050000, -2.7568000,  4.9264000]
    ]).flatten().tolist()

with TCPBClient(host=sys.argv[1], port=int(sys.argv[2])) as client:
    # client = TCPBClient(host=sys.argv[1], port=int(sys.argv[2]))
    options = {
        "atoms": atoms,
        "charge": 0,
        "spinmult": 1,
        "closed_shell": True,
        "restricted": True,
        "method": "camb3lyp",
        "basis": "6-31g",
        "pointcharges" : "charges.xyz"
    }
    #   calculation
    result = client.compute_job_sync("energy", geom, "angstrom", **options)
    # print("Results:\n{}".format(result))
