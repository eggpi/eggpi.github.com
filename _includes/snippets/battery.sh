#!/bin/bash

while :; do
    now=$(awk '(NR == 5) {print $3}' /proc/acpi/battery/BAT0/state)
    total=$(awk '(NR == 3) {print $4}' /proc/acpi/battery/BAT0/info)

    echo $now $total | \
        awk '{ printf("\r%d/%d mWh (%.1f%%)", $1, $2, 100*$1/$2) }'

    sleep 2
done
