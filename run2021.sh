#!/usr/bin/env bash
# -*- coding: utf-8 -*-

RED='\033[0;31m'
NC='\033[0m' # No Color

for file in $(find . * | grep -P "./AOC-2021-..\.py"); do
	echo -e "${RED}$file${NC}"
	python3 $file
done
