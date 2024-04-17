" Turn on syntax highlighting & and color scheme
colorscheme slate
syntax on

" Colour Overrides
highlight Normal ctermbg=None
highlight StatusLine ctermbg=magenta ctermfg=black
highlight StatusLineNC ctermbg=magenta ctermfg=black 
highlight VertSplit ctermfg=magenta ctermbg=None

" Syntax corrections for unsupported file types
augroup SyntaxHighlighting
    autocmd!
    autocmd BufNewFile,BufRead *.md set filetype=text
    autocmd BufNewFile,BufRead *.q set filetype=sql
augroup END

" Display line number & highlight line cursor is on
set scrolloff=100
set number
augroup RelativeNumberToggle
    autocmd!
    autocmd BufEnter,FocusGained,WinEnter * if &number | set relativenumber | endif
    autocmd BufLeave,FocusLost,WinLeave   * if &number | set norelativenumber | endif
augroup END

" Add a vertical ruler at char 80 & make it light grey
augroup LineLengthMarkers
    autocmd!
    autocmd BufNewFile,Bufread *.py set colorcolumn=80
    autocmd BufNewFile,BufRead *.sql set colorcolumn=120
augroup END
highlight ColorColumn ctermbg=8

" Always show status bar
set laststatus=2
set statusline=[%f]\ %y\ %=\ [Column:\ %v]

" Set tab length to 4 & use spaces
set shiftwidth=4
set tabstop=4
set expandtab
set smartindent

" Window resizing using Ctrl + hjkl
nnoremap <C-W><C-h> <C-W><
nnoremap <C-W><C-j> <C-W>+
nnoremap <C-W><C-k> <C-W>-
nnoremap <C-W><C-l> <C-W>>

" Highlight matches while searching
set hlsearch

" Tabable options when autocompleting in command mode
" set wildmenu
set wildmode=longest

" For all those times you hit a button and you're not sure what it was
set showcmd

" Enable backspacing to previous line
set backspace=eol,start

" Disable that gahd damn bell
set visualbell

" Command for encasing
let mapleader="\\"
nnoremap <leader>' ciw'<C-R>"'<ESC>bh
nnoremap <leader>" ciw"<C-R>""<ESC>bh
