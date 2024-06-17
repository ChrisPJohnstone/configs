require'nvim-treesitter.configs'.setup {
    ensure_installed = {
        "json",
        "lua",
        "nix",
        "python",
        "sql",
        "tmux",
        "vim",
        "vimdoc",
    },
    sync_install = false,
    auto_install = true,
    highlight = {
        enable = true,
        additional_vim_regex_highlighting = true,
    },
    indent = {
        enable = true,
    },
}
