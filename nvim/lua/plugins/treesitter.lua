require'nvim-treesitter.configs'.setup {
    ensure_installed = {"vim", "lua", "python", "sql", "nix"},
    sync_install = false,
    auto_install = true,
    highlight = {
        enable = true,
        additional_vim_regex_highlighting = true,
    },
}
