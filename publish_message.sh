#!/bin/bash

message_body="$1"
if [ -z "$message_body" ]; then
  echo "Error: No se proporcionó cuerpo del mensaje. Proporcione un mensaje como argumento."
  exit 1
fi

python sns_publish.py "$1"