-- Window resizing using Ctrl + hjkl
vim.api.nvim_set_keymap("n", "<C-W><C-h>", "<C-W><", {noremap = true})
vim.api.nvim_set_keymap("n", "<C-W><C-j>", "<C-W>+", {noremap = true})
vim.api.nvim_set_keymap("n", "<C-W><C-k>", "<C-W>-", {noremap = true})
vim.api.nvim_set_keymap("n", "<C-W><C-l>", "<C-W>>", {noremap = true})

-- Command for encasing
vim.g.mapleader = "\\"
vim.api.nvim_set_keymap("n", "<leader>'", "ciw'<C-R>\"'<ESC>bh", {noremap = true})
vim.api.nvim_set_keymap("n", "<leader>\"", "ciw\"<C-R>\"\"<ESC>bh", {noremap = true})
vim.api.nvim_set_keymap("n", "<leader>`", "ciw`<C-R>\"`<ESC>bh", {noremap = true})
