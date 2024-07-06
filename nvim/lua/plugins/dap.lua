return {
    "mfussenegger/nvim-dap",
    dependencies = {
        -- "williamboman/mason.nvim",
        "nvim-neotest/nvim-nio",
        "rcarriga/nvim-dap-ui",
    },
    config = function()
        local dap = require('dap')
        local dapui = require("dapui")

        require("dapui").setup()

        vim.keymap.set("n", "<leader>b", dap.toggle_breakpoint)
        vim.keymap.set("n", "<leader>gb", dap.run_to_cursor)
        vim.keymap.set("n", "<F1>", dap.continue)
        vim.keymap.set("n", "<F2>", dap.step_into)
        vim.keymap.set("n", "<F3>", dap.step_over)
        vim.keymap.set("n", "<F4>", dap.step_out)
        vim.keymap.set("n", "<F5>", dap.step_back)
        vim.keymap.set("n", "<F13>", dap.restart)

        dap.adapters.python = {
            type = 'executable';
            command = "python3";
            args = { '-m', 'debugpy.adapter' };
        }
        dap.configurations.python = {
            {
                type = 'python';
                request = 'launch';
                program = "${file}";
                console = "internalConsole";
            },
        }

        dap.listeners.before.attach.dapui_config = function()
            dapui.open()
        end
        dap.listeners.before.launch.dapui_config = function()
            dapui.open()
        end
        dap.listeners.before.event_terminated.dapui_config = function()
            dapui.close()
        end
        dap.listeners.before.event_exited.dapui_config = function()
            dapui.close()
        end
    end,
}
