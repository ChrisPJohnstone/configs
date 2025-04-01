from libqtile import qtile
from libqtile.config import Group, Key
from libqtile.lazy import LazyCall, lazy

from .type_definitions import Directions


class KeyBindings:
    def __init__(
        self,
        mod: str,
        terminal: str,
        groups: list[Group],
        directions: Directions,
    ) -> None:
        self.mod = mod
        self.terminal = terminal
        self.groups = groups
        self.directions = directions

    @property
    def mod(self) -> str:
        return self._mod

    @mod.setter
    def mod(self, value: str) -> None:
        self._mod: str = value

    @property
    def terminal(self) -> str:
        return self._terminal

    @terminal.setter
    def terminal(self, value: str) -> None:
        self._terminal: str = value

    @property
    def groups(self) -> list[Group]:
        return self._groups

    @groups.setter
    def groups(self, value: list[Group]) -> None:
        self._groups: list[Group] = value

    @property
    def directions(self) -> Directions:
        return self._directions

    @directions.setter
    def directions(self, value: Directions) -> None:
        self._directions: Directions = value

    def _bind(
        self,
        modifiers: list[str],
        key: str,
        *commands: LazyCall,
        desc: str = "",
        swallow: bool = False,
    ) -> Key:
        return Key(modifiers, key, *commands, desc=desc, swallow=swallow)

    def refresh_config(self, modifiers: list[str], key: str) -> Key:
        commands: list[LazyCall] = [lazy.reload_config()]
        desc: str = "Reload the config"
        return self._bind(modifiers, key, *commands, desc=desc)

    def spawn_launcher(self, modifiers: list[str], key: str) -> Key:
        commands: list[LazyCall] = [lazy.spawn("rofi -show drun")]
        desc: str = "Spawn a command using a prompt widget"
        return self._bind(modifiers, key, *commands, desc=desc)

    def spawn_terminal(self, modifiers: list[str], key: str) -> Key:
        commands: list[LazyCall] = [lazy.spawn(self.terminal)]
        desc: str = "Launch Terminal"
        return self._bind(modifiers, key, *commands, desc=desc)

    def kill_window(self, modifiers: list[str], key: str) -> Key:
        commands: list[LazyCall] = [lazy.window.kill()]
        desc: str = "Kill focused window"
        return self._bind(modifiers, key, *commands, desc=desc)

    def shutdown_qtile(self, modifiers: list[str], key: str) -> Key:
        commands: list[LazyCall] = [lazy.shutdown()]
        desc: str = "Shutdown qtile"
        return self._bind(modifiers, key, *commands, desc=desc)

    def move_group(self, modifiers: list[str]) -> list[Key]:
        return [
            self._bind(
                modifiers,
                group.name,
                lazy.group[group.name].toscreen(),
                desc="Switch to group {group.name}",
            )
            for group in self.groups
        ]

    def move_window_to_group(self, modifiers: list[str], follow: bool) -> list[Key]:
        return [
            self._bind(
                modifiers,
                group.name,
                lazy.window.togroup(group.name, switch_group=follow),
                desc="Move focused window to {group.name}. Follow {follow}",
            )
            for group in self.groups
        ]

    def move_focus(self, modifiers: list[str]) -> list[Key]:
        return [
            self._bind(
                modifiers,
                key,
                eval(f"lazy.layout.{direction}()"),
                desc="Move focus {direction}",
            )
            for direction, key in self.directions.items()
        ]

    def move_window(self, modifiers: list[str]) -> list[Key]:
        return [
            self._bind(
                modifiers,
                key,
                eval(f"lazy.layout.shuffle_{direction}()"),
                desc="Move focused window {direction}",
            )
            for direction, key in self.directions.items()
        ]

    def grow_window(self, modifiers: list[str]) -> list[Key]:
        return [
            self._bind(
                modifiers,
                key,
                eval(f"lazy.layout.grow_{direction}()"),
                desc="Grow focused window {direction}",
            )
            for direction, key in self.directions.items()
        ]

    def reset_sizes(self, modifiers: list[str], key: str) -> Key:
        commands: list[LazyCall] = [lazy.layout.normalize()]
        desc: str = "Reset all window sizes"
        return self._bind(modifiers, key, *commands, desc=desc)

    def toggle_fullscreen(self, modifiers: list[str], key: str) -> Key:
        commands: list[LazyCall] = [lazy.window.toggle_fullscreen()]
        desc: str = "Toggle fullscreen on the focused window"
        return self._bind(modifiers, key, *commands, desc=desc)

    def toggle_floating(self, modifiers: list[str], key: str) -> Key:
        commands: list[LazyCall] = [lazy.window.toggle_floating()]
        desc: str = "Toggle floating on the focused window"
        return self._bind(modifiers, key, *commands, desc=desc)

    def cycle_layout(self, modifiers: list[str], key: str) -> Key:
        commands: list[LazyCall] = [lazy.next_layout()]
        desc: str = "Cycle between layouts"
        return self._bind(modifiers, key, *commands, desc=desc)

    def switch_vt(self, modifiers: list[str]) -> list[Key]:
        """
        TODO: Figure out what any of this means
        Add key bindings to switch VTs in Wayland.
        We can't check qtile.core.name in default config as it is loaded before qtile is started
        We therefore defer the check until the key binding is run by using .when(func=...)
        """
        return [
            self._bind(
                modifiers,
                f"f{n}",
                lazy.core.change_vt(n).when(func=lambda: qtile.core.name == "wayland"),
                desc=f"Switch to VT {n}",
            )
            for n in range(1, 8)
        ]

    def init_bindings(self) -> list[Key]:
        return [
            self.refresh_config([self.mod, "control"], "r"),
            self.spawn_launcher([self.mod], "space"),
            self.spawn_terminal([self.mod], "Return"),
            self.kill_window([self.mod, "shift"], "q"),
            self.shutdown_qtile([self.mod, "shift"], "e"),
            *self.move_group([self.mod]),
            *self.move_window_to_group([self.mod, "shift"], follow=False),
            *self.move_focus([self.mod]),
            *self.move_window([self.mod, "shift"]),
            *self.grow_window([self.mod, "control"]),
            self.reset_sizes([self.mod], "n"),
            self.toggle_fullscreen([self.mod], "f"),
            self.toggle_floating([self.mod], "t"),
            self.cycle_layout([self.mod], "tab"),
            *self.switch_vt(["control", "mod1"]),
        ]
