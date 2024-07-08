-- Set tab length to 4 & use spaces
vim.opt.shiftwidth = 4
vim.opt.tabstop = 4
vim.opt.expandtab = true
vim.opt.smartindent = true

-- Diable mouse interaction
vim.opt.mouse = ""

-- Disable linewrapping
vim.opt.wrap = false

-- Remove directories from vimgrep
vim.opt.wildignore:append("*/__pycache__/*")
vim.opt.wildignore:append("*/node_movules/*")
vim.opt.wildignore:append("*/.venv/*")
vim.opt.wildignore:append("*/venv/*")

-- Map strange filetypes
vim.cmd("autocmd BufRead,BufNewFile *.ddl set filetype=sql")

-- Centre cursor on screen
vim.opt.scrolloff = 999
