#!/usr/bin/env bash
CONNECTED_STATES=('Connecting' 'Connected' 'Reconnecting' 'DisconnectingToReconnect')
DISCONNECTED_STATES=('Disconnected' 'Interrupted' 'Disconnecting')

status=$(piactl get connectionstate)

if printf '%s\0' "${CONNECTED_STATES[@]}" | grep -Fxqz -- "${status}"; then
    echo 'Disconnecting'
    piactl disconnect
    exit 1
fi

if printf '%s\0' "${DISCONNECTED_STATES[@]}" | grep -Fxqz -- "${status}"; then
    echo 'Connecting'
    piactl connect
    exit 1
fi

echo "Unknown status ${status}"
exit 0
