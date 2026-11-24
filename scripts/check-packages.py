#!/usr/bin/env python3
"""Checks that every package the component pages install exists. Usage:

    check-packages.py <swaydesk checkout> [data/components.toml]

The checkout is a clone of github.com/nielsonrolim/swaydesk (or any tree with its debian/control and
packaging/arch/PKGBUILD). Each non-empty `package` in the data file (components and [groups.*]) must be a
`Package:` of debian/control and a name in the PKGBUILD's pkgname=(...), since the pages print both
`apt install` and `pacman -Syu` lines; a swaydesk-* name in `arch_with` must be in the PKGBUILD.
A missing file, or one with no package names, is an error, never a pass.
"""
import pathlib
import re
import sys
import tomllib


def debian_names(control):
    return set(re.findall(r"(?m)^Package:\s*(\S+)", control))


def arch_names(pkgbuild):
    match = re.search(r"(?ms)^pkgname=\((.*?)\)", pkgbuild)
    if not match:
        return set()
    return set(re.sub(r"#[^\n]*", "", match.group(1)).replace("'", " ").replace('"', " ").split())


def main(argv):
    if len(argv) not in (2, 3):
        print(__doc__, file=sys.stderr)
        return 2
    tree = pathlib.Path(argv[1])
    data = pathlib.Path(argv[2] if len(argv) == 3 else "data/components.toml")
    try:
        debian = debian_names((tree / "debian/control").read_text(encoding="utf-8"))
        arch = arch_names((tree / "packaging/arch/PKGBUILD").read_text(encoding="utf-8"))
        loaded = tomllib.loads(data.read_text(encoding="utf-8"))
        components = loaded["components"]
        data_groups = loaded.get("groups", {})
    except (OSError, KeyError, tomllib.TOMLDecodeError) as error:
        print(f"error: {error}", file=sys.stderr)
        return 1
    if not debian or not arch:
        print("error: no package names in debian/control or the PKGBUILD's pkgname", file=sys.stderr)
        return 1
    errors = []
    checks = [(c["id"], c.get("package", ""), c.get("arch_with", [])) for c in components]
    checks += [(f"groups.{name}", g.get("package", ""), g.get("arch_with", [])) for name, g in data_groups.items()]
    for where, package, arch_with in checks:
        if package:
            for distro, names in (("debian/control", debian), ("PKGBUILD", arch)):
                if package not in names:
                    errors.append(f"{where}: {package} is not a package in {distro}")
        # Our own packages in the pacman line must exist too (the others are the distro's).
        for extra in arch_with:
            if extra.startswith("swaydesk-") and extra not in arch:
                errors.append(f"{where}: arch_with {extra} is not a package in PKGBUILD")
    for line in errors:
        print(line)
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
