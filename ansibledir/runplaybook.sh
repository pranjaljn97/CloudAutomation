#!/bin/bash
playbook=$1
envfile=$2

sudo ansible-playbook $playbook --extra-vars @$envfile 
