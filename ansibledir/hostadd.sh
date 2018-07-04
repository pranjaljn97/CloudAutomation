#!/bin/bash
playbook=$1
envfile=$2
echo $envfile
sudo ansible-playbook $playbook --extra-vars "$envfile"