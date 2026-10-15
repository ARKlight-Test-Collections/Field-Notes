# include <stdlib.ARKlight>

from content.site_content import FOOTER_TEXT


def footer():
    return Footer(
        Container(
            Text("FIELD NOTES SUPPLY", class_name="footer-brand"),
            Text(FOOTER_TEXT, class_name="footer-copy"),
            Text("DESIGNED FOR WEATHER / MADE FOR DISTANCE", class_name="footer-coordinate"),
            class_name="footer-inner",
        ),
        class_name="site-footer site-frame",
    )
