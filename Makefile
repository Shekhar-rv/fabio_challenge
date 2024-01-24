# formatting
NONE=\033[00m
RED=\033[01;31m
GREEN=\033[01;32m
YELLOW=\033[01;33m
PURPLE=\033[01;35m
CYAN=\033[01;36m
WHITE=\033[01;37m
BOLD=\033[1m
UNDERLINE=\033[4m

help:
	@echo ""
	@echo "${UNDERLINE} Fabrio Technical Challenge ${NONE}"
	@echo ""
	@echo "${UNDERLINE} Code usage: ${NONE}"
	@echo " ${BOLD}run-python-script ${NONE} : ${GREEN}Runs the python code and outputs the stats into the output folder${NONE}"

run-python-script:
	@echo "${GREEN}Running python script${NONE}"
	@python3 main.py
	@echo "${GREEN}Done${NONE}"