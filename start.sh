#!/usr/bin/env bash

apt-get update && apt-get install python3
bash -c "wget https://bootstrap.pypa.io/ez_setup.py && python3 ez_setup.py && rm ez_setup.py"
bash -c "wget https://bootstrap.pypa.io/get-pip.py && python3 get-pip.py && rm get-pip.py"
pip install ansible==1.9.3

pushd provisioning > /dev/null
ansible-playbook project.yml -i inventories/local -vvvv
popd > /dev/null