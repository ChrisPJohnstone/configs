-- Set tab length to 4 & use spaces
vim.opt.shiftwidth = 4
vim.opt.tabstop = 4
vim.opt.expandtab = true
vim.opt.smartindent = true

-- Disable linewrapping
vim.opt.wrap = false

-- Remove directories from vimgrep
vim.opt.wildignore:append("*/__pycache__/*")
vim.opt.wildignore:append("*/node_movules/*")
vim.opt.wildignore:append("*/.venv/*")
vim.opt.wildignore:append("*/venv/*")
