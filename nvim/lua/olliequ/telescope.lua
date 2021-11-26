    local telescope = require('telescope')
    telescope.setup {
        defaults = {
            layout_strategy = "vertical",
        },
        pickers = {
            find_files = {
                hidden = true,
            },
        },
    }
-- To get fzf loaded and working with telescope,
-- you need to call load_extension, somewhere after
-- the setup function.
telescope.load_extension('fzf')
