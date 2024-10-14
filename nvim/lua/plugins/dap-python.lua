return {
    "mfussenegger/nvim-dap-python",
    ft = "python",
    dependencies = {
        "mfussenegger/nvim-dap",
    },
    config = function()
        require("dap-python").setup(vim.g.python_host_prog)
    end,
}
