#!/bin/bash
playbook=$1
envfile=$2
hostip=$3
sudo ansible-playbook $playbook --extra-vars @$envfile 
