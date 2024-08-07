if [ -z $1 ]
then
    path="~"
    session_name="Home"
else
    path="$PWD/$1"
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
