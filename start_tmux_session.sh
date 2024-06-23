if [ -z $1 ]
then
    path="~"
    session_name="Home"
else
    path=$1
    session_name="${path##*/}"
fi

tmux has-session -t "$session_name"
if [ $? != 0 ]
then
    tmux new-session -d -s "$session_name" -c "$path" -n "Home"
    tmux new-window -t "$session_name" -c "$path" -n "Test"
fi

if [ -z $TMUX ]
then
    tmux attach-session -t "$session_name:1"
else
    tmux switch-client -t "$session_name:1"
fi
