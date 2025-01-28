-- Open dir of current file
vim.api.nvim_set_keymap("n", "<leader>d", ":e %:h<CR>", {noremap = true})

-- Window resizing using Ctrl + hjkl
vim.api.nvim_set_keymap("n", "<C-W><C-h>", "<C-W><", {noremap = true})
vim.api.nvim_set_keymap("n", "<C-W><C-j>", "<C-W>+", {noremap = true})
vim.api.nvim_set_keymap("n", "<C-W><C-k>", "<C-W>-", {noremap = true})
vim.api.nvim_set_keymap("n", "<C-W><C-l>", "<C-W>>", {noremap = true})
