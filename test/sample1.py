#
# Copyright (C) scenüs, 2023.
# All rights reserved.
# Ehsan Haghpanah; ehsan@scenus.com
#

# https://pypi.org/project/cassandra-driver/

from cassandra.cluster import Cluster
cluster = Cluster(['192.168.1.1', '192.168.1.2'])