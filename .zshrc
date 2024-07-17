# ------------------------------ MISCELLANEOUS ------------------------------ #
# Changes shell to vi mode
bindkey -v

# -------------------------- ENVIRONMENT VARIABLES -------------------------- #
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
VIRTUAL_ENV_DISABLE_PROMPT=1
PROMPT='%F{141}%K{236}%S[%1~]$(parse_git_branch)$(parse_virtual_env)%s '

# Set editor
EDITOR=nvim

# Save command history
HISTFILE=~/.histfile
SAVEHIST=1000

# --------------------------------- ALIASES --------------------------------- #
# Aliases cdk to clear before running
alias cdk="clear ; cdk"

# Alias to start tmux session script
alias tcd="~/configs/start_tmux_session.sh"

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
