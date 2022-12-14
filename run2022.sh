#!/usr/bin/env bash
# -*- coding: utf-8 -*-

BLACK='\u001b[30m'
RED='\033[0;31m'
GREEN='\u001b[32m'
BGREEN='\u001b[42m'
BLINK='\033[5m'
NC='\033[0m' # No Color
BAR='________________________________________________________'
HALFBAR='                 '

start=$(date +%s.%N)
for file in $(find . * | grep -P "./AOC_2022_..\.py" | sort); do
    echo -e "\n🎄 ${BGREEN}${BLACK}${HALFBAR}$file${HALFBAR}${NC} 🎄\n"
    python3 $file
done
end=$(date +%s.%N)

runtime=$(echo "scale=2; ($end - $start)*100/100" | bc -l)

echo -e "${BAR}\nExecuted in: ${runtime} secs${NC}"
