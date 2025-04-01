if [ -z $1 ]
then
    path="~"
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
