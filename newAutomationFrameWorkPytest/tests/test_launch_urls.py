from newAutomationFrameWorkPytest.PageObjectsUI import PageObjectsUI


def test_ui_validate_youtube_is_launched_on_browser(ui: PageObjectsUI):
    applicationUrl = "https://www.youtube.com/"
    ui.navigation.launch_application(applicationUrl)
    assert ui.navigation.get_page_title() == "YouTube"