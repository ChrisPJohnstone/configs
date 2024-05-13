session_name="${1##*/}"

tmux has-session -t "$session_name"
if [ $? != 0 ]
then
    tmux new-session -d -s "$session_name" -c "$1" -n "Editing"
    tmux new-window -t "$session_name" -c "$1" -n "Testing"
fi
tmux switch-client -t "$session_name:Editing"
