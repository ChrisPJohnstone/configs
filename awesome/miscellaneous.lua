-- Tag layout
-- TODO: Research
tag.connect_signal(
  "request::default_layouts",
  function()
    awful.layout.append_default_layouts({
      awful.layout.suit.floating,
      awful.layout.suit.tile,
      awful.layout.suit.tile.left,
      awful.layout.suit.tile.bottom,
      awful.layout.suit.tile.top,
      awful.layout.suit.fair,
      awful.layout.suit.fair.horizontal,
      awful.layout.suit.spiral,
      awful.layout.suit.spiral.dwindle,
      awful.layout.suit.max,
      awful.layout.suit.max.fullscreen,
      awful.layout.suit.magnifier,
      awful.layout.suit.corner.nw,
    })
  end
)

-- Keyboard map indicator and switcher
-- TODO: Research
mykeyboardlayout = awful.widget.keyboardlayout()

-- Themes define colours, icons, font and wallpapers.
-- TODO: Research
beautiful.init(gears.filesystem.get_themes_dir() .. "default/theme.lua")

-- Enable sloppy focus, so that focus follows mouse.
client.connect_signal(
  "mouse::enter",
  function(c) c:activate {context = "mouse_enter", raise = false} end
)
