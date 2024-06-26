-- Set indenting
vim.opt_local.shiftwidth = 4
vim.opt_local.tabstop = 4

-- Add a vertical ruler at char 80 & make it light grey
vim.opt_local.colorcolumn = "80"
vim.cmd([[highlight ColorColumn ctermbg=8]])

-- Set the python interpreter to python3
vim.g.pyindent_open_paren = 4
