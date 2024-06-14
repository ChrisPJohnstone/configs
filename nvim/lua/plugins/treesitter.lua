require'nvim-treesitter.configs'.setup {
    ensure_installed = {
        "json",
        "lua",
        "nix",
        "python",
        "sql",
        "vim",
        "vimdoc",
    },
    sync_install = false,
    auto_install = true,
    highlight = {
        enable = true,
        additional_vim_regex_highlighting = true,
    },
}
