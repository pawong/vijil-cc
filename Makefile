# Project makefile

procs = $(shell ps -ef | grep  'api.main:api' | grep -v grep | awk '{ print $$2 ; }')
killcmd := $(if $(procs), "kill" "-9" $(procs), "echo" "no matching processes")

build:
	@echo "Building"
	@cd src/server && poetry install
	@cd src/client && poetry install
	@echo "build complete."

start-server:
	@echo "Starting server..."
	@cd src/server && nohup poetry run uvicorn api.main:api &
	@echo "server has started."

stop-server:
	@echo 'Stopping server processes: ['$(procs)']'
	@$(killcmd)
	@echo "server has been stopped."

benchmarks:
	@echo 'Collecting benchmarks...'
	@cd src/client && poetry run python main.py
	@echo 'Done.'
