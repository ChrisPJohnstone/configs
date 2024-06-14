-- Aesthetic Choices
vim.cmd([[colorscheme slate]])

-- Enable syntax highlighting
vim.opt.syntax = on

-- Display line number & highlight line cursor is on
vim.opt.number = true
vim.api.nvim_create_autocmd(
    {"BufEnter", "FocusGained", "WinEnter"},
    {
        pattern = {"*"},
        callback = function ()
            vim.opt.relativenumber = true
        end
    }
)
vim.api.nvim_create_autocmd(
    {"BufLeave", "FocusLost", "WinLeave"},
    {
        pattern = {"*"},
        callback = function ()
            vim.opt.relativenumber = false
        end
    }
)

-- Add a vertical ruler at char 80 & make it light grey
vim.cmd([[highlight ColorColumn ctermbg=8]])
vim.api.nvim_create_autocmd(
    {"BufNewFile", "BufRead"},
    {
        pattern = {"*.py"},
        callback = function ()
            vim.opt.colorcolumn = "80"
        end
    }
)

-- Always show status bar
vim.opt.laststatus = 2
vim.opt.statusline = "[%f] %y %= [Column: %v]";

-- Set tab length to 4 & use spaces
vim.opt.shiftwidth = 4
vim.opt.tabstop = 4
vim.opt.expandtab = true
vim.opt.smartindent = true

-- Highlight matches to current search buffer
vim.opt.hlsearch = true

-- For all those times you hit a button and you're not sure what it was
vim.opt.showcmd = true

-- Disable linewrapping
vim.opt.wrap = false

-- Remove directories from vimgrep
vim.opt.wildignore:append("*/__pycache__/*")
vim.opt.wildignore:append("*/node_movules/*")
vim.opt.wildignore:append("*/.venv/*")
vim.opt.wildignore:append("*/venv/*")

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
