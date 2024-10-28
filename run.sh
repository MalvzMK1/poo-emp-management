if [ -n "$1" ] && [ "$1" = "--no-cache" ]; then
  find $(pwd) -type d -name "*pycache*" -exec rm -r {} \; 2> /dev/null
fi 

./venv/bin/python main.py
