# This script takes a path as an optional argument.
# If no argument is provided, it defaults to the home directory.
# It will determine the bottom directory of the path and attach to that session.
# If the session does not exist, it will create a new tmux session with that name and path.

#!/usr/bin/env bash
if [ -z $1 ]
then
    path="$HOME"
    session_name="Home"
else
    if [[ $1 == */ ]]; then
        path="$PWD/${1:0:${#1}-1}"
    else
        path="$PWD/$1"
    fi
    session_name="${path##*/}"
fi

tmux has-session -t "$session_name"
if [ $? != 0 ]
then
    tmux new-session -d -s "$session_name" -c "$path" -n "Home"
fi

if [ -z $TMUX ]
then
    tmux attach-session -t "$session_name:1"
else
    tmux switch-client -t "$session_name:1"
fi
