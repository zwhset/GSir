#!/bin/bash
# Gsir restart
echo "Stop GSir... "
/usr/bin/supervisorctl -c supervisor.conf stop gsir
echo "Start GSir"
/usr/bin/supervisorctl -c supervisor.conf start gsir
echo "Restart Over.."

