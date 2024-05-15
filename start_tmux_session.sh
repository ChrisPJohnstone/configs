if [ -z $1 ]
then
    path="~/my_folder"
else
    path=$1
fi
session_name="${path##*/}"

tmux has-session -t "$session_name"
if [ $? != 0 ]
then
    tmux new-session -d -s "$session_name" -c "$path" -n "Editing"
    tmux new-window -t "$session_name" -c "$path" -n "Testing"
fi
tmux switch-client -t "$session_name:Editing"
