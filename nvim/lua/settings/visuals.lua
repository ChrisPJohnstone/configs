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

-- For all those times you hit a button and you're not sure what it was
vim.opt.showcmd = true

-- Highlight matches to current search buffer
vim.opt.hlsearch = true
