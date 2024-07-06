return {
    "williamboman/mason.nvim",
    config = function()
        local mason = require("mason")

        mason.setup {
            ui = {
                icons = {
                    package_installed = "✓",
                    package_pending = "➜",
                    package_uninstalled = "✗",
                },
            },
            ensure_installed = {
                "debugpy",
                "pyright",
            },
        }
    end,
}
