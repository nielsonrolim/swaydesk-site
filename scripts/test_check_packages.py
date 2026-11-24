#!/usr/bin/env python3
"""Tests of check-packages.py. Run: python3 -I -m unittest discover -s scripts -p 'test_*.py'"""
import pathlib
import subprocess
import sys
import tempfile
import unittest

SCRIPT = pathlib.Path(__file__).resolve().parent / "check-packages.py"

CONTROL = "Source: swaydesk\n\nPackage: swaydesk-dock\nArchitecture: any\n\nPackage: swaydesk-drawer\n"
PKGBUILD = "pkgbase=swaydesk\npkgname=(swaydesk-dock  # the dock\n         'swaydesk-drawer')\n"


class CheckPackagesTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = pathlib.Path(self.tmp.name)
        (self.root / "debian").mkdir()
        (self.root / "packaging/arch").mkdir(parents=True)
        self.write(CONTROL, PKGBUILD)

    def tearDown(self):
        self.tmp.cleanup()

    def write(self, control, pkgbuild):
        (self.root / "debian/control").write_text(control, encoding="utf-8")
        (self.root / "packaging/arch/PKGBUILD").write_text(pkgbuild, encoding="utf-8")

    def run_with(self, *packages):
        data = self.root / "components.toml"
        data.write_text("".join(f'[[components]]\nid = "c{i}"\npackage = "{p}"\n\n' for i, p in enumerate(packages)),
                        encoding="utf-8")
        return subprocess.run([sys.executable, "-I", str(SCRIPT), str(self.root), str(data)],
                              capture_output=True, text=True)

    def test_known_and_empty_packages_pass(self):
        result = self.run_with("swaydesk-dock", "swaydesk-drawer", "")
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_an_unknown_package_fails_on_both_distros(self):
        result = self.run_with("swaydesk-dock", "swaydesk-audio")
        self.assertEqual(result.returncode, 1)
        self.assertIn("c1: swaydesk-audio is not a package in debian/control", result.stdout)
        self.assertIn("c1: swaydesk-audio is not a package in PKGBUILD", result.stdout)
        self.assertNotIn("c0", result.stdout)

    def test_a_package_only_on_one_distro_fails(self):
        self.write(CONTROL, "pkgname=(swaydesk-dock)\n")
        result = self.run_with("swaydesk-drawer")
        self.assertEqual(result.returncode, 1)
        self.assertEqual(result.stdout.strip(), "c0: swaydesk-drawer is not a package in PKGBUILD")

    def test_a_missing_tree_fails(self):
        result = subprocess.run([sys.executable, "-I", str(SCRIPT), str(self.root / "nothing")],
                                capture_output=True, text=True)
        self.assertEqual(result.returncode, 1)

    def test_no_package_names_fails(self):
        self.write("Source: swaydesk\n", "pkgbase=swaydesk\n")
        self.assertEqual(self.run_with("swaydesk-dock").returncode, 1)


if __name__ == "__main__":
    unittest.main()
