#! /usr/bin/env bash

# Written by Brad Barker, brad.barker@databricks.com July 2021
#
# This program is provided to wait for a given databricks cluster to be in running status.
# This program presumes the databricks cli is installed and configured.
# This program is provided without any warranty.

#######################################
# Waits until cluster is running.
# ARGUMENTS:
#   Cluster id forwhich to wait
# OUTPUTS:
#   String of statuses
# RETURN:
#   0 if succeeds
#######################################

echo "Waiting for run status for cluster: "$1

sleep 5
state_txt=$(databricks clusters get --cluster-id $1 | grep '"state":')
echo $state_txt
while [ "$state_txt" != '  "state": "RUNNING",' ]
do
    sleep 5
    state_txt=$(databricks clusters get --cluster-id $1 | grep '"state":')
    echo $state_txt
done

exit 0
