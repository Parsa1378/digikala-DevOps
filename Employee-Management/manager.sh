#!/bin/bash
if [ "$1" = "city" ]; then
    employees=$(grep -i "$2" employee.csv)
    if [ -z "$employees" ]; then
        echo "no employees found"
    
    else
        while read -r line; do
        name=$(echo "$line" | cut -d ',' -f 3)
        echo "Customer Name: "$name""
        number=$(echo "$line" | cut -d ',' -f 4)
        echo "Mobile No: $number"
        done <<< "$employees"
    fi
elif [ "$1" = "bonus" ]; then
    employee=$(grep "$2" employee.csv)
    salary=$(echo $employee | cut -d ',' -f 5)
    name=$(echo $employee | cut -d ',' -f 3)
    bonus=$(echo "$salary * 0.05" | bc)
    bonus=$(printf "%.0f" $bonus)
    echo ""$name" will get \$$bonus bonus"
else
    echo "command not found"
    exit 1
fi