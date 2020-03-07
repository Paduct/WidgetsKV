# coding: utf-8
# Copyright 2019

"""Accumulate of resources."""

from os import path
from typing import Tuple

WKV_FILE_PATH: str = path.dirname(__file__)

WKV_SEPARATOR_LINE: str = path.join(WKV_FILE_PATH, "separator_line.kv")
WKV_ABOUT_DIALOG: str = path.join(WKV_FILE_PATH, "about_dialog.kv")
WKV_PATH_CHOOSER: str = path.join(WKV_FILE_PATH, "path_chooser.kv")
WKV_PANEL_MENU: str = path.join(WKV_FILE_PATH, "panel_menu.kv")

WKV_ALL_FILES: Tuple[str, ...] = (WKV_SEPARATOR_LINE, WKV_ABOUT_DIALOG,
                                  WKV_PATH_CHOOSER, WKV_PANEL_MENU)
