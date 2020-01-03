#!/bin/sh

export SLACK_BOT_TOKEN=$1
export SLACK_SIGNING_SECRET=$2

while true; do
  python3 ./QuestionHelper.py 2>&1 >> log.log 
done

