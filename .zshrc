# Function to get the current git branch
function parse_git_branch() {
    git branch 2> /dev/null | sed -n -e 's/^\* \(.*\)/ [\1]/p'
}

# Function to get virtual environment name
function parse_virtual_env() {
    if [[ -n "$VIRTUAL_ENV" ]]; then
        echo " [${VIRTUAL_ENV##*/}]"
    fi
}

# Change Prompt
setopt PROMPT_SUBST
export VIRTUAL_ENV_DISABLE_PROMPT=1
export PROMPT='%S[%1~]$(parse_git_branch)$(parse_virtual_env)%s '

# Changes shell to vi mode
bindkey -v

# Aliases cdk to clear before running
alias cdk="clear ; cdk"

# Start tmux by default
if [ -z "$TMUX" ]; then
    tmux attach-session || tmux new-session -c ~/my_folder
fi

# Alias to start tmux session script
alias tcd="~/my_folder/configs/start_tmux_session.sh"

# Aliases grep to exclude directories that make me cry
alias grep='clear ; grep \
    --exclude-dir ".idea" \
    --exclude-dir ".git" \
    --exclude-dir ".serverless" \
    --exclude-dir ".venv" \
    --exclude-dir "__pycache__" \
    --exclude-dir "cdk.out" \
    --exclude-dir "node_modules" \
    --exclude-dir "python_modules" \
    --exclude-dir "venv" \
'
