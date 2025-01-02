# import html
# import pytest
import pytest_html


def test_extra_text(extras):
    extras.append(pytest_html.extras.text("some string", name="Directly Added in Report via Test"))


def test_extra_image(extras):
    extras.append(pytest_html.extras.png("./extras_png.png", name="Directly Added in Report via Test"))
