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

-- Change status bar format
vim.opt.statusline = "[%f] %y %m %= [Column: %v]";

-- For all those times you hit a button and you're not sure what it was
vim.opt.showcmd = true

-- Highlight matches to current search buffer
vim.opt.hlsearch = true

-- Disable linewrapping but have settings in case I enable it
vim.opt.wrap = false
vim.opt.linebreak = true
vim.opt.breakat = " "
vim.opt.breakindent = true
vim.opt.breakindentopt = "shift:2"
vim.opt.showbreak = "↪"
