# Change Prompt
parse_git_branch() {
    git branch 2> /dev/null | sed -n -e 's/^\* \(.*\)/ [\1]/p'
}
setopt PROMPT_SUBST
export PROMPT='%S[%D{%T}] [%1~]$(parse_git_branch)%s '

# Changes shell to vi mode
bindkey -v

# Aliases grep to exclude directories that make me cry
alias grep='grep --exclude-dir "__pycache__" --exclude-dir "cdk.out" --exclude-dir ".git" --exclude-dir ".venv"'
 
 # Start tmux by default
 tmux attach-session || tmux new-session -c ~/my_folder
