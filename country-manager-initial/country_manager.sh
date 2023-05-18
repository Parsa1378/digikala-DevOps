#!/bin/bash

if [ "$#" -lt 2 ]; then
    echo "not enough arguments"
    exit 1
fi

command=$1
filepath=$2

if [ "$command" != "block" ] && [ "$command" != "unblock" ]; then
    echo "invalid command"
    exit 1
fi

if [ ! -f "$filepath" ]; then
  echo "ip list file not found"
  exit 1
fi

# Function to block incoming requests
block_requests() {
  ip_list=$(cat "$filepath")

  for ip_range in $ip_list; do
    sudo iptables -D INPUT -s "$ip_range" -j ACCEPT 2>/dev/null
    sudo iptables -A INPUT -s "$ip_range" -j DROP
  done
}

# Function to unblock incoming requests
unblock_requests() {
  ip_list=$(cat "$filepath")

  for ip_range in $ip_list; do
    sudo iptables -D INPUT -s "$ip_range" -j DROP 2>/dev/null
    sudo iptables -A INPUT -s "$ip_range" -j ACCEPT
  done
}

# Check the command and perform the respective action
if [ "$command" == "block" ]; then
  block_requests
elif [ "$command" == "unblock" ]; then
  unblock_requests
fi

