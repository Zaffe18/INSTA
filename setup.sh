#!/bin/env bash
if [[ $(command -v python) ]]; then
       echo ""
else
       pkg install python -y
fi
